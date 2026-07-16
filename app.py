import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    env = os.getenv("FLASK_ENV", "development")
    return f"Hello! Running in {env} mode 🚀"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)