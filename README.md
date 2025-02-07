---

# **Flask Microservices on Virtual Machines**  

This repository contains two Flask-based microservices designed to run on separate Virtual Machines (VMs). Each microservice provides basic API endpoints and communicates over a network using a bridged adapter.  

## **Microservices Overview**  

1. **Microservice 1 (VM1)**
   - Runs on **port 5000**
   - Provides a basic greeting and a multiplication API  
   - [Source Code](https://github.com/mrpritesh45/microservices-vm-deployment/blob/main/microservice1.py)  

2. **Microservice 2 (VM2)**
   - Runs on **port 5001**
   - Provides similar functionality but runs independently on another VM  
   - [Source Code](https://github.com/mrpritesh45/microservices-vm-deployment/blob/main/microservice2.py)  

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
- Download and save [microservice1.py](https://github.com/mrpritesh45/microservices-vm-deployment/blob/main/microservice1.py).  
- Start the microservice:  
  ```bash
  python3 microservice1.py
  ```

#### **On VM2 (192.168.0.109)**
- Download and save [microservice2.py](https://github.com/mrpritesh45/microservices-vm-deployment/blob/main/microservice2.py).  
- Start the microservice:  
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
