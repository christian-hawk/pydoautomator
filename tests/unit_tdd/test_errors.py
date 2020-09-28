import pytest
from pydoautomator import errors
import inspect
from pydoautomator.errors import DropletCreationError


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
