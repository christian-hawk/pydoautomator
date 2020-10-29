from pydoautomator import Automator
import inspect
from unittest.mock import MagicMock
from .api_mocks import list_droplets_response
import requests
import responses
from .helper import get_json_from_file


class TestGetAllDroplets():
    def get_responses(self):
        three_responses = [
            requests.get('https://api.digitalocean.com/v2/droplets'),
            requests.get(
                'https://api.digitalocean.com/v2/droplets?page=2&per_page=20'),
            requests.get(
                'https://api.digitalocean.com/v2/droplets?page=3&per_page=20')
        ]
        return three_responses

    def test_get_all_droplets_exists(self):
        assert hasattr(Automator, 'get_all_droplets')

    def test_get_all_droplets_should_be_function(self):
        assert inspect.isfunction(Automator.get_all_droplets)

    def test_get_all_droplets_call_requests_get_once(self):
        aut = Automator('whatever-test-token')
        stashed = aut.requests.get
        aut.requests.get = MagicMock()
        aut.get_all_droplets()
        aut.requests.get.assert_called_once()
        aut.requests.get = stashed

    def test_get_all_droplets_call_requests_w_args(self):
        aut = Automator('whatever-test-token')
        stashed = aut.requests.get
        aut.requests.get = MagicMock()
        aut.get_all_droplets()
        aut.requests.get.assert_called_once_with(
            'https://api.digitalocean.com/v2/droplets')
        aut.requests.get = stashed

    @responses.activate
    def test_get_all_droplets_should_return_list(self):
        aut = Automator('whatever-test-token')
        list_droplets_response()
        stashed = aut.requests.get
        aut.requests.get = MagicMock()
        aut.requests.get.side_effect = self.get_responses()
        assert type(aut.get_all_droplets()) is list
        aut.requests.get = stashed

    @responses.activate
    def test_get_all_droplets_item_should_contain_keys(self):
        some_expected_keys = ['id', 'name', 'region']
        aut = Automator('whatever-test-token')
        list_droplets_response()
        stashed = aut.requests.get
        aut.requests.get = MagicMock()
        aut.requests.get.side_effect = self.get_responses()
        assert set(some_expected_keys) <= set(aut.get_all_droplets()[0])
        aut.requests.get = stashed

    @responses.activate
    def test_sum_all_droplets_should_be_the_same_as_meta(self):
        # test failing cauz of responses bug: https://github.com/getsentry/responses/issues/352
        # responses.reset()
        # aut = Automator('whatever-test-token')
        # meta_total = get_json_from_file(
        #     'list_droplets_page_1.json')['meta']['total']
        # list_droplets_response()
        # assert len(aut.get_all_droplets()) == meta_total

        # rewriting temporary:
        aut = Automator('whatever-test-token')
        meta_total = get_json_from_file(
            'list_droplets_page_1.json')['meta']['total']

        # mocks
        list_droplets_response()
        stashed = aut.requests.get
        aut.requests.get = MagicMock()
        aut.requests.get.side_effect = self.get_responses()

        assert len(aut.get_all_droplets()) == meta_total

        aut.requests.get = stashed
        # @TODO restore commented test after issue resolved

    @responses.activate
    def test_request_get_should_be_called_3_times(self):
        responses.reset()
        aut = Automator('whatever-test-token')

        # mocks
        list_droplets_response()
        stashed = aut.requests.get
        aut.requests.get = MagicMock()
        aut.requests.get.side_effect = self.get_responses()

        aut.get_all_droplets()

        assert aut.requests.get.call_count == 3
        aut.requests.get = stashed
