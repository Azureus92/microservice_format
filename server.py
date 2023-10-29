from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def handle_generate():
    a = request.json.get("a")
    b = request.json.get("b")

    return jsonify({
        "result": a+b
    })

@app.route("/ping", methods=["GET"])
def handle_ping():
    return "pong"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)