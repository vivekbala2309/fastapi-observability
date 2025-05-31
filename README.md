# FastAPI Server Monitoring

A simple, production-ready FastAPI HTTP server with basic endpoints (GET, POST, PUT) and Prometheus metrics support.  
The app is Dockerized for easy deployment and designed to work with Prometheus and Grafana for observability, especially in Kubernetes environments like Minikube.

---

## Features

- Basic API endpoints:
  - `GET /` — returns confirmation message  
  - `POST /submit` — returns confirmation message  
  - `PUT /update` — returns confirmation message  
- Prometheus metrics exposed on `/metrics`  
- Dockerfile included for containerization  
- Clean, modular project structure  

---

## Project Structure

fastapi-server/
├── app/
│ ├── init.py
│ ├── main.py # App entrypoint, starts FastAPI server
│ ├── metrics.py # Prometheus metrics setup
│ └── routes/
│ ├── init.py
│ └── basic.py # API route definitions
├── requirements.txt # Python dependencies
├── Dockerfile # Docker build instructions
├── .gitignore # Files/folders to ignore in git
└── README.md # Project documentation (you’re reading it!)


---

## Getting Started

### Prerequisites

- Python 3.9 or higher  
- Docker (for containerization)  
- (Optional) Minikube, kubectl for Kubernetes deployment and monitoring  

### Setup Locally

```bash
git clone https://github.com/vivekbala2309/fastapi-server-monitoring.git
cd fastapi-server-monitoring

# Create and activate virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run FastAPI server
uvicorn app.main:app --reload


Open your browser at http://localhost:8000 — you should see the API working.

Docker Usage
To build and run your FastAPI app inside Docker:

docker build -t fastapi-server .
docker run -p 8000:8000 fastapi-server
The server will be accessible at http://localhost:8000.

Minikube
https://minikube.sigs.k8s.io/docs/start/?arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download


https://hub.docker.com/repositories/vivekbala2903


Push images to docker hub repo
docker login
docker images
docker tag fastapi-server:latest vivekbala2903/fastapi-app:latest
docker push vivekbala2903/fastapi-app:latest

1. Create a file deployment.yaml with this content:
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-deployment
spec:
  replicas: 2
  selector:
    matchLabels:
      app: fastapi-app
  template:
    metadata:
      labels:
        app: fastapi-app
    spec:
      containers:
      - name: fastapi-container
        image: vivekbala2903/fastapi-app:latest  # Your Docker Hub image
        ports:
        - containerPort: 8000

2. Create a file service.yaml to expose the app:
apiVersion: v1
kind: Service
metadata:
  name: fastapi-service
spec:
  type: NodePort                  # exposes on a node port (accessible from localhost in Minikube)
  selector:
    app: fastapi-app
  ports:
  - protocol: TCP
    port: 80                     # Port to expose inside the cluster
    targetPort: 8000             # Container port your app listens on
    nodePort: 30080              # Port to access on the Minikube host


minikube service fastapi-service --url

PS C:\Users\nithy> minikube ssh
docker@minikube:~$ docker login



Prometheus Metrics
Your app exposes metrics at http://localhost:8000/metrics in the Prometheus format.
This endpoint can be scraped by Prometheus to collect HTTP request data.

Monitoring with Grafana
You can deploy Prometheus and Grafana on Minikube and connect Grafana dashboards to the Prometheus metrics endpoint for observability.
This repo is ready for such deployments (future work or separate manifests needed).



Author
Vivek B 


