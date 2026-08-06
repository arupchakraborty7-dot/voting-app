from flask import Flask, jsonify, request

app = Flask(__name__)

# Decorator
@app.route("/")

def home():
    return "Welcome th the App"

# Check App health status
@app.route("/health")

def health():
    return "App is running"

if __name__ == "__main__":
    app.run(debug=True)