import urllib,sys
import ssl
from urllib.request import urlopen
import json

AK = "你的AK"
SK = "你的SK"

# token 请求 url 与图片不一样
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials' \
       '&client_id=%s' \
       '&client_secret=%s' % (AK, SK)

def GetToken():
    request = urllib.request.Request(host)
    print(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if (content):
        js = json.loads(content)
        # return js['refresh_token']
        return js['access_token']
    return None
