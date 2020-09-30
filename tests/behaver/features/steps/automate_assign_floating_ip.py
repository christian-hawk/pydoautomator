from behave import when, then, given
import requests
from pydoautomator import Automator


@given(u'a droplet with id {droplet_id} exists')
def step_impl(context, droplet_id: int):
    context.droplet_id = droplet_id
    full_url = '%s/droplets/%s' % (context.api_uri, str(droplet_id))
    context.json_headers = context.headers
    context.json_headers['Content-Type'] = 'application/json'
    response = requests.get(full_url, headers=context.json_headers)
    assert response.status_code == 200


@given(u'a floating ip with id {floating_ip} exists')
def step_impl(context, floating_ip: str):
    context.floating_ip = floating_ip
    full_url = '%s/floating_ips/%s' % (context.api_uri, str(floating_ip))
    response = requests.get(full_url, headers=context.json_headers)
    assert response.status_code == 200


@when(u'assign_floating_ip_to_droplet is called')
def step_impl(context):
    aut = Automator(context.token)
    aut.assign_floating_ip_to_droplet(context.floating_ip, context.droplet_id)


@then(u'floating ip should be assigned to droplet')
def step_impl(context):
    full_url = '%s/floating_ips/%s' % (context.api_uri,
                                       str(context.floating_ip))
    response = requests.get(full_url, headers=context.json_headers)
    json_resp = response.json()
    floating_ip_droplet_id = json_resp['floating_ip']['droplet']['id']
    assert floating_ip_droplet_id == context.droplet_id
