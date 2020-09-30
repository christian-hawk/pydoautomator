# pydoautomator

[![codecov](https://codecov.io/gh/christian-hawk/pydoautomator/branch/master/graph/badge.svg)](https://codecov.io/gh/christian-hawk/pydoautomator)

The Digital Ocean python automation lib

Alpha

## Simple as that

``` python
from pydoautomator import Automator, Droplet
digital_ocean_token = 'my-digital-ocean-api-token'

aut = Automator(digital_ocean_token)

droplet_data = {
    "name" : "t1.techno24x7.com",
    "region" : "nyc1",
    "size" : "s-8vcpu-16gb",
    "image" : 68259296, # snapshot id
    "ssh_keys" : [27410347, 27608055, 27590881],
    "private_networking" : True,
    "vpc_uuid" : "47e5c00a-2b23-4dac-bed4-0e44659941f3",
    "monitoring" : True
}

droplet = Droplet(**droplet_data)

aut.create_droplet_from_snapshot(droplet)

```

### Assign floating ip to droplet

```python
droplet_id = 152412424
floating_ip = '164.90.252.72'
action_status = aut.assign_floating_ip_to_droplet(floating_ip, droplet_id)

if action_status == 'completed':
    print('floating_ip assigned to droplet!')
```

### Create droplet and assign floating ip as soon as droplet created

```python
igital_ocean_token = 'my-super-cool-digital-ocean-api-token'

aut = Automator(digital_ocean_token)

droplet_data = {
    "name": "t1.techno24x7.com",
    "region": "nyc1",
    "size": "s-8vcpu-16gb",
    "image": 70649304, # snapshot id
    "ssh_keys": [27410347, 27608055, 27590881],
    "private_networking": True,
    "vpc_uuid": "47e5c00a-2b23-4dac-bed4-0e44659941f3",
    "monitoring": True
}

droplet = Droplet(**droplet_data)

droplet_id = aut.create_droplet_from_snapshot(droplet)


floating_ip = '164.90.252.72'
action_status = aut.assign_floating_ip_to_droplet(floating_ip, droplet_id)

if action_status == 'completed':
    print('floating_ip assigned to droplet!')
```
