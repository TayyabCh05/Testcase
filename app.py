from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello mister: Why are you so cute'
if __name__ == "__main__":
    app.run()
