from flask import Flask
import os

app = Flask(__name__)

ENV = os.getenv("ENVIRONMENT", "development")

@app.route("/")
def home():
    return f"DevOps Flask App Running in {ENV} environment"

@app.route("/health")
def health():
    return {"status": "OK"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)