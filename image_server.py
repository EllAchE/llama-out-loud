from flask import Flask, request
app = Flask(__name__)

@app.route('/post', methods=['POST'])
def receive_data():
    data = request.get_json()
    print(data)
    # Process the data here
    return 'Data received', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
