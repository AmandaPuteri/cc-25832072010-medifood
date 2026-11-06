from datetime import datetime, timezone
import os
import socket

from flask import Flask, jsonify, render_template

app = Flask(__name__)

DIET_CATEGORIES = [
    {
        "id": "diabetes",
        "nama": "Diabetes",
        "fokus": "Gula dan karbohidrat terkontrol",
    },
    {
        "id": "hipertensi",
        "nama": "Hipertensi",
        "fokus": "Rendah natrium (garam)",
    },
    {
        "id": "pasca-operasi",
        "nama": "Pasca-operasi",
        "fokus": "Tinggi protein dan mudah dicerna",
    },
]


@app.get("/")
def index():
    return render_template(
        "index.html",
        app_env=os.getenv("APP_ENV", "development"),
        hostname=socket.gethostname(),
        categories=DIET_CATEGORIES,
    )


@app.get("/health")
def health():
    return jsonify(
        status="ok",
        environment=os.getenv("APP_ENV", "development"),
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@app.get("/api/info")
def info():
    return jsonify(
        project="Medifood Garut",
        course="Cloud Computing",
        code="PTI 2802",
        meeting=3,
        milestone="M03",
        deployment="AWS EC2 Ubuntu Server 24.04",
    )


@app.get("/api/diet-categories")
def diet_categories():
    return jsonify(categories=DIET_CATEGORIES)
