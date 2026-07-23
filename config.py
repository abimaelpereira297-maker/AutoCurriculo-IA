"""
==========================================================
CONFIGURAÇÕES DO PROJETO AUTOCURRICULO IA
==========================================================
"""

from pathlib import Path

# ==========================================================
# PASTA PRINCIPAL
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

# ==========================================================
# PASTAS
# ==========================================================

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
PERFIL_DIR = BASE_DIR / "perfil"
CHROME_PROFILE = PERFIL_DIR / "chrome"
PROMPTS_DIR = BASE_DIR / "prompts"
CURRICULOS_DIR = BASE_DIR / "curriculos"
CARTAS_DIR = BASE_DIR / "cartas"

# ==========================================================
# CRIAR PASTAS AUTOMATICAMENTE
# ==========================================================

for pasta in [
    DATA_DIR,
    LOG_DIR,
    PERFIL_DIR,
    CHROME_PROFILE,
    PROMPTS_DIR,
    CURRICULOS_DIR,
    CARTAS_DIR,
]:
    pasta.mkdir(parents=True, exist_ok=True)

# ==========================================================
# ARQUIVOS
# ==========================================================

VAGAS_JSON = DATA_DIR / "vagas.json"
VAGAS_SCORE_JSON = DATA_DIR / "vagas_score.json"
HISTORICO_JSON = DATA_DIR / "historico.json"

LOG_FILE = LOG_DIR / "autocurriculo.log"

# ==========================================================
# PLAYWRIGHT
# ==========================================================

HEADLESS = False

TIMEOUT = 30000

SCROLL_DELAY = 2

MAX_SCROLL = 30

MAX_VAGAS = 200

# ==========================================================
# LINKEDIN
# ==========================================================

LINKEDIN_LOGIN = "https://www.linkedin.com/login"

LINKEDIN_JOBS = "https://www.linkedin.com/jobs"

PALAVRAS_CHAVE = [
    "Assistente de Qualidade",
    "Inspetor de Qualidade",
    "Analista de Qualidade",
    "Auxiliar de Qualidade",
]

CIDADES = [
    "Porto Alegre",
    "Canoas",
    "Gravataí",
    "Cachoeirinha",
    "São Leopoldo",
    "Novo Hamburgo",
]

# ==========================================================
# OLLAMA
# ==========================================================

OLLAMA_URL = "http://localhost:11434/api/generate"

OLLAMA_MODEL = "mistral:latest"

TEMPERATURE = 0.2

# ==========================================================
# SCORE
# ==========================================================

SCORE_MINIMO = 85

# ==========================================================
# GOOGLE SHEETS
# ==========================================================

CREDENTIALS_FILE = BASE_DIR / "credentials.json"

PLANILHA = "Banco_Vagas"

ABA_VAGAS = "Vagas"

ABA_SCORE = "Score"

ABA_CANDIDATURAS = "Candidaturas"

# ==========================================================
# TELEGRAM
# ==========================================================

TELEGRAM_TOKEN = ""

TELEGRAM_CHAT_ID = ""

# ==========================================================
# PROMPTS
# ==========================================================

PROMPT_SCORE = PROMPTS_DIR / "score.txt"

PROMPT_CURRICULO = PROMPTS_DIR / "curriculo.txt"

PROMPT_CARTA = PROMPTS_DIR / "carta.txt"
# ==========================================================
# PERFIL DO CHROME (PLAYWRIGHT)
# ==========================================================

USER_DATA = str(CHROME_PROFILE)

# ==========================================================
# CARGO E LOCAL PADRÃO
# ==========================================================

CARGO = PALAVRAS_CHAVE[0]

LOCAL = CIDADES[0]
# ==========================================================
# PALAVRAS-CHAVE PARA SCORE
# ==========================================================

KEYWORDS_POSITIVAS = [
    "qualidade",
    "assistente",
    "analista",
    "inspeção",
    "controle",
    "iso",
    "auditoria",
    "processo",
    "melhoria",
    "5s",
    "indicadores",
    "não conformidade",
    "fmea",
    "pdca",
    "lean",
    "six sigma",
]

KEYWORDS_NEGATIVAS = [
    "estágio",
    "trainee",
    "júnior sem experiência",
]
# ==========================================================
# PALAVRAS-CHAVE DO ENGINE
# ==========================================================

KEYWORDS_POSITIVAS = [

    "qualidade",
    "assistente",
    "analista",
    "inspeção",
    "controle",
    "iso",
    "auditoria",
    "processo",
    "melhoria",
    "5s",
    "lean",
    "pdca",
    "kaizen",
    "não conformidade",
    "indicadores",
    "sgq",
    "fmea",
    "8d",
    "cep",
    "metrologia",
    "laboratório",
    "calibração"

]

KEYWORDS_NEGATIVAS = [

    "estágio",
    "trainee",
    "júnior sem experiência",
    "sem experiência",
    "vendedor",
    "telemarketing"

]
CURRICULOS_TXT = CURRICULOS_DIR / "txt"
CURRICULOS_DOCX = CURRICULOS_DIR / "docx"
CURRICULOS_PDF = CURRICULOS_DIR / "pdf"

for pasta in [
    CURRICULOS_TXT,
    CURRICULOS_DOCX,
    CURRICULOS_PDF,
]:
    pasta.mkdir(parents=True, exist_ok=True)