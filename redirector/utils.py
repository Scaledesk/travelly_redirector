import requests
from django.conf import settings
import json


class DataGetter(object):
    """
    Class for getting the data 
    from the API servers
    """
    def __init__(self):
       """
       Initiates the class
       with the authentication credentials
       """
       self.username = 'BIS151'
       self.password = 'iuW109trq'

    def get_data(self, request_method, url, payload):
       """
       Make request to the API server
       """
       current_api_url = settings.BASE_API + url

       # headers for the request
       headers = {
                    'x-UserName': self.username,
                    'x-Password': self.password
                  }

       # general request data
       request_config = {
		          'data': json.dumps(payload)
                        }

       request_response = None
       if request_method == 'POST':
           request_response = requests.post(current_api_url, headers=headers, data=request_method)
       elif request_method == 'GET':
           request_response = requests.get(current_api_url, headers=headers, data=request_method)

       return json.loads(request_response.content)
