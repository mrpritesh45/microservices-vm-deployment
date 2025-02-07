# **Flask Microservices on Virtual Machines**  

This repository contains two Flask-based microservices designed to run on separate Virtual Machines (VMs). Each microservice provides basic API endpoints and communicates over a network using a bridged adapter.  

## **Microservices Overview**  

1. **Microservice 1 (VM1)**
   - Runs on **port 5000**
   - Provides a basic greeting and a multiplication API  

2. **Microservice 2 (VM2)**
   - Runs on **port 5001**
   - Provides similar functionality but runs independently on another VM  

## **Endpoints**  

| Method | URL | Description |
|--------|-----|------------|
| GET | `/` | Returns a greeting message from the respective VM |
| GET | `/multiply/<a>/<b>` | Multiplies two numbers and returns the result |

## **Setup & Usage**  

### **1. Install Dependencies**  
Run the following commands on **both VMs**:  
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip -y
python3 -m venv vmenv
source vmenv/bin/activate
pip install flask
```

### **2. Create and Run Microservices**  

#### **On VM1 (192.168.0.114)**
Create `microservice1.py`:  
```python
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
```
Run the microservice:  
```bash
python3 microservice1.py
```

#### **On VM2 (192.168.0.109)**
Create `microservice2.py`:  
```python
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
```
Run the microservice:  
```bash
python3 microservice2.py
```

## **Testing the Microservices**  

### **From VM1 (Test VM2’s Service)**
```bash
curl 192.168.0.109:5001
curl 192.168.0.109:5001/multiply/4/7
```

### **From VM2 (Test VM1’s Service)**
```bash
curl 192.168.0.114:5000
curl 192.168.0.114:5000/multiply/4/6
```

## **Future Enhancements**  
- Containerizing the microservices using **Docker**  
- Implementing **inter-service communication**  
- Adding **logging and monitoring**  

---
