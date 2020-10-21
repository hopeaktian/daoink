# -*- coding: utf-8 -*-
import json
import requests

# 请求的头部内容
# 以下的 Id 与 Key 都是无效的仅做示范，在实际试验中请替换成自己的 Id 与 Key
headers = {
    "X-LC-Id": "pq2BaybjAigwb7ATgKO0ggmK-gzGzoHsz",
    "X-LC-Key": "7VMMYQ8HyXDwNqWksMPjuEsW",
    "Content-Type": "application/json",
}

# 请求发送验证码 API
REQUEST_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/requestSmsCode'

# 请求校验验证码 API
VERIFY_SMS_CODE_URL = 'https://api.leancloud.cn/1.1/verifySmsCode/'


def send_message(phone):
    """
    通过 POST 请求 requestSmsCode API 发送验证码到指定手机
    :param phone: 通过网页表单获取的电话号
    :return:
    """
    data = {
        "mobilePhoneNumber": phone,
    }

    # post 方法参数包含三部分，如我们之前分析 API 所述
    # REQUEST_SMS_CODE_URL: 请求的 URL
    # data: 请求的内容，另外要将内容编码成 JSON 格式
    # headers: 请求的头部，包含 Id 与 Key 等信息
    r = requests.post(REQUEST_SMS_CODE_URL, data=json.dumps(data), headers=headers)

    # 响应 r 的 status_code 值为 200 说明响应成功
    # 否则失败
    if r.status_code == 200:
        return True
    else:
        return False


def verify(phone, code):
    """
    发送 POST 请求到 verifySmsCode API 获取校验结果
    :param phone: 通过网页表单获取的电话号
    :param code: 通过网页表单获取的验证码
    :return:
    """
    # 使用传进的参数 code 与 phone 拼接出完整的 URL
    target_url = VERIFY_SMS_CODE_URL + "%s?mobilePhoneNumber=%s" % (code, phone)

    # 这里的 POST 方法只传入了两个参数
    # target_url： 请求的 URL
    # headers: 请求的头部，包含 Id 与 Key 等信息
    r = requests.post(target_url, headers=headers)

    # 响应 r 的 status_code 值为 200 说明验证成功
    # 否则失败
    if r.status_code == 200:
        return True
    else:
        return False
