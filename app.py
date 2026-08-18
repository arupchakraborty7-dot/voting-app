from flask import Flask, jsonify, request

votes = {} #in-memory store:{"Alice":3, "Bob":1}

app = Flask(__name__)

# Decorator
@app.route("/")

def home():
    return "Welcome th the App"

# Check App health status
@app.route("/health")

def health():
    return "App is running"

# Vote name and count
@app.route("/vote/<name>")
def vote(name):
    votes[name] = votes.get(name, 0) + 1
    return f"Vote recorded for {name}. Total votes: {votes[name]}"
# Result on votes
@app.route("/results")
def results():
    return jsonify(votes)

if __name__ == "__main__":
    app.run(debug=True)
