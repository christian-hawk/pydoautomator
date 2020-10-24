from pydoautomator import Automator
import inspect
from unittest.mock import MagicMock
from .api_mocks import list_droplets_response
import requests
import responses


class TestGetAllDroplets():
    def test_get_all_droplets_exists(self):
        assert hasattr(Automator, 'get_all_droplets')

    def test_get_all_droplets_should_be_function(self):
        assert inspect.isfunction(Automator.get_all_droplets)

    def test_get_all_droplets_call_requests_get_once(self):
        aut = Automator('whatever-test-token')
        aut.requests.get = MagicMock()
        aut.get_all_droplets()
        aut.requests.get.assert_called_once()

    def test_get_all_droplets_call_requests_w_args(self):
        aut = Automator('whatever-test-token')
        aut.requests.get = MagicMock()
        aut.get_all_droplets()
        aut.requests.get.assert_called_once_with(
            'https://api.digitalocean.com/v2/droplets')

    @responses.activate
    def test_get_all_droplets_should_return_list(self):
        aut = Automator('whatever-test-token')
        list_droplets_response()
        response = requests.get('https://api.digitalocean.com/v2/droplets')
        aut.requests.get = MagicMock(return_value=response)
        assert type(aut.get_all_droplets()) is list

    @responses.activate
    def test_get_all_droplets_item_should_contain_keys(self):
        some_expected_keys = ['id', 'name', 'region']
        aut = Automator('whatever-test-token')
        list_droplets_response()
        response = requests.get('https://api.digitalocean.com/v2/droplets')
        aut.requests.get = MagicMock(return_value=response)
        assert set(some_expected_keys) <= set(aut.get_all_droplets()[0])
