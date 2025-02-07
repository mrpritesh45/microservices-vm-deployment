from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_vm1():
    return "Hello from VM1!"

@app.route("/multiply/<int:a>/<int:b>")
def multiply_vm1(a, b):
    result = a * b
    return f"Result (From VM1) of {a} x {b} = {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
