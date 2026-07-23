import gspread
from google.oauth2.service_account import Credentials

SHEET_NAME = "VagasLinkedIn"

def conectar():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    return gspread.authorize(creds)


def enviar_vagas(vagas):
    client = conectar()

    try:
        sheet = client.open(SHEET_NAME).sheet1
    except:
        sheet = client.create(SHEET_NAME).sheet1
        sheet.append_row(["Data", "Titulo", "Empresa", "Score"])

    for v in vagas:
        sheet.append_row([
            v["data"],
            v["titulo"],
            v["empresa"],
            v["score"]
        ])