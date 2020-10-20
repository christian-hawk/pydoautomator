from pydoautomator.droplet import Droplet
from pydoautomator.adapters import ApiAdapter
import asyncio
from pydoautomator.errors import DropletCreationError, FloatingIpAssignmentError, TurnoffDropletError, DestroyDropletError


class Automator:
    do_token = ''
    requests = ''
    __base_url = 'https://api.digitalocean.com/v2'

    def __init__(self, do_token: str):
        self.do_token = do_token
        self.api_adapter = ApiAdapter(self.do_token)
        self.requests = self.api_adapter.requests
        self.__base_url = 'https://api.digitalocean.com/v2'

    def turnoff_droplet(self, droplet_id: int) -> str:
        """[summary]

        :param droplet_id: droplet id
        :type droplet_id: int
        :raises TurnoffDropletError: when no success on request
        :return: 'completed' if completed
        :rtype: str
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
        response = self.requests.get(self.__base_url+'/droplets')
        return response.json()['droplets']

    def assign_floating_ip_to_droplet(self, floating_ip: str, droplet_id: int) -> str:
        """Assigns a floating_ip to a droplet

        :param floating_ip: floating ip
        :type floating_ip: str
        :param droplet_id: droplet id
        :type droplet_id: int
        :return: droplet id that received the new floating ip
        :rtype: str
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
        """creates droplet from snapshot

        :param droplet: Droplet object to be created on DO
        :type droplet: Droplet
        :param snapshot_id: snapshot ID
        :type snapshot_id: int
        :return: created droplet ID
        :rtype: int
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
        """
        Check action status

        :param action_id: action ID
        :type action_id: int
        :return: action status (in-progress, completed, errored)
        :rtype: str
        """
        print('Entered __check_action_status')

        response = self.requests.get(
            self.__base_url + '/actions/' + str(action_id)
        )
        print(response.json())

        return response.json()['action']['status']
