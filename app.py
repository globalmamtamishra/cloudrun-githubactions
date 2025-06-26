from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, You’re fighting through pixels with me, so sit and rest, you are doing fine!"

if __name__ == "__main__":
    app.run(debug=True, port=8000)
