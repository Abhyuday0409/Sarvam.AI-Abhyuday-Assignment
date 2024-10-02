import requests

url = 'https://api.sarvam.ai/<api-endpoint>'
headers = {
    'API-Subscription-Key': 'your-api-key'
}
data = {
    'text': 'Sarvam AI is a powerful platform for LLM tasks.'
}

response = requests.post(url, headers=headers, json=data)
print(response.json())


import requests

url = "https://api.sarvam.ai/text-to-speech"

payload = {
    "inputs": ["<string>"],
    "target_language_code": "hi-IN",
    "speaker": "meera",
    "pitch": 0,
    "pace": 1.65,
    "loudness": 1.5,
    "speech_sample_rate": 8000,
    "enable_preprocessing": True,
    "model": "bulbul:v1"
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)