from unittest import TestCase
import pydoautomator
from pydoautomator.droplet import Droplet
from pydantic import BaseModel


class TestDropletClass(TestCase):

    def test_if_droplet_submodule_exists(self):
        try:
            import pydoautomator.droplet as droplet
        except ModuleNotFoundError:
            self.fail('submodule does not exist!')

    def test_if_droplet_class_exists(self):
        import pydoautomator.droplet as droplet
        self.assertTrue(hasattr(droplet, 'Droplet'),
                        'Droplet does not exists in droplet')

    def test_if_droplet_is_pydantic_base_model_subclass(self):
        self.assertTrue(issubclass(Droplet, BaseModel),
                        'Droplet is not a subclass from BaseModel')

    def test_if_model_has_id(self):
        self.assertIn(
            'id',
            Droplet.schema()['properties']
        )

    def test_if_id_is_int(self):
        self.assertIs(
            Droplet.schema()['properties']['id']['type'],
            'integer'
        )

    def test_if_id_is_required(self):
        self.assertIn(
            'id',
            Droplet.__annotations__,
            'id is NOT required!'
        )

    def test_if_model_has_name(self):
        self.assertIn(
            'name',
            Droplet.schema()['properties']
        )

    def test_if_name_is_string(self):
        self.assertIs(
            Droplet.schema()['properties']['name']['type'],
            'string'
        )

    def test_if_name_is_required(self):
        self.assertIn(
            'name',
            Droplet.__annotations__,
            'name is NOT required!'
        )

    def test_if_model_has_region(self):
        self.assertIn(
            'region',
            Droplet.schema()['properties']
        )

    def test_if_region_is_string(self):
        self.assertIs(
            Droplet.schema()['properties']['region']['type'],
            'string'
        )

    def test_if_region_is_required(self):
        self.assertIn(
            'region',
            Droplet.__annotations__,
            'region is NOT required!'
        )

    def test_if_model_has_size(self):
        self.assertIn(
            'size',
            Droplet.schema()['properties']
        )

    def test_if_size_is_string(self):
        self.assertIs(
            Droplet.schema()['properties']['size']['type'],
            'string'
        )

    def test_if_size_is_required(self):
        self.assertIn(
            'size',
            Droplet.__annotations__,
            'size is NOT required!'
        )

    def test_if_model_has_image(self):
        self.assertIn(
            'image',
            Droplet.schema()['properties']
        )

    def test_if_image_is_int(self):
        self.assertIs(
            Droplet.schema()['properties']['image']['type'],
            'integer'
        )

    def test_if_image_is_required(self):
        self.assertIn(
            'image',
            Droplet.__annotations__,
            'image is NOT required!'
        )

    def test_if_model_has_ssh_keys(self):
        self.assertIn(
            'ssh_keys',
            Droplet.schema()['properties']
        )

    def test_if_ssh_keys_is_list(self):
        self.assertIs(
            Droplet.schema()['properties']['ssh_keys']['type'],
            'array'
        )

    def test_if_model_has_private_networking(self):
        self.assertIn(
            'private_networking',
            Droplet.schema()['properties']
        )

    def test_if_private_networking_is_bool(self):
        self.assertIs(
            Droplet.schema()['properties']['private_networking']['type'],
            'boolean'
        )

    def test_if_model_has_vpc_uuid(self):
        self.assertIn(
            'vpc_uuid',
            Droplet.schema()['properties']
        )

    def test_if_vpc_uuid_is_string(self):
        self.assertIs(
            Droplet.schema()['properties']['vpc_uuid']['type'],
            'string'
        )

    def test_if_model_has_monitoring(self):
        self.assertIn(
            'monitoring',
            Droplet.schema()['properties']
        )

    def test_if_monitoring_is_bool(self):
        self.assertIs(
            Droplet.schema()['properties']['monitoring']['type'],
            'boolean'
        )

    def test_object_creation(self):
        try:
            droplet = Droplet(**{
                "name": "t1.techno24x7.com",
                "region": "nyc1",
                "size": "s-8vcpu-16gb",
                "image": 68259296,
                "ssh_keys": [27410347, 27608055, 27590881],
                "private_networking": True,
                "vpc_uuid": "47e5c00a-2b23-4dac-bed4-0e44659941f3",
                "monitoring": True
            })
        except:
            self.fail('Droplet object couldnt be created!')
