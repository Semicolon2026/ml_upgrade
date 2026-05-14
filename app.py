from flask import Flask, jsonify
from app.crypto_service import get_crypto_status

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "ml_upgrade",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify(get_crypto_status())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
