
from flask import Flask, request, jsonify

def create_app():
    app = Flask(__name__)

    @app.route("/add_format", methods=["POST"])
    def handle_generate():
        result = request.json.get("result")

        return jsonify({
            "result": str(result)
        })

    @app.route("/ping", methods=["GET"])
    def handle_ping():
        return "pong_format"

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)