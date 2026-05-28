import requests
from flask import Flask
import yaml

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from frogbot-oidc-test"

if __name__ == '__main__':
    app.run()
