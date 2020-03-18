import requests

# POST for qbo sandbox
from OAuth2DjangoSampleApp import settings

def requestQBO(method, url, context, payload=None):
    
    if settings.oauth_flag == 2:
        headers = {'Accept': 'application/json', 'User-Agent': 'PythonSampleApp2.0', 'Authorization': 'Bearer '+settings.ID_TOKEN_ISSUER}
        req = requests.request(method,url, headers=headers, json=payload)
    else:
        pass
    return req



    
        
