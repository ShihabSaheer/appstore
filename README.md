This is a containerized web application built to demonstrate a minimal web server with Prometheus metrics integration. It supports deployment on Google Kubernetes Engine (GKE) with infrastructure provisioned via Terraform and configuration managed using Ansible.

- 🌐 Web endpoints:
- `/gandalf`: Displays an image of Gandalf with a message.
- `/colombo`: Shows the current time in Colombo, Sri Lanka.
- `/metrics`: Exposes Prometheus-compatible metrics.
- Dockerized for containerized environments.
- Kubernetes manifests for deployment on GKE.
- Infrastructure automation using **Terraform** and **Ansible**.
- Prometheus-based monitoring of application endpoints.

The tech stack used:
- **Backend:** Python 3.10, Flask
- **Monitoring:** Prometheus, Prometheus Python client
- **Infrastructure as Code:** Terraform (GCP), Ansible (Debian VM setup)
- **Deployment:** Docker, Kubernetes (GKE)
- **Cloud:** Google Cloud Platform (GKE + Compute Engine)

**Project Structure**


appstore/
├── Dockerfile
├── app.py
├── requirements.txt
├── templates/
│   └── gandalf.html
├── static/
│   └── gandalf.jpg
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── infra/
│ ├── terraform/ 
│ │ ├── main.tf
│ │ ├── variables.tf
│ │ └── terraform.tfvars
│ └── ansible/ 
│ ├── inventory.ini
│ └── playbook.yml

**Architecture Flow**
<img width="1536" height="1024" alt="ChatGPT Image Jul 27, 2025, 02_25_20 PM" src="https://github.com/user-attachments/assets/02f85c6a-4eb3-475e-8c14-818213d1ae84" />

### ✅ Prerequisites

- GCP project with billing enabled
- Google Cloud SDK (`gcloud`) installed and authenticated
- `Terraform`, `kubectl`, `Docker`, and `Ansible` installed
- SSH key pair at `~/.ssh/id_rsa` and `~/.ssh/id_rsa.pub`

Follow the below steps to run the application in the local

## Local Setup (for Testing)

### ✅ Requirements

- Python 3.10+
- `pip` (Python package manager)

**Run Python Locally**
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

Open your browser at the below url to see the pages created:
http://localhost/gandalf
http://localhost/colombo
http://localhost/metrics

### Run Locally with Docker
# To build the docker image
docker build -t local-gandalf-app .
# To run the detached container
docker run -d -p 80:80 local-gandalf-app

The container can be accessed from http:localhost
