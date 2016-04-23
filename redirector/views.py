from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
from redirector.utils import DataGetter

@api_view(['GET', 'POST'])
def redirector(request):
    """
    Redirect all requests which come from the front end
    """
    data_dict = request.data
    current_url = data_dict.get('url')
    payload = data_dict.get('payload')
    request_method = data_dict.get('method')


    current_data_getter = DataGetter()

    data_response = current_data_getter.get_data(request_method, current_url, payload)

    return Response(data_response)
