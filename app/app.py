from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "app": "Secure CI/CD Demo",
        "status": "running",
        "message": "Deployed through a security-hardened pipeline"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/info")
def info():
    return jsonify({
        "pipeline": "GitHub Actions",
        "scanning": ["Bandit", "Trivy", "OWASP ZAP", "hadolint", "flake8"],
        "policy": "Block on HIGH/CRITICAL vulnerabilities"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
