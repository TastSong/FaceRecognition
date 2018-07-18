# encoding:utf-8
import urllib
from tokenURL import GetToken
import base64
import json

'''
人脸检测与属性分析
'''
def FaceRecognition(imgFilePath):
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"

    # 二进制方式打开图片文件
    f = open(imgFilePath, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img,"image_type":"BASE64","face_field":"age,beauty,faceshape,facetype"}
    params = urllib.parse.urlencode(params).encode(encoding='UTF8')

    access_token = GetToken()
    request_url = request_url + "?access_token=" + access_token
    request = urllib.request.Request(url=request_url, data=params)
    request.add_header('Content-Type', 'application/json')
    response = urllib.request.urlopen(request)
    content = response.read()
    # s1 = content.decode('utf-8')
    if content:
        js = json.loads(content)
        return js['result']['face_list'][0]['beauty']
    return None


if __name__ == "__main__":
    beauty = FaceRecognition("img/1.jpg")
    print('beauty = ', beauty) #此处只用人脸的魅力值做演示
