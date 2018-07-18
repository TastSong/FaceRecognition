import urllib,sys
import ssl
from urllib.request import urlopen
import json

AK = "yuZAGBb5s2h3og5Fl1DxRsji"
SK = "0KoZEsIGeucYjVvMTnUKWt8UcI3F7IpO"

# token 请求 url 与图片不一样
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
