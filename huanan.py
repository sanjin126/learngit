import requests
from bs4 import BeautifulSoup
import time
import os
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20210111 import sms_client, models

def sms(code) :
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户 SecretId 和 SecretKey，此处还需注意密钥对的保密
        # 代码泄露可能会导致 SecretId 和 SecretKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考，建议采用更安全的方式来使用密钥，请参见：https://cloud.tencent.com/document/product/1278/85305
        # 密钥可前往官网控制台 https://console.cloud.tencent.com/cam/capi 进行获取
        cred = credential.Credential("AKIDrXyB9rJWUCftra3HGzSgeNq3tUpunQow", "uZy70f4E8oEPKzPZT8aruhGZdR087tSo")
        # 实例化一个http选项，可选的，没有特殊需求可以跳过
        httpProfile = HttpProfile()
        httpProfile.endpoint = "sms.tencentcloudapi.com"

        # 实例化一个client选项，可选的，没有特殊需求可以跳过
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        # 实例化要请求产品的client对象,clientProfile是可选的
        client = sms_client.SmsClient(cred, "ap-beijing", clientProfile)

        # 实例化一个请求对象,每个接口都会对应一个request对象
        req = models.SendSmsRequest()
        params = {
            "PhoneNumberSet": [ "18237379593" ],
            "SmsSdkAppId": "1400809556",
            "SignName": "春禾支教",
            "TemplateId": "1755499",
            "TemplateParamSet": [ str(code) ]
        }
        req.from_json_string(json.dumps(params))

        # 返回的resp是一个SendSmsResponse的实例，与请求对象对应
        resp = client.SendSms(req)
        # 输出json格式的字符串回包
        print(resp.to_json_string())

    except TencentCloudSDKException as err:
        sms(444)
        print(err)

try:
    url = 'http://site.scnu.edu.cn/yjspy/tzgg/'
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    content = response.text
    soup =BeautifulSoup(content,'html.parser')
    cw = soup.select('#right > ul > li:nth-child(1) > a')
    print(cw)
    file = r'C:\Users\10326\Music\安河桥.mp3'

    while (True) :
        time.sleep(5)   # 加上3s 的延时防止被反爬
        response = requests.get(url)
        response.encoding = response.apparent_encoding
        soup =BeautifulSoup(response.text,'html.parser')
        cw = soup.select('#right > ul > li:nth-child(1) > a')
        print('查询:'+str(time.time())+str(cw))
        if (content != response.text):
            print('hit')
            sms(111)
            print('---------new-----------')
            print(response.text)
            print('----------old--------')
            print(content)
            # os.system(file)
            break
except:
    sms(444)
