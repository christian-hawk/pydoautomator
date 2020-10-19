from behave import when, then, given
import requests
from pydoautomator import Automator, Droplet


@given(u'droplet {droplet_id:d} exists')
def step_impl(context, droplet_id):
    context.droplet_id = droplet_id
    full_url = '%s/droplets/%s' % (context.api_uri, context.droplet_id)
    response = requests.get(full_url, headers=context.headers)
    assert response.status_code == 200, 'response status code is %s' % response.status_code

@when(u'turnoff droplet is called')
def step_impl(context):
    aut = Automator(context.token)
    aut.turnoff_droplet(context.droplet_id)


@then(u'turnoff droplet')
def step_impl(context):
    full_url = '%s/droplets/%s' % (context.api_uri, context.droplet_id)
    response = requests.get(full_url, headers=context.headers)
    json_resp = response.json()
    droplet_status = json_resp['droplet']['status']
    assert droplet_status == 'off', 'droplet status is %s! should be off.' % droplet_status

