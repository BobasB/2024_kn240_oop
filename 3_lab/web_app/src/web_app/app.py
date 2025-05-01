from flask import Flask
from redis import Redis

app = Flask(__name__)
r = Redis(host='localhost', port=6379, db=0)
C = 0

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/info")
def info():
    C += 1
    r.set("info_count", C)
    return f"Інкрементуємо значення до {C}"

if __name__ == "__main__":
    # Runs the app on localhost at port 5000 in debug mode
    app.run(host="127.0.0.1", port=5000, debug=True)