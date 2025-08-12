from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return "This is My API Service."