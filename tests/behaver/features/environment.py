# -- FILE:features/environment.py
import os

OD_TOKEN = os.getenv('OD_TOKEN')


def before_all(context):
    context.token = OD_TOKEN
    #context.token = '2431074b5dd96c51d3428a78496dc9c7d184ec0db150cd954483de4955e28890'
    context.headers = {'Authorization': 'Bearer ' + context.token}
    context.api_uri = 'https://api.digitalocean.com/v2'
