# 🏷️ CobrançaAI

**Agente de cobrança e conciliação para PMEs brasileiras**

Recupera até 80% do que seus clientes devem via WhatsApp e voz. Você só paga quando recuperamos.

---

## 🎯 O Problema

- **9,4 milhões** de CNPJs inadimplentes no Brasil (R$ 247,8 bi)
- **8,9 milhões** são micro e pequenas empresas (R$ 214,4 bi)
- PMEs não têm time de cobrança — perdem receita por falta de processo

---

## 💡 A Solução

Um agente de IA que:
1. **Importa** boletos, Pix e notas fiscais (Asaas, Conta Azul, Omie, CSV)
2. **Identifica** quem deve, quanto e quando venceu
3. **Cobra automaticamente** por WhatsApp e voz — educado, dentro do CDC
4. **Negocia** parcelamento dentro das regras que você define
5. **Concilia** automaticamente quando o cliente paga
6. **Entrega** relatório do que recuperou

---

## 💰 Preço Justo por Resultado

| Modelo | Detalhes |
|--------|----------|
| **Taxa de sucesso** | **7% sobre valor recuperado** |
| **Custo fixo** | **R$ 0,99 por cobrança ativada** |
| **Teste grátis** | **30 dias** sem cartão |

> Você só paga muito se recuperar muito. Se não recuperar, paga centavos.

---

## 🏗️ Arquitetura

```
┌─────────────────┐     HTTPS/JSON      ┌──────────────────┐
│  Landing Page   │ ◄─────────────────► │   API Backend    │
│  (Vercel)       │   REST API          │  (FastAPI + SQLite)│
└─────────────────┘                     └──────────────────┘
                                                │
                                                ▼
                                        ┌───────────────┐
                                        │   Banco       │
                                        │   SQLite      │
                                        └───────────────┘
```

---

## 🚀 Deploy

### Landing Page (Vercel)
- **Framework:** Static HTML/CSS/JS
- **Output Directory:** `agentguard-landing`
- **URL:** `https://cobrancai.vercel.app`

### API Backend (Koyeb / Render / Deta)
- **Framework:** FastAPI + SQLite
- **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- **Build:** `pip install -r requirements.txt`

---

## 📁 Estrutura

```
cobrancai/
├── agentguard-landing/     # Landing page (HTML/CSS/JS)
│   └── index.html
├── app/                    # FastAPI Backend
│   ├── main.py
│   └── routers/
│       ├── agents.py
│       └── events.py
├── requirements.txt
└── README.md
```

---

## 🔧 Desenvolvimento Local

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar API
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Rodar Landing Page
cd agentguard-landing && python -m http.server 8000
```

---

## 📊 APIs

| Endpoint | Descrição |
|----------|-----------|
| `GET /health` | Health check |
| `GET /agents/` | Listar agentes |
| `POST /agents/` | Criar agente |
| `POST /events/ingest` | Ingerir evento |
| `GET /events/stats/{id}` | Stats da sessão |

---

## 📈 Roadmap

- [x] Landing page (HTML/CSS/JS)
- [x] API FastAPI + SQLite
- [ ] Integração Asaas (webhook + API)
- [ ] Régua de cobrança (48h, CDC compliant)
- [ ] Dashboard (recuperação, conciliação)
- [ ] Conciliação automática Pix + boleto
- [ ] Banco de avaliações (flywheel)

---

## 📝 Licença

MIT License - Livre para uso comercial.

---

**CobrançaAI** — Recuperamos seu dinheiro. Você cresce.