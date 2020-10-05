import responses

# mock api responses


def error_404_response(url):
    """Respond a 404 with dummy json
    """
    responses.add(
        responses.POST,
        url=url,
        json={'any_key': 'any_value'},
        status=404
    )


def assign_floating_ip_success_response(floating_ip: str, droplet_id: int):
    """needs to be used with @responses.activate
    Successfull responses for params

    :param floating_ip: floating ip to be sucessfully assigned
    :type floating_ip: str
    :param droplet_id: droplet id to sucessfully receive fip
    :type droplet_id: int
    """

    response_action_data = {
        "action": {
            "id": 1032896014,
            "status": "in-progress",
            "type": "assign_ip",
            "started_at": "2020-09-29T18:21:38Z",
            "completed_at": None,
            "resource_id": 2757426197,
            "resource_type": "floating_ip",
            "region": {
                "name": "New York 1",
                "slug": "nyc1",
                "features": [
                    "private_networking",
                    "backups",
                    "ipv6",
                    "metadata",
                    "install_agent",
                    "storage",
                    "image_transfer"
                ],
                "available": True,
                "sizes": [
                    "c-2",
                    "c-4",
                    "m-1vcpu-8gb",
                    "m-16gb",
                    "m-32gb",
                    "m-64gb",
                    "m-128gb",
                    "512mb",
                    "1gb",
                    "2gb",
                    "4gb",
                    "8gb",
                    "32gb",
                    "48gb",
                    "64gb",
                    "s-1vcpu-1gb",
                    "s-3vcpu-1gb",
                    "s-1vcpu-2gb",
                    "s-2vcpu-2gb",
                    "s-1vcpu-3gb",
                    "s-2vcpu-4gb",
                    "s-4vcpu-8gb",
                    "s-6vcpu-16gb",
                    "s-8vcpu-32gb",
                    "g-2vcpu-8gb",
                    "m-2vcpu-16gb",
                    "m3-2vcpu-16gb",
                    "m6-2vcpu-16gb",
                    "s-12vcpu-48gb",
                    "s-16vcpu-64gb",
                    "s-20vcpu-96gb",
                    "s-24vcpu-128gb",
                    "s-32vcpu-192gb",
                    "gd-2vcpu-8gb",
                    "s-8vcpu-16gb",
                    "c2-2vcpu-4gb",
                    "c2-4vpcu-8gb",
                    "c2-8vpcu-16gb",
                    "c2-16vcpu-32gb",
                    "c2-32vpcu-64gb"
                ]
            },
            "region_slug": "nyc1"
        }
    }

    responses.add(
        responses.POST,
        url='https://api.digitalocean.com/v2/floating_ips/%s/actions' % floating_ip,
        json=response_action_data,
        status=201
    )


def existing_droplet_response():
    """needs to be used with @responses.activate
    """
    responses.add(
        responses.GET,
        url='https://api.digitalocean.com/v2/droplets/209808688',
        json={
            "droplet": {
                "id": 209808688,
                "name": "t1.techno24x7.com",
                "memory": 16384,
                "vcpus": 8,
                "disk": 320,
                "locked": False,
                "status": "active",
                "kernel": None,
                "created_at": "2020-09-29T00:59:22Z",
                "features": [
                    "monitoring",
                    "private_networking"
                ],
                "backup_ids": [],
                "next_backup_window": None,
                "snapshot_ids": [],
                "image": {
                    "id": 70649304,
                    "name": "t1.techno24x7.com-latest-dev",
                    "distribution": "Ubuntu",
                    "slug": None,
                    "public": False,
                    "regions": [
                        "nyc1"
                    ],
                    "created_at": "2020-09-24T22:54:22Z",
                    "min_disk_size": 320,
                    "type": "snapshot",
                    "size_gigabytes": 1.92,
                    "tags": [],
                    "status": "available"
                },
                "volume_ids": [],
                "size": {
                    "slug": "s-8vcpu-16gb",
                    "memory": 16384,
                    "vcpus": 8,
                    "disk": 320,
                    "transfer": 6.0,
                    "price_monthly": 80.0,
                    "price_hourly": 0.11905,
                    "regions": [
                        "ams2",
                        "ams3",
                        "blr1",
                        "fra1",
                        "lon1",
                        "nyc1",
                        "nyc2",
                        "nyc3",
                        "sfo1",
                        "sfo2",
                        "sfo3",
                        "sgp1",
                        "tor1"
                    ],
                    "available": True
                },
                "size_slug": "s-8vcpu-16gb",
                "networks": {
                    "v4": [
                        {
                            "ip_address": "10.116.0.2",
                            "netmask": "255.255.240.0",
                            "gateway": "<nil>",
                            "type": "private"
                        },
                        {
                            "ip_address": "161.35.110.172",
                            "netmask": "255.255.240.0",
                            "gateway": "161.35.96.1",
                            "type": "public"
                        }
                    ],
                    "v6": []
                },
                "region": {
                    "name": "New York 1",
                    "slug": "nyc1",
                    "features": [
                        "private_networking",
                        "backups",
                        "ipv6",
                        "metadata",
                        "install_agent",
                        "storage",
                        "image_transfer"
                    ],
                    "available": True,
                    "sizes": [
                        "s-1vcpu-1gb",
                        "512mb",
                        "s-1vcpu-2gb",
                        "1gb",
                        "s-3vcpu-1gb",
                        "s-2vcpu-2gb",
                        "s-1vcpu-3gb",
                        "s-2vcpu-4gb",
                        "2gb",
                        "s-4vcpu-8gb",
                        "m-1vcpu-8gb",
                        "c-2",
                        "4gb",
                        "c2-2vcpu-4gb",
                        "g-2vcpu-8gb",
                        "gd-2vcpu-8gb",
                        "m-16gb",
                        "s-8vcpu-16gb",
                        "s-6vcpu-16gb",
                        "c-4",
                        "8gb",
                        "c2-4vpcu-8gb",
                        "m-2vcpu-16gb",
                        "m3-2vcpu-16gb",
                        "g-4vcpu-16gb",
                        "gd-4vcpu-16gb",
                        "m6-2vcpu-16gb",
                        "m-32gb",
                        "s-8vcpu-32gb",
                        "c-8",
                        "c2-8vpcu-16gb",
                        "m-4vcpu-32gb",
                        "m3-4vcpu-32gb",
                        "g-8vcpu-32gb",
                        "s-12vcpu-48gb",
                        "gd-8vcpu-32gb",
                        "m6-4vcpu-32gb",
                        "m-64gb",
                        "s-16vcpu-64gb",
                        "c-16",
                        "32gb",
                        "c2-16vcpu-32gb",
                        "m-8vcpu-64gb",
                        "m3-8vcpu-64gb",
                        "g-16vcpu-64gb",
                        "s-20vcpu-96gb",
                        "48gb",
                        "gd-16vcpu-64gb",
                        "m6-8vcpu-64gb",
                        "m-128gb",
                        "s-24vcpu-128gb",
                        "c-32",
                        "64gb",
                        "c2-32vpcu-64gb",
                        "m-16vcpu-128gb",
                        "m3-16vcpu-128gb",
                        "s-32vcpu-192gb",
                        "m-24vcpu-192gb",
                        "m6-16vcpu-128gb",
                        "m3-24vcpu-192gb",
                        "m6-24vcpu-192gb"
                    ]
                },
                "tags": [],
                "vpc_uuid": "47e5c00a-2b23-4dac-bed4-0e44659941f3"
            }
        },
        status=200)


def list_droplets_response():
    response_data = {
        "droplets": [
            {
                "id": 201147650,
                "name": "chris.testingenv.org",
                "memory": 4096,
                "vcpus": 2,
                "disk": 80,
                "locked": False,
                "status": "active",
                "kernel": None,
                "created_at": "2020-07-23T12:57:22Z",
                "features": [],
                "backup_ids": [],
                "next_backup_window": None,
                "snapshot_ids": [
                    69227970
                ],
                "image": {
                    "id": 67204635,
                    "name": "chris-testingenv-164.90.252.21",
                    "distribution": "Ubuntu",
                    "slug": None,
                    "public": False,
                    "regions": [
                        "nyc1"
                    ],
                    "created_at": "2020-07-22T21:53:58Z",
                    "min_disk_size": 60,
                    "type": "snapshot",
                    "size_gigabytes": 16.4,
                    "tags": [],
                    "status": "available"
                },
                "volume_ids": [],
                "size": {
                    "slug": "s-2vcpu-4gb",
                    "memory": 4096,
                    "vcpus": 2,
                    "disk": 80,
                    "transfer": 4.0,
                    "price_monthly": 20.0,
                    "price_hourly": 0.02976,
                    "regions": [
                        "ams2",
                        "ams3",
                        "blr1",
                        "fra1",
                        "lon1",
                        "nyc1",
                        "nyc2",
                        "nyc3",
                        "sfo1",
                        "sfo2",
                        "sfo3",
                        "sgp1",
                        "tor1"
                    ],
                    "available": True
                },
                "size_slug": "s-2vcpu-4gb",
                "networks": {
                    "v4": [
                        {
                            "ip_address": "161.35.111.46",
                            "netmask": "255.255.240.0",
                            "gateway": "161.35.96.1",
                            "type": "public"
                        },
                        {
                            "ip_address": "164.90.252.21",
                            "netmask": "255.255.252.0",
                            "gateway": "164.90.252.1",
                            "type": "public"
                        }
                    ],
                    "v6": []
                },
                "region": {
                    "name": "New York 1",
                    "slug": "nyc1",
                    "features": [
                        "private_networking",
                        "backups",
                        "ipv6",
                        "metadata",
                        "install_agent",
                        "storage",
                        "image_transfer"
                    ],
                    "available": True,
                    "sizes": [
                        "s-1vcpu-1gb",
                        "512mb",
                        "s-1vcpu-2gb",
                        "1gb",
                        "s-3vcpu-1gb",
                        "s-2vcpu-2gb",
                        "s-1vcpu-3gb",
                        "s-2vcpu-4gb",
                        "2gb",
                        "s-4vcpu-8gb",
                        "m-1vcpu-8gb",
                        "c-2",
                        "4gb",
                        "c2-2vcpu-4gb",
                        "g-2vcpu-8gb",
                        "gd-2vcpu-8gb",
                        "m-16gb",
                        "s-8vcpu-16gb",
                        "s-6vcpu-16gb",
                        "c-4",
                        "8gb",
                        "c2-4vpcu-8gb",
                        "m-2vcpu-16gb",
                        "m3-2vcpu-16gb",
                        "g-4vcpu-16gb",
                        "gd-4vcpu-16gb",
                        "m6-2vcpu-16gb",
                        "m-32gb",
                        "s-8vcpu-32gb",
                        "c-8",
                        "c2-8vpcu-16gb",
                        "m-4vcpu-32gb",
                        "m3-4vcpu-32gb",
                        "g-8vcpu-32gb",
                        "s-12vcpu-48gb",
                        "gd-8vcpu-32gb",
                        "m6-4vcpu-32gb",
                        "m-64gb",
                        "s-16vcpu-64gb",
                        "c-16",
                        "32gb",
                        "c2-16vcpu-32gb",
                        "m-8vcpu-64gb",
                        "m3-8vcpu-64gb",
                        "g-16vcpu-64gb",
                        "s-20vcpu-96gb",
                        "48gb",
                        "gd-16vcpu-64gb",
                        "m6-8vcpu-64gb",
                        "m-128gb",
                        "s-24vcpu-128gb",
                        "c-32",
                        "64gb",
                        "c2-32vpcu-64gb",
                        "m-16vcpu-128gb",
                        "m3-16vcpu-128gb",
                        "s-32vcpu-192gb",
                        "m6-16vcpu-128gb"
                    ]
                },
                "tags": [
                    "dev"
                ]
            }
        ],
        "links": {},
        "meta": {
            "total": 1
        }
    }
    responses.add(
        responses.GET,
        url='https://api.digitalocean.com/v2/droplets',
        json=response_data,
        status=200
    )
