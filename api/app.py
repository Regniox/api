from flask import Flask
from steam import steam_bp
from deepseek import deepseek_bp

app = Flask(__name__)

@app.route('/')
def main():
    return "This is My API Service."

app.register_blueprint(steam_bp)
app.register_blueprint(deepseek_bp)

if __name__ == '__main__':
    app.run(debug=True)