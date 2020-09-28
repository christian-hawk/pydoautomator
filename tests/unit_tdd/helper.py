import json

# Test data

valid_droplet = {
    "name": "t1.techno24x7.com",
    "region": "nyc1",
    "size": "s-8vcpu-16gb",
    "image": 68259296,
    "ssh_keys": [27410347, 27608055, 27590881],
    "private_networking": True,
    "vpc_uuid": "47e5c00a-2b23-4dac-bed4-0e44659941f3",
    "monitoring": True
}

valid_droplet_created_json_response = '{"droplet":{"id":209450285,"name":"t1.techno24x7.com","memory":16384,"vcpus":8,"disk":320,"locked":false,"status":"new","kernel":null,"created_at":"2020-09-26T03:27:40Z","features":[],"backup_ids":[],"next_backup_window":null,"snapshot_ids":[],"image":{"id":68259296,"name":"t1.techno24x7.com-final-test420","distribution":"Ubuntu","slug":null,"public":false,"regions":["nyc1"],"created_at":"2020-08-11T20:38:19Z","min_disk_size":160,"type":"snapshot","size_gigabytes":5.13,"tags":[],"status":"available"},"volume_ids":[],"size":{"slug":"s-8vcpu-16gb","memory":16384,"vcpus":8,"disk":320,"transfer":6.0,"price_monthly":80.0,"price_hourly":0.11905,"regions":["ams2","ams3","blr1","fra1","lon1","nyc1","nyc2","nyc3","sfo1","sfo2","sfo3","sgp1","tor1"],"available":true},"size_slug":"s-8vcpu-16gb","networks":{"v4":[],"v6":[]},"region":{"name":"New York 1","slug":"nyc1","features":["private_networking","backups","ipv6","metadata","install_agent","storage","image_transfer"],"available":true,"sizes":["s-1vcpu-1gb","512mb","s-1vcpu-2gb","1gb","s-3vcpu-1gb","s-2vcpu-2gb","s-1vcpu-3gb","s-2vcpu-4gb","2gb","s-4vcpu-8gb","m-1vcpu-8gb","c-2","4gb","c2-2vcpu-4gb","g-2vcpu-8gb","gd-2vcpu-8gb","m-16gb","s-8vcpu-16gb","s-6vcpu-16gb","c-4","8gb","c2-4vpcu-8gb","m-2vcpu-16gb","m3-2vcpu-16gb","g-4vcpu-16gb","gd-4vcpu-16gb","m6-2vcpu-16gb","m-32gb","s-8vcpu-32gb","c-8","c2-8vpcu-16gb","m-4vcpu-32gb","m3-4vcpu-32gb","g-8vcpu-32gb","s-12vcpu-48gb","gd-8vcpu-32gb","m6-4vcpu-32gb","m-64gb","s-16vcpu-64gb","c-16","32gb","c2-16vcpu-32gb","m-8vcpu-64gb","m3-8vcpu-64gb","g-16vcpu-64gb","s-20vcpu-96gb","48gb","gd-16vcpu-64gb","m6-8vcpu-64gb","m-128gb","s-24vcpu-128gb","64gb","c2-32vpcu-64gb","m-16vcpu-128gb","m3-16vcpu-128gb","s-32vcpu-192gb","m-24vcpu-192gb","m6-16vcpu-128gb","m3-24vcpu-192gb","m6-24vcpu-192gb"]},"tags":[]},"links":{"actions":[{"id":1030573508,"rel":"create","href":"https://api.digitalocean.com/v2/actions/1030573508"}]}}'

valid_droplet_created_response = json.loads(
    valid_droplet_created_json_response)

valid_creation_in_progress_json_resp = '{"action":{"id":1030573508,"status":"in-progress","type":"create","started_at":"2020-09-26T03:27:40Z","completed_at":null,"resource_id":209450285,"resource_type":"droplet","region":{"name":"New York 1","slug":"nyc1","features":["private_networking","backups","ipv6","metadata","install_agent","storage","image_transfer"],"available":true,"sizes":["c-2","c-4","m-1vcpu-8gb","m-16gb","m-32gb","m-64gb","m-128gb","512mb","1gb","2gb","4gb","8gb","32gb","48gb","64gb","s-1vcpu-1gb","s-3vcpu-1gb","s-1vcpu-2gb","s-2vcpu-2gb","s-1vcpu-3gb","s-2vcpu-4gb","s-4vcpu-8gb","s-6vcpu-16gb","s-8vcpu-32gb","g-2vcpu-8gb","m-2vcpu-16gb","m3-2vcpu-16gb","m6-2vcpu-16gb","s-12vcpu-48gb","s-16vcpu-64gb","s-20vcpu-96gb","s-24vcpu-128gb","s-32vcpu-192gb","gd-2vcpu-8gb","s-8vcpu-16gb","c2-2vcpu-4gb","c2-4vpcu-8gb","c2-8vpcu-16gb","c2-16vcpu-32gb","c2-32vpcu-64gb"]},"region_slug":"nyc1"}}'

valid_creation_in_progress_response = json.loads(
    valid_creation_in_progress_json_resp)

valid_creation_completed_json_resp = '{"action":{"id":1030573508,"status":"completed","type":"create","started_at":"2020-09-26T03:27:40Z","completed_at":"2020-09-26T03:33:44Z","resource_id":209450285,"resource_type":"droplet","region":{"name":"New York 1","slug":"nyc1","features":["private_networking","backups","ipv6","metadata","install_agent","storage","image_transfer"],"available":true,"sizes":["c-2","c-4","m-1vcpu-8gb","m-16gb","m-32gb","m-64gb","m-128gb","512mb","1gb","2gb","4gb","8gb","32gb","48gb","64gb","s-1vcpu-1gb","s-3vcpu-1gb","s-1vcpu-2gb","s-2vcpu-2gb","s-1vcpu-3gb","s-2vcpu-4gb","s-4vcpu-8gb","s-6vcpu-16gb","s-8vcpu-32gb","g-2vcpu-8gb","m-2vcpu-16gb","m3-2vcpu-16gb","m6-2vcpu-16gb","s-12vcpu-48gb","s-16vcpu-64gb","s-20vcpu-96gb","s-24vcpu-128gb","s-32vcpu-192gb","gd-2vcpu-8gb","s-8vcpu-16gb","c2-2vcpu-4gb","c2-4vpcu-8gb","c2-8vpcu-16gb","c2-16vcpu-32gb","c2-32vpcu-64gb"]},"region_slug":"nyc1"}}'

valid_creation_completed_response = json.loads(
    valid_creation_completed_json_resp)
