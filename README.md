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

Prometheus Metrics
Your app exposes metrics at http://localhost:8000/metrics in the Prometheus format.
This endpoint can be scraped by Prometheus to collect HTTP request data.

Monitoring with Grafana
You can deploy Prometheus and Grafana on Minikube and connect Grafana dashboards to the Prometheus metrics endpoint for observability.
This repo is ready for such deployments (future work or separate manifests needed).



Author
Vivek B 


