# Finance API Demo

A simple FastAPI service that fetches stock price data and exposes it as RESTful APIs.

---

## 🚀 Features
- Fetch stock price data using yfinance
- REST API built with FastAPI
- Input validation & error handling
- Interactive API docs (/docs)
- Docker-ready

---

## 🛠 Tech Stack
- Python 3.11
- FastAPI
- Pandas
- yfinance
- Docker

---

## 📁 Project Structure
```
ml-api-demo/
├─ app/
│  ├─ main.py        # FastAPI entry point
│  └─ finance.py     # data fetching logic
├─ Dockerfile
├─ requirements.txt
└─ README.md
```

---

## 📌 API Usage

### POST /api/price

#### Request
```json
{
  "ticker": "AAPL",
  "days": 30
}
```

#### Response
```json
{
  "ticker": "AAPL",
  "last_close": 189.32,
  "rows": [...]
}
```

---

## ▶️ Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🌐 API Docs

http://127.0.0.1:8000/docs

---

## 📦 Future Improvements
- Add caching (Redis)
- Add database (PostgreSQL)
- Deploy to cloud (AWS / GCP)

---

## 👩‍💻 Author

Yasin