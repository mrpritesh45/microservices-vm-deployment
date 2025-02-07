from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_vm2():
    return "Hello from VM2!"

@app.route("/multiply/<int:a>/<int:b>")
def multiply_vm2(a, b):
    result = a * b
    return f"Result (From VM2) of {a} x {b} = {result}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
