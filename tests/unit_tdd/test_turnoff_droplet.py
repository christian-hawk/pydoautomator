from pydoautomator import Automator
import inspect
import responses
import requests
from tests.unit_tdd.api_mocks import shutdown_droplet_success_response, error_404_response
from unittest.mock import MagicMock
import pytest
from pydoautomator.errors import TurnoffDropletError


def test_turnoff_droplet_should_exist():
    assert hasattr(Automator, 'turnoff_droplet')


def test_turnoff_droplet_should_be_a_function():
    assert inspect.isfunction(
        Automator.turnoff_droplet), 'turnoff_project is not a function'


def test_turnoff_droplet_should_receive_self_and_droplet_id():
    expected_args = {'self', 'droplet_id'}
    arguments = inspect.getfullargspec(Automator.turnoff_droplet).args

    assert set(arguments) <= expected_args <= set(arguments)


def test_should_have_expected_annotations():
    expected_annotations = {
        'return': str,
        'droplet_id': int,
    }
    annotations = inspect.getfullargspec(Automator.turnoff_droplet).annotations
    assert set(expected_annotations) <= set(annotations)


@responses.activate
def test_assert_requests_post_is_called_once():
    token = 'my-test-token-123'
    aut = Automator(token)
    stashed = aut.requests.post
    droplet_id = 212611563

    full_url = 'https://api.digitalocean.com/v2/droplets/%s/actions' % droplet_id

    data = {
        "type": "shutdown"
    }
    json_headers = {'Content-Type': 'application/json'}

    # mock response w/ success status
    responses.reset()
    shutdown_droplet_success_response(droplet_id)
    mocked_response = requests.post(full_url)

    stashed = aut._Automator__check_action_status
    stashed2 = aut.requests.post
    aut._Automator__check_action_status = MagicMock(
        return_value='completed')
    aut.requests.post = MagicMock(return_value=mocked_response)

    aut.turnoff_droplet(droplet_id)

    aut.requests.post.assert_called_once_with(
        full_url, json=data, headers=json_headers)

    aut._Automator__check_action_status.assert_called_once_with(
        mocked_response.json()['action']['id'])

    aut._Automator__check_action_status = stashed
    aut.requests.post = stashed2


@responses.activate
def test_if_response_status_201_return_completed():
    token = 'my-test-token-123'
    aut = Automator(token)
    droplet_id = 212611563
    # response mock w/ 201 response
    shutdown_droplet_success_response(droplet_id)

    stashed = aut._Automator__check_action_status

    aut._Automator__check_action_status = MagicMock(
        return_value='completed')

    result = aut.turnoff_droplet(droplet_id)
    assert result == 'completed'
    aut._Automator__check_action_status = stashed


@responses.activate
def test_if_response_not_201_raise_error():
    token = 'my-test-token-123'
    aut = Automator(token)
    droplet_id = 212611563

    full_url = 'https://api.digitalocean.com/v2/droplets/%s/actions' % droplet_id

    responses.reset()
    error_404_response(full_url)

    with pytest.raises(TurnoffDropletError):
        aut.turnoff_droplet(droplet_id)

    responses.reset()
