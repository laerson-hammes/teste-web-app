from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def index():
    referrer = request.referrer
    data = ''
    if referrer:
        data = referrer
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
