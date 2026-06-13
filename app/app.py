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


# INTENTIONALLY VULNERABLE CODE (for Bandit demo)
# Let's see if this code is caught by the SAST scanner


# B105: Hardcoded password (Bandit will flag this)
DB_PASSWORD = "super_secret_password_123"

# B602: Shell injection risk (Bandit will flag this)
import subprocess


@app.route("/lookup")
def lookup():
    domain = "example.com"
    result = subprocess.call(f"nslookup {domain}", shell=True)
    return jsonify({"result": str(result)})


if __name__ == "__main__":
    # B201: Running Flask in debug mode (Bandit will flag this)
    app.run(host="0.0.0.0", port=5000, debug=True)

