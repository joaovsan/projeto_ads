from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'API online!'})

if __name__ == '__main__':
    app.run()
