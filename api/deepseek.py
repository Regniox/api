from flask import Blueprint, request
import requests
from openai import OpenAI

deepseek_bp = Blueprint('deepseek_bp', __name__)

# deepseek api_key https://api-docs.deepseek.com

@deepseek_bp.route("/deepseek/")
def deepseek():
    api_key = request.args.get('api_key')

    api_balance_url = "https://api.deepseek.com/user/balance/"
    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }

    response = requests.request("GET", api_balance_url, headers=headers, data=payload)
    return response.json(), 200

# Only inquire, do not engage in memory conversations
# You can add a database yourself to enable memory conversations
@deepseek_bp.route("/deepseek/ask/")
def deepseek_chat():
    api_key = request.args.get('api_key')
    question = request.args.get('question')

    client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com/")

    system_prompt  = "You are one of my assistants to solve my problems"

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt },
            {"role": "user", "content": question}
        ],
        max_tokens=4096,
        temperature=0.7,
        stream=False,
    )

    return response.choices[0].message.content, 200
