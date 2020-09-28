from pydoautomator.droplet import Droplet
from pydoautomator.adapters import ApiAdapter
import asyncio
from pydoautomator.errors import DropletCreationError


class Automator:
    do_token = ''
    requests = ''
    __base_url = 'https://api.digitalocean.com/v2'

    def __init__(self, do_token: str):
        self.do_token = do_token
        self.api_adapter = ApiAdapter(self.do_token)
        self.requests = self.api_adapter.requests
        self.__base_url = 'https://api.digitalocean.com/v2'

    def create_droplet_from_snapshot(self, droplet: Droplet) -> int:
        """creates droplet from snapshot

        :param droplet: Droplet object to be created on DO
        :type droplet: Droplet
        :param snapshot_id: snapshot ID
        :type snapshot_id: int
        :return: created droplet ID
        :rtype: int
        """

        created_droplet = self.requests.post(
            self.__base_url + '/droplets', data=droplet.json())

        print(created_droplet.json())

        action_id = created_droplet.json()['links']['actions'][0]['id']
        loop = asyncio.get_event_loop()

        loop.run_until_complete(
            self.__wait_till_action_complete(action_id)
        )

        return created_droplet.json()['droplet']['id']

    async def __wait_till_action_complete(self, action_id: int) -> str:
        print('Entered  __wait_till_action_complete')
        action_status = self.__check_action_status(action_id)

        while action_status == 'in-progress':
            await asyncio.sleep(5)
            action_status = self.__check_action_status(action_id)
            print(action_status)

        if action_status == 'errored':
            raise DropletCreationError

        return action_status

    def __check_action_status(self, action_id: int) -> str:
        """Check action status

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
