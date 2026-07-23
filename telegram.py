import requests

BOT_TOKEN = "SEU_TOKEN_AQUI"
CHAT_ID = "SEU_CHAT_ID"


def enviar_alerta(vaga):

    msg = f"""
🚨 NOVA VAGA BOA

📌 {vaga['titulo']}
🏢 {vaga['empresa']}
📍 {vaga['localizacao']}
⭐ Score: {vaga['score']}
🔗 {vaga['link']}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": msg
    })