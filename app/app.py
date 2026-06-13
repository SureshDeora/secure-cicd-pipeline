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



# SECURE CODE (vulnerabilities fixed)

# FIX B105: Use environment variables instead of hardcoded passwords
import os
DB_PASSWORD = os.environ.get("DB_PASSWORD", "change-me")

# FIX B602: Use subprocess without shell=True
import subprocess


@app.route("/lookup")
def lookup():
    domain = "example.com"
    result = subprocess.run(
        ["nslookup", domain],
        capture_output=True,
        text=True
    )
    return jsonify({"result": result.stdout})


if __name__ == "__main__":
    # FIX B201: Never use debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=False)

