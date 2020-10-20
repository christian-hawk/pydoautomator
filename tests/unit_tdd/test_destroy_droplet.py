from pydoautomator import Automator
import inspect
import responses
import requests
from tests.unit_tdd.api_mocks import error_404_response, destroy_droplet_success_response
from unittest.mock import MagicMock
import pytest
from pydoautomator.errors import DestroyDropletError


def test_destroy_droplet_should_exist():
    assert hasattr(Automator, 'destroy_droplet')


def test_destroy_droplet_should_be_a_function():
    assert inspect.isfunction(
        Automator.destroy_droplet), 'destroy_droplet is not a function'


def test_destroy_droplet_should_receive_self_and_droplet_id():
    expected_args = {'self', 'droplet_id'}
    arguments = inspect.getfullargspec(Automator.destroy_droplet).args

    assert set(arguments) <= expected_args <= set(arguments)


def test_should_have_expected_annotations():
    expected_annotations = {
        'return': str,
        'droplet_id': int,
    }
    annotations = inspect.getfullargspec(Automator.destroy_droplet).annotations
    assert set(expected_annotations) <= set(annotations)


@responses.activate
def test_assert_requests_delete_is_called_once_with_args():
    token = 'my-test-token-123'
    aut = Automator(token)
    droplet_id = 212611563

    full_url = 'https://api.digitalocean.com/v2/droplets/%s' % droplet_id

    # stash to mock
    stashed2 = aut.requests.delete

    # mocks
    responses.reset()
    destroy_droplet_success_response(droplet_id)
    mocked_response = requests.delete(full_url)
    aut.requests.delete = MagicMock(return_value=mocked_response)

    # test
    aut.destroy_droplet(droplet_id)
    aut.requests.delete.assert_called_once_with(full_url)

    # pop stashed
    aut.requests.delete = stashed2


@responses.activate
def test_if_response_status_204_return_completed():
    token = 'my-test-token-123'
    aut = Automator(token)
    droplet_id = 212611563

    # response mock w/ 204 response
    responses.reset()
    destroy_droplet_success_response(droplet_id)

    result = aut.destroy_droplet(droplet_id)
    assert result == 'completed'


@responses.activate
def test_if_response_not_204_raise_error():
    token = 'my-test-token-123'
    aut = Automator(token)
    droplet_id = 212611563

    full_url = 'https://api.digitalocean.com/v2/droplets/%s' % droplet_id

    responses.reset()
    error_404_response(full_url)

    with pytest.raises(DestroyDropletError):
        aut.destroy_droplet(droplet_id)


# def test_destroy_droplet_should_have_docstring():
#     assert inspect.getdoc(Automator.destroy_droplet) is not None
