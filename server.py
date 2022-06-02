from flask import Flask, jsonify, request
from threading import Thread

app = Flask('')

@app.route('/', methods = ['GET'])
def main():
    return jsonify({"status": "online"})

def run():
    app.run(host='0.0.0.0', port='80')

def keep_alive():
    t = Thread(target=run)
    t.start()