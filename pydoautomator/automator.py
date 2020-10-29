from pydoautomator.droplet import Droplet
from pydoautomator.adapters import ApiAdapter
import asyncio
from pydoautomator.errors import DropletCreationError, FloatingIpAssignmentError, TurnoffDropletError, DestroyDropletError


class Automator:
    """Here are the main methods / functions
    Call this class passing the Digital Ocean TOKEN.

    Raises:
        TurnoffDropletError: Error while shutting down droplet
        FloatingIpAssignmentError: Error while assigning floating ip
        DestroyDropletError: Error while destroying droplet
        DropletCreationError: Error while creating droplet

    """

    do_token = ''

    requests = ''
    __base_url = 'https://api.digitalocean.com/v2'

    def __init__(self, do_token: str):
        """constructor

        Args:
            do_token (str): digital ocean token
        """

        self.do_token = do_token
        self.api_adapter = ApiAdapter(self.do_token)
        self.requests = self.api_adapter.requests
        self.__base_url = 'https://api.digitalocean.com/v2'

    def turnoff_droplet(self, droplet_id: int) -> str:
        """Turnoff / Shutdown Droplet

        Args:
            droplet_id (int): droplet id

        Raises:
            TurnoffDropletError: Error if droplet is not shutdown

        Returns:
            str: `completed`
        """

        headers = {'Content-Type': 'application/json'}
        data = {'type': 'shutdown'}

        response = self.requests.post(
            self.__base_url+'/droplets/'+str(droplet_id)+'/actions',
            headers=headers,
            json=data
        )

        if response.status_code != 201:
            raise TurnoffDropletError(response.json())

        action_id = response.json()['action']['id']

        loop2 = asyncio.get_event_loop()
        loop2.run_until_complete(
            self.__wait_till_action_complete(action_id)
        )
        return "completed"

    def get_all_droplets(self) -> list:
        """Get all droplets from Digital Ocean

        Returns:
            list: list of droplets (dict)
        """

        response = self.requests.get(self.__base_url+'/droplets')
        droplets = response.json()['droplets']

        while 'next' in response.json()['links']['pages']:
            response = self.requests.get(
                response.json()['links']['pages']['next'])
            droplets = droplets + response.json()['droplets']

        return droplets

    def assign_floating_ip_to_droplet(self, floating_ip: str, droplet_id: int) -> str:
        """Assigns a floating ip to a droplet

        Args:
            floating_ip (str): Floating IP (i.e.: `125.68.75.2`)
            droplet_id (int): The droplet ID

        Raises:
            FloatingIpAssignmentError: if not completed

        Returns:
            str: return `completed` if completed
        """

        url = self.__base_url + '/floating_ips/' + floating_ip + '/actions'
        data = {
            "type": "assign",
            "droplet_id": droplet_id
        }

        headers = {'Content-Type': 'application/json'}
        response = self.requests.post(url, json=data, headers=headers)

        if response.status_code != 201:
            raise FloatingIpAssignmentError(response.json())

        action_id = response.json()['action']['id']

        loop2 = asyncio.get_event_loop()
        loop2.run_until_complete(
            self.__wait_till_action_complete(action_id)
        )
        if response.status_code == 201:
            return 'completed'

    def create_droplet_from_snapshot(self, droplet: Droplet) -> int:
        """Creates droplet from snapshot/image

        Args:
            droplet (Droplet): Droplet object

        Returns:
            int: `droplet_id` from created droplet
        """

        headers = {'Content-Type': 'application/json'}
        created_droplet = self.requests.post(
            self.__base_url + '/droplets', data=droplet.json(), headers=headers)

        action_id = created_droplet.json()['links']['actions'][0]['id']
        loop = asyncio.get_event_loop()

        loop.run_until_complete(
            self.__wait_till_action_complete(action_id)
        )

        return created_droplet.json()['droplet']['id']

    def destroy_droplet(self, droplet_id: int) -> str:
        """Destroy / Delete droplet

        Args:
            droplet_id (int): droplet id to be destroyed

        Raises:
            DestroyDropletError: if droplet is not destroyed

        Returns:
            str: `completed` if destroyed
        """

        response = self.requests.delete(
            self.__base_url + '/droplets/' + str(droplet_id)
        )

        if response.status_code != 204:
            raise DestroyDropletError(response.json())

        return 'completed'

    async def __wait_till_action_complete(self, action_id: int) -> str:
        action_status = self.__check_action_status(action_id)

        while action_status == 'in-progress':
            await asyncio.sleep(5)
            action_status = self.__check_action_status(action_id)

        if action_status == 'errored':
            raise DropletCreationError

        return action_status

    def __check_action_status(self, action_id: int) -> str:
        """Checks digital ocean action status

        Args:
            action_id (int): Digital Ocean action id

        Returns:
            str: action status (`in-progress`, `completed`, `errored`)
        """
        print('Entered __check_action_status')

        response = self.requests.get(
            self.__base_url + '/actions/' + str(action_id)
        )
        print(response.json())

        return response.json()['action']['status']
