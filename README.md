# pydoautomator
The Digital Ocean python automation lib

Alpha

``` python
from pydoautomator import Automator, Droplet
digital_ocean_token = 'my-digital-ocean-api-token'

aut = Automator(digital_ocean_token)

droplet_data = {
    "name" : "t1.techno24x7.com",
    "region" : "nyc1",
    "size" : "s-8vcpu-16gb",
    "image" : 68259296,
    "ssh_keys" : [27410347, 27608055, 27590881],
    "private_networking" : true,
    "vpc_uuid" : "47e5c00a-2b23-4dac-bed4-0e44659941f3",
    "monitoring" : true
}

droplet = Droplet(**droplet_data)

aut.create_droplet_from_snapshot(droplet)

```
