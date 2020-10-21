from unittest import TestCase
from unittest.mock import MagicMock
import inspect
from pydoautomator.automator import Automator
import pydoautomator
from pydoautomator.droplet import Droplet
from . import helper
import responses
import asyncio
import pytest
from asyncio.futures import Future
from pydoautomator.errors import DropletCreationError


droplet_instance = Droplet(**helper.valid_droplet)


def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()

# using pytest here for async


@pytest.mark.asyncio
async def test_async_mock():
    token = 'my-test-token-234'
    action_id = 1030573508
    aut = Automator(token)
    # stash
    check = aut._Automator__check_action_status

    aut._Automator__check_action_status = MagicMock(return_value=Future())
    aut._Automator__check_action_status.return_value.set_result(
        'in-progress')
    result = await aut._Automator__check_action_status(action_id)
    assert result == 'in-progress'

    # restore
    aut._Automator__check_action_status = check


@pytest.mark.asyncio
async def test_wait_till_complete_should_call_check_action_status_each_5_secs():
    token = 'my-test-token-234'
    action_id = 1030573508
    aut = Automator(token)

    # stash
    check = aut._Automator__check_action_status

    aut._Automator__check_action_status = MagicMock(return_value=Future())
    aut._Automator__check_action_status.return_value.set_result('in-progress')
    try:
        await asyncio.wait_for(aut._Automator__wait_till_action_complete(action_id), timeout=14.0)
    except asyncio.TimeoutError:
        # timeout reached
        # should call 3 times in 14 sec (0s, 5s, 10s)
        assert aut._Automator__check_action_status.call_count == 3
    finally:
        # restore from stash
        aut._Automator__check_action_status = check


@pytest.mark.asyncio
async def test_wait_till_complete_should_return_complete():
    token = 'my-test-token-234'
    action_id = 1030573508
    aut = Automator(token)

    # stash
    check = aut._Automator__check_action_status

    aut._Automator__check_action_status = MagicMock(return_value='completed')

    result = await aut._Automator__wait_till_action_complete(action_id)
    assert result == 'completed'

    # restore
    aut._Automator__check_action_status = check


@responses.activate
def test_check_action_status_should_return_created_droplet_id():
    token = 'my-test-token-234'
    action_id = 1030573508
    action_url = 'https://api.digitalocean.com/v2/actions/' + str(action_id)
    droplet_url = 'https://api.digitalocean.com/v2/droplets'
    aut = Automator(token)
    # mock action response
    responses.add(responses.GET, action_url,
                  json=helper.valid_creation_completed_response, status=200)
    # mock droplet response
    responses.add(responses.POST, droplet_url,
                  json=helper.valid_droplet_created_response, status=200)

    expected_droplet_id = helper.valid_droplet_created_response['droplet']['id']
    result = aut.create_droplet_from_snapshot(droplet_instance)

    assert result == expected_droplet_id


@pytest.mark.asyncio
async def test_wait_till_complete_should_raise_error():
    token = 'my-test-token-234'
    action_id = 1030573508
    aut = Automator(token)

    # stash
    check = aut._Automator__check_action_status

    with pytest.raises(DropletCreationError):

        aut._Automator__check_action_status = MagicMock(return_value='errored')

        await aut._Automator__wait_till_action_complete(action_id)

    aut._Automator__check_action_status = check


class TestAutomator(TestCase):

    def test_if_submodule_automator_exists(self):
        try:
            import pydoautomator.automator as automator
        except:
            self.fail('submodule automator does NOT exist')

    def test_if_Automator_exists(self):
        import pydoautomator.automator as automator
        self.assertTrue(hasattr(automator, 'Automator'),
                        'Automator does not exists in automator')

    def test_Automator_should_be_a_class(self):
        from pydoautomator.automator import Automator
        self.assertTrue(
            inspect.isclass(Automator),
            'Automator is NOT a class!'
        )

    def test_automator_should_have_create_droplet_from_snapshot(self):
        self.assertTrue(
            hasattr(Automator, 'create_droplet_from_snapshot'),
            'create_droplet_from_snapshot does not exist in Automator'
        )

    def test_create_droplet_from_snapshot_should_be_a_method(self):
        self.assertTrue(
            inspect.isfunction(Automator.create_droplet_from_snapshot),
            'create_droplet_from_snapshot is NOT a function!'
        )

    def test_if_Droplet_exists_in_package(self):
        self.assertTrue(
            hasattr(pydoautomator.automator, 'Droplet'),
            'Droplet does not exists in package'
        )

    def test_Droplet_should_be_not_none(self):
        self.assertIsNotNone(
            pydoautomator.automator.Droplet,
            'Droplet has None value!'
        )

    def test_if_Droplet_is_a_class(self):
        self.assertTrue(
            inspect.isclass(pydoautomator.automator.Droplet),
            'pydoautomator.automator.Droplet is not a class'
        )

    def test_if_Droplet_is_from_droplet_submodule(self):
        self.assertTrue(
            pydoautomator.automator.Droplet.__module__ == 'pydoautomator.droplet',
            'pydoautomator.Droplet is NOT a module from pydoautomator.droplet'
        )

    def test_create_droplet_from_snapshot_should_receive_args(self):
        expected_args = {'self', 'droplet'}
        current_args = set(inspect.getfullargspec(
            Automator.create_droplet_from_snapshot).args)

        self.assertTrue(
            expected_args <= current_args <= expected_args,
            'create_droplet_from_snapshot does NOT have expected arguments'
        )

    def test_if_droplet_arg_has_coorect_annotation(self):
        annotations = inspect.getfullargspec(
            Automator.create_droplet_from_snapshot).annotations
        self.assertIs(
            annotations['droplet'],
            pydoautomator.droplet.Droplet
        )

    def test_if_Automator_has_requests(self):
        self.assertTrue(
            hasattr(pydoautomator.automator.Automator, 'requests'),
            'automator does not have requests'
        )

    def test_automator_should_have_do_token(self):
        self.assertTrue(
            hasattr(Automator, 'do_token'),
            'Automator does NOT have do_token attr'
        )

    def test_automator_instance_should_have_do_token_value(self):
        token = 'my-test-token-234'
        aut = Automator(token)
        self.assertEqual(
            token,
            aut.do_token
        )

    def test_automator_should_have_ApiAdapter(self):
        self.assertTrue(
            hasattr(pydoautomator.automator, 'ApiAdapter'),
            'Automator does NOt have ApiAdapter attr'
        )

    def test_ApiAdapter_should_be_adapters_class(self):
        self.assertIs(
            pydoautomator.automator.ApiAdapter,
            pydoautomator.adapters.ApiAdapter
        )

    def test_Automator_instance_should_have_api_adapter(self):
        token = 'my-test-token-234'
        aut = Automator(token)
        self.assertTrue(
            hasattr(aut, 'api_adapter')
        )

    def test_api_adapter_should_be_ApiAdapter_instance(self):
        token = 'my-test-token-234'
        aut = Automator(token)
        self.assertIsInstance(
            aut.api_adapter,
            pydoautomator.adapters.ApiAdapter
        )

    def test_if_requests_is_session_instance(self):
        import requests
        token = 'my-test-token-234'
        aut = Automator(token)
        self.assertIsInstance(
            aut.requests,
            requests.sessions.Session
        )

    @responses.activate
    def test_create_droplet_from_snapshot_should_call_post_once(self):
        token = 'my-test-token-234'
        action_id = 1030573508
        aut = Automator(token)
        self.post = aut.requests.post
        action_url = 'https://api.digitalocean.com/v2/actions/' + \
            str(action_id)
        droplet_url = 'https://api.digitalocean.com/v2/droplets'
        aut = Automator(token)
        aut._Automator__check_action_status = MagicMock(
            return_value='completed')
        # mock action response
        responses.add(responses.GET, action_url,
                      json=helper.valid_creation_completed_response, status=200)
        # mock droplet response
        responses.add(responses.POST, droplet_url,
                      json=helper.valid_droplet_created_response, status=200)

        stashed = aut.requests.post

        aut.requests.post = MagicMock()

        aut.create_droplet_from_snapshot(droplet_instance)

        aut.requests.post.assert_called_once()
        aut.requests.posts = self.post

        aut.requests.post = stashed

    def test_create_droplet_from_snapshot_should_call_post_with_args(self):
        token = 'my-test-token-234'
        url = 'https://api.digitalocean.com/v2/droplets'
        aut = Automator(token)
        aut._Automator__check_action_status = MagicMock(
            return_value='completed')

        stashed = aut.requests.post
        aut.requests.post = MagicMock()
        aut.create_droplet_from_snapshot(droplet_instance)
        aut.requests.post.assert_called_once_with(
            url, data=droplet_instance.json(),
            headers={'Content-Type': 'application/json'})

        aut.requests.post = stashed

    def test_check_action_status_should_exist(self):
        self.assertTrue(
            hasattr(Automator, '_Automator__check_action_status'),
            'Automator does not have _Automator__check_action_status attr'
        )

    def test_check_action_status_should_be_function(self):
        self.assertTrue(
            inspect.isfunction(
                Automator._Automator__check_action_status),
            '__check_action_status is NOT a function'
        )

    def test_check_action_status_should_receive_action_id(self):
        args = inspect.getfullargspec(
            Automator._Automator__check_action_status).args
        self.assertIn(
            'action_id',
            args
        )

    def test_check_action_status_should_call_get_once_with_args(self):
        token = 'my-test-token-234'
        action_id = 1030573508
        url = 'https://api.digitalocean.com/v2/actions/' + str(action_id)
        aut = Automator(token)
        self.get = aut.requests.get
        aut.requests.get = MagicMock()
        aut._Automator__check_action_status(action_id)
        aut.requests.get.assert_called_once_with(url)
        aut.requests.get = self.get

    @responses.activate
    def test_check_action_status_should_return_status(self):

        token = 'my-test-token-234'
        action_id = 1030573508
        url = 'https://api.digitalocean.com/v2/actions/' + str(action_id)

        # mock response
        responses.add(responses.GET, url,
                      json=helper.valid_creation_in_progress_response, status=200)
        aut = Automator(token)

        self.assertEqual(
            aut._Automator__check_action_status(action_id),
            'in-progress'
        )

    def test_wait_till_action_complete_should_exist(self):
        self.assertTrue(
            hasattr(Automator, '_Automator__wait_till_action_complete'),
            'Automator does not have __wait_till_action_complete attr'
        )

    def test_wait_till_action_complete_should_be_a_function(self):
        self.assertTrue(
            inspect.isfunction(
                Automator._Automator__wait_till_action_complete),
            '__wait_till_action_complete is NOT a function!'
        )

    def test_wait_till_action_complete_should_receive_action_id(self):
        args = inspect.getfullargspec(
            Automator._Automator__wait_till_action_complete).args
        self.assertIn(
            'action_id',
            args
        )

    def test_wait_till_action_complete_action_id_should_have_int_annot(self):
        annotations = inspect.getfullargspec(
            Automator._Automator__wait_till_action_complete).annotations
        self.assertIs(
            annotations['action_id'],
            int
        )

    async def test_check_action_status_should_be_called_with_action_id(self):
        """
        Test: When calling __wailt_till_action_complete,
        __check_action_status should be called
        """
        token = 'my-test-token-234'
        action_id = 1030573508

        aut = Automator(token)
        # stash
        self.check = aut._Automator__check_action_status
        aut._Automator__check_action_status = MagicMock(
            name='__check_action_status')
        await aut._Automator__wait_till_action_complete(action_id)
        aut._Automator__check_action_status.assert_called_with(action_id)

        # restore stashed
        aut._Automator__check_action_status = self.check

    def test_create_droplet_request_should_have_json_headers(self):
        expected_args = {
            'data': '{"id": null, "name": "t1.techno24x7.com", "region": "nyc1", "size": "s-8vcpu-16gb", "image": 68259296, "ssh_keys": [27410347, 27608055, 27590881], "private_networking": true, "vpc_uuid": "47e5c00a-2b23-4dac-bed4-0e44659941f3", "monitoring": true, "tags": []}',
            'headers': {
                'Content-Type': 'application/json'
            }}
        token = 'my-test-token-234'
        aut = Automator(token)

        # mock complete action response
        aut._Automator__check_action_status = MagicMock(
            return_value='complete')
        # mock post
        stashed = aut.requests.post
        aut.requests.post = MagicMock()

        aut.create_droplet_from_snapshot(droplet_instance)

        self.assertIn(
            expected_args,
            aut.requests.post.call_args
        )
        aut.requests.post = stashed
