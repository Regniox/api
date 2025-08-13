from flask import Flask
from flask_cors import CORS
from .steam import steam_bp
from .deepseek import deepseek_bp
from .cnblogs import cnblogs_bp

app = Flask(__name__)

@app.route('/')
def main():
    return "This is My API Service."

app.register_blueprint(steam_bp)
app.register_blueprint(deepseek_bp)
app.register_blueprint(cnblogs_bp)

CORS(app)