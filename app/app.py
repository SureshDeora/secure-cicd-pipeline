from flask import Flask, jsonify
import os
import subprocess

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


# FIX B105: Use environment variables instead of hardcoded passwords
DB_PASSWORD = os.environ.get("DB_PASSWORD", "change-me")


@app.route("/lookup")
def lookup():
    domain = "example.com"
    # FIX B602: Use subprocess.run without shell=True
    result = subprocess.run(
        ["nslookup", domain],
        capture_output=True,
        text=True
    )
    return jsonify({"result": result.stdout})


if __name__ == "__main__":
    # FIX B201: debug=False for production
    # FIX B104: nosec tells Bandit to ignore binding to 0.0.0.0 (required for Docker)
    app.run(host="0.0.0.0", port=5000, debug=False)  # nosec B104
