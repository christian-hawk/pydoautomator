# pytest
from pydoautomator import Automator
import inspect
from unittest.mock import MagicMock
from .api_mocks import assign_floating_ip_success_response, error_404_response
import pytest
import responses
from pydoautomator.errors import FloatingIpAssignmentError
import requests


def test_assign_floating_ip_to_dropletshould_exist():
    assert hasattr(Automator, 'assign_floating_ip_to_droplet')


def test_assign_floating_ip_should_not_be_none():
    assert Automator.assign_floating_ip_to_droplet is not None


def test_assign_floating_ip_is_function():
    assert inspect.isfunction(Automator.assign_floating_ip_to_droplet)


def test_assign_floating_ip_should_receive_expected_args():
    args = inspect.getfullargspec(Automator.assign_floating_ip_to_droplet).args
    expected_args = ['self', 'floating_ip', 'droplet_id']
    assert set(expected_args) <= set(args) <= set(expected_args)


def test_assign_floating_ip_floating_ip_should_have_annotations():
    annotations = inspect.getfullargspec(
        Automator.assign_floating_ip_to_droplet).annotations
    assert bool(annotations)


def test_assign_floating_ip_floating_ip_should_have_str_annotation():
    annotations = inspect.getfullargspec(
        Automator.assign_floating_ip_to_droplet).annotations
    assert annotations['floating_ip'] is str


def test_assign_floating_ip_droplet_id_should_have_str_annotations():
    annotations = inspect.getfullargspec(
        Automator.assign_floating_ip_to_droplet).annotations
    assert annotations['droplet_id'] is int


def test_assert_docstring_exists_in_assign_floating_ip():
    assert inspect.getdoc(Automator.assign_floating_ip_to_droplet) is not None


@responses.activate
def test_assert_requests_post_is_called_once():
    token = 'my-test-token-123'
    aut = Automator(token)
    stashed = aut.requests.post
    floating_ip = '124.52.234.6'
    droplet_id = 42312552

    full_url = 'https://api.digitalocean.com/v2/floating_ips/%s/actions' % floating_ip

    # mock response w/ success status
    responses.reset()
    assign_floating_ip_success_response(floating_ip, droplet_id)
    mocked_response = requests.post(full_url)

    stashed = aut._Automator__check_action_status
    stashed2 = aut.requests.post
    aut._Automator__check_action_status = MagicMock(
        return_value='completed')
    aut.requests.post = MagicMock(return_value=mocked_response)
    aut.assign_floating_ip_to_droplet(floating_ip, droplet_id)

    aut.requests.post.assert_called_once()

    aut._Automator__check_action_status = stashed
    aut.requests.post = stashed2


@responses.activate
def test_assert_request_post_is_called_with_args():
    floating_ip = '124.52.234.6'
    droplet_id = 42312552

    full_url = 'https://api.digitalocean.com/v2/floating_ips/%s/actions' % floating_ip
    data = {
        "type": "assign",
        "droplet_id": 8219222
    }
    json_headers = {'Content-Type': 'application/json'}

    token = 'my-test-token-123'
    aut = Automator(token)

    stashed = aut.requests.post
    stashed2 = aut._Automator__check_action_status

    # mock response w/ success status
    responses.reset()
    assign_floating_ip_success_response(floating_ip, droplet_id)
    mocked_response = requests.post(full_url)

    aut._Automator__check_action_status = MagicMock(
        return_value='completed')
    aut.requests.post = MagicMock(return_value=mocked_response)

    aut.assign_floating_ip_to_droplet('124.52.234.6', 8219222)

    aut.requests.post.assert_called_once_with(
        full_url, json=data, headers=json_headers)

    aut.requests.post = stashed
    aut._Automator__check_action_status = stashed2


@responses.activate
def test_if_response_status_201_return_completed():
    token = 'my-test-token-123'
    aut = Automator(token)
    floating_ip = '135.155.152.2'
    droplet_id = 42143152
    # response mock w/ 201 response
    assign_floating_ip_success_response(floating_ip, droplet_id)

    stashed = aut._Automator__check_action_status
    aut._Automator__check_action_status = MagicMock(
        return_value='completed')

    result = aut.assign_floating_ip_to_droplet(floating_ip, droplet_id)
    assert result == 'completed'


@responses.activate
def test_if_response_not_201_raise_error():
    token = 'my-test-token-123'
    aut = Automator(token)
    floating_ip = '135.155.152.2'
    droplet_id = 42143152
    url = 'https://api.digitalocean.com/v2/floating_ips/%s/actions' % floating_ip

    responses.reset()
    error_404_response(url)

    with pytest.raises(FloatingIpAssignmentError):
        aut.assign_floating_ip_to_droplet(floating_ip, droplet_id)
        responses.reset()
