from flask import Flask
from steam import steam_bp

app = Flask(__name__)

@app.route('/')
def main():
    return "This is My API Service."

app.register_blueprint(steam_bp)