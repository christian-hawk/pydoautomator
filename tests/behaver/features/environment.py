# -- FILE:features/environment.py

def before_all(context):
    context.token = '2431074b5dd96c51d3428a78496dc9c7d184ec0db150cd954483de4955e28890'
    context.headers = {'Authorization': 'Bearer ' + context.token}
    context.api_uri = 'https://api.digitalocean.com/v2'
