from behave import when, then
from pydoautomator import Automator
import requests


@when(u'destroy droplet is called')
def step_impl(context):
    aut = Automator(context.token)
    aut.destroy_droplet(context.droplet_id)


@then(u'droplet should be destroyed')
def step_impl(context):
    full_url = '%s/droplets/%s' % (context.api_uri, context.droplet_id)
    response = requests.get(full_url, headers=context.headers)
    assert response.status_code == 404, 'Response status_code is NOT 404!'
