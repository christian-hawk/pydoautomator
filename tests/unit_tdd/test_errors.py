import pytest
from pydoautomator import errors
import inspect
from pydoautomator.errors import DropletCreationError, FloatingIpAssignmentError


def test_if_submodule_automator_exists():
    try:
        import pydoautomator.errors as errors
    except ModuleNotFoundError:
        pytest.fail('submodule errors does NOT exist')


def test_droplet_creation_error_should_exist():
    assert hasattr(errors, 'DropletCreationError')


def test_droplet_creation_error_should_be_a_class():
    assert inspect.isclass(errors.DropletCreationError)


def test_droplet_creation_error_should_be_exception_subclass():
    assert issubclass(errors.DropletCreationError, Exception)


def test_droplet_creation_error_should_have_msg():
    expected_msg = 'Digital Ocean API returned errored'
    with pytest.raises(DropletCreationError, match=expected_msg):
        raise DropletCreationError


def test_floating_ip_assignment_error_should_exist():
    assert hasattr(errors, 'FloatingIpAssignmentError')


def test_floating_ip_assignment_error_should_be_a_class():
    assert inspect.isclass(errors.FloatingIpAssignmentError)


def test_floating_ip_assignment_error_should_be_exception_subclass():
    assert issubclass(errors.FloatingIpAssignmentError, Exception)


def test_floating_ip_assignment_error_should_have_msg():
    msg = {'error': 'yeah right'}
    expected_msg = 'Error on assigning floating ip. Response data is: ' + \
        str(msg)

    with pytest.raises(FloatingIpAssignmentError, match=expected_msg):
        raise FloatingIpAssignmentError(msg)
