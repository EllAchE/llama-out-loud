from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>tesing webhook receiver app</h1><p>This is a simple Flask application to receive webhooks.</p>"


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received data:", data)
    return jsonify({"status": "success", "message": "Data received"}), 200


if __name__ == '__main__':
    app.run(port=4040, debug=True)
