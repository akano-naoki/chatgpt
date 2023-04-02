import argparse
import os
import requests
import json

# APIキーの設定
api_key = os.environ['OPENAI_API_KEY']
api_endpoint = "https://api.openai.com/v1/chat/completions"
model = 'gpt-3.5-turbo'

parser = argparse.ArgumentParser(description="Chat with GPT-3 using a prompt.")
parser.add_argument("prompt", type=str, help="The prompt you want to use.")
args = parser.parse_args()


# ヘッダーの設定
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# データの設定
data = {
    "model": model,
    "messages": [{"role": "user", "content": args.prompt}],
    "temperature": 0.8,
    "max_tokens": 2000
}

# APIリクエストの送信
response = requests.post(api_endpoint, headers=headers, json=data)

# レスポンスの解析
response_data = json.loads(response.text)
generated_message = response_data['choices'][0]['message']['content']

# 生成されたメッセージの表示
print(generated_message)
