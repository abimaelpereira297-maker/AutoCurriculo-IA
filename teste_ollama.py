import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "mistral:latest",
    "prompt": "Responda apenas com OK.",
    "stream": False
}

print("Enviando...")

r = requests.post(url, json=payload, timeout=30)

print("Status:", r.status_code)
print(r.json())