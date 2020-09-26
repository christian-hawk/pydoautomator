import requests
from behave import when, then, given


@given(u'snapshot name is {snapshot}')
def step_impl(context, snapshot):
    context.snapshot = snapshot


@given(u'snapshot exists')
def step_impl(context):
    full_url = '%s/snapshots?name=%s' % (context.api_uri, context.snapshot)
    response = requests.get(full_url, headers=context.headers)
    json_resp = response.json()
    assert(json_resp['snapshots'][0]['name'] == context.snapshot)
    context.snapshot_id = json_resp['snapshots'][0]['id']


@given(u'host name is {host}')
def step_impl(context, host):
    context.host = host


@when(u'I receive a droplet start call')
def step_impl(context):
    response = requests.post('http://localhost:5000/droplet/create', data={
        "snapshot": context.snapshot
    })


@then(u'droplet should be created')
def step_impl(context):
    full_url = '%s/droplets' % context.api_uri
    response = requests.get(full_url, headers=context.headers)
    context.droplets = response.json()['droplets']
    image_name = ''
    for droplet in context.droplets:
        if droplet['name'] == context.host:
            image_name = droplet['image']['name']
    assert(image_name == context.snapshot)


@then(u'droplet name should be {host}')
def step_impl(context, host):
    droplet_name = ''
    for droplet in context.droplets:
        if droplet['name'] == context.host:
            droplet_name = droplet['name']
    assert(droplet_name == context.host)
