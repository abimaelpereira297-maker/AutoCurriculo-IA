# 🤖 AutoCurriculo IA

Sistema inteligente para busca, análise e organização de vagas de emprego utilizando Inteligência Artificial local com Ollama.

---

## 🚀 Funcionalidades

- ✅ Coleta automática de vagas do LinkedIn
- ✅ Banco de dados SQLite
- ✅ Análise das vagas usando IA (Ollama + Mistral)
- ✅ Score inteligente de compatibilidade
- ✅ Classificação por prioridade
- ✅ Exportação para Excel
- ✅ Geração automática de currículo
- ✅ Estrutura para Google Sheets
- ✅ Estrutura para Telegram

---

## 🧠 Tecnologias

- Python 3
- Playwright
- SQLite
- Ollama
- Mistral
- OpenPyXL
- Git
- GitHub

---

## 📂 Estrutura

```
AutoCurriculo-IA/

├── main.py
├── linkedin.py
├── ollama_ai.py
├── ollama_score.py
├── engine.py
├── score.py
├── export.py
├── gerar_curriculo.py
├── dashboard.py
├── db.py
├── config.py
├── requirements.txt
│
├── prompts/
├── templates/
└── README.md
```

---

## ⚙️ Como instalar

Clone o projeto

```bash
git clone https://github.com/abimaelpereira297-maker/AutoCurriculo-IA.git
```

Entre na pasta

```bash
cd AutoCurriculo-IA
```

Instale as dependências

```bash
pip install -r requirements.txt
```

Instale o Playwright

```bash
playwright install
```

Instale o Ollama

https://ollama.com

Baixe o modelo

```bash
ollama pull mistral
```

---

## ▶️ Executar

```bash
python main.py
```

---

## 📊 Fluxo do projeto

```
LinkedIn
      │
      ▼
Playwright
      │
      ▼
Coleta das vagas
      │
      ▼
SQLite
      │
      ▼
Ollama + Mistral
      │
      ▼
Score IA
      │
      ▼
Classificação
      │
      ▼
Excel
      │
      ▼
Currículo Inteligente
```

---

## 📌 Roadmap

- [x] Coleta de vagas
- [x] Banco SQLite
- [x] Score com IA
- [x] Exportação para Excel
- [x] GitHub

Próximas versões

- [ ] Dashboard Web
- [ ] Currículo personalizado
- [ ] Carta de apresentação automática
- [ ] Telegram
- [ ] Google Sheets
- [ ] Interface Web
- [ ] Candidatura automática

---

## 👨‍💻 Autor

**Abimael Pereira**

GitHub:

https://github.com/abimaelpereira297-maker

---

## ⭐ Projeto em desenvolvimento

Este projeto está em evolução contínua.