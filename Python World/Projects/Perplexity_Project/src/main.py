import requests
import json
import re

api_key = "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"

user_question = input("Enter your question: ")

url = "https://api.perplexity.ai/chat/completions"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "model": "sonar-pro",
    "temperature": 0,
    "max_tokens": 500,
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"{user_question}"}
    ]
}

response = requests.post(url, headers=headers, json=data)

# Correct way to parse and print response when successful
if response.status_code == 200:
    data = response.json()
    content = data["choices"][0]["message"]["content"]
    clean_text = re.sub(r'\[\d+\]', '', content)
    print(clean_text.strip())
    with open ("../output.md", "w") as output_md:
        output_md.write(clean_text.strip())
else:
    print(f"Error: {response.status_code}")
    print(response.text)