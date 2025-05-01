from flask import Flask
from redis import Redis

app = Flask(__name__)
r = Redis(host='localhost', port=6379, db=0)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/info")
def info():
    C = r.incr("info_count")
    return f"Інкрементуємо значення до {C}"

@app.route("/del")
def del_info():
    C = r.decr("info_count")
    return f"Декрементуємо значення до {C}"

if __name__ == "__main__":
    # Runs the app on localhost at port 5000 in debug mode
    app.run(host="localhost", port=5000, debug=True)