# DMetroverse Backend API

A high-performance, fully async FastAPI proxy wrapper for all Delhi Metro Rail Corporation (DMRC) backend API endpoints.

This project was built to allow frontend applications (like the DMetroverse UI) to smoothly interface with the DMRC backend without facing strict CORS blockades from the browser. 

## Features

- **Blazing Fast**: Uses `httpx.AsyncClient` holding a persistent connection pool.
- **RESTful Endpoints**: Grouped cleanly across Journey Planning, Service Status, CMS Pages, Corporate Info, Tenders, and Tourism.
- **Interactive API Docs**: Comes built-in with Swagger UI to test and review live.
- **CORS Unlocked**: Enables client-side rendering frameworks (React, Vite, Next) to consume the DMRC capabilities flawlessly.

---

## 🚀 Running Locally

Ensure you have **Python 3.11+** installed.

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the Development Server**
   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

3. Open your browser and go to:
   - **Main Entry:** `http://127.0.0.1:8000/`
   - **Live API Docs & Testing Page:** `http://127.0.0.1:8000/help` or `http://127.0.0.1:8000/docs`

---

## 🛠️ Tech Stack
- **Framework:** FastAPI
- **Proxy Client:** HTTPX (Asynchronous HTTP)
- **Runtime:** Uvicorn (ASGI server with high-performance `uvloop`)
- **Data Validation:** Pydantic

---

## 🔒 Configuration & Access Control
By default, the server restricts certain incoming requests based on HTTP `Origin` to prevent unwanted hotlinking. 

However, **in development mode**, the server freely accepts `localhost` and `127.0.0.1` traffic so you can rapidly develop your connected frontend!

If you wish to change the hardcoded allowed domains for production, modify `_default_origins` in `app/config.py`.

---

## 🌍 Deploying to Render.com

This backend is plug-and-play ready for [Render.com](https://render.com/).

1. Create a **New Web Service** and connect this repository.
2. Complete the configuration with:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Click **Deploy**. Render respects the `.python-version` file automatically.
