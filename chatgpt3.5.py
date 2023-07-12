import openai
import json
import os
import requests

os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"

# 配置OpenAI API凭证
openai.api_key = "sk-xxxxxxxxxxxxxxxx"
message="hello"

def chatgpt(message):
    # 发送请求
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer %s"% openai.api_key
    }

    data = {
        "model": "gpt-3.5-turbo-16k",
        "messages": [{"role": "user", "content": "%s" % message}],
        "temperature": 0.7
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    return response.json().get("choices")[0].get("message").get("content")


# print(chatgpt("chatgpt 你好吗"))


