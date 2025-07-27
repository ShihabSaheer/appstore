This is a containerized web application built to demonstrate a minimal web server with Prometheus metrics integration. It supports deployment on Google Kubernetes Engine (GKE) with infrastructure provisioned via Terraform and configuration managed using Ansible.

I chose Flask for its simplicity in building lightweight web services, Docker to containerize the app for consistent deployment, Prometheus to monitor request metrics, Kubernetes for orchestrating containers at scale, Terraform to provision cloud infrastructure declaratively, Ansible to automate Prometheus setup on the VM, and GCP for its reliable managed services — all combined to ensure a portable, observable, and production-ready web application.

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

**Run Application Locally**
```
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

Open your browser at the below url to see the pages created:
- http://localhost/gandalf
- http://localhost/colombo
- http://localhost/metrics
```

### Run application with Docker
```
# To build the docker image
docker build -t local-gandalf-app .
# To run the detached container
docker run -d -p 80:80 local-gandalf-app

The container can be accessed from http:localhost
```

**Cloud Deployment (GCP + Kubernetes + Prometheus)**
Prerequisites
- GCP Project with billing enabled
- gcloud, kubectl, terraform, ansible, docker installed
- SSH keys generated at ~/.ssh/id_rsa.pub

 Step 1: Configure Terraform
 - terraform.tfvars
   - project_id      = "your-gcp-project-id" - provide the GCP Project ID
   - ssh_user        = "your-ssh-user" - The SSH username
   - public_key_path = "~/.ssh/id_rsa.pub" - The Public RSA key path

Step 2: Deploy Infra with Terraform
  - terraform init
  - terraform apply

Step 3: Connect kubectl to GKE
  - gcloud container clusters get-credentials appstore-cluster --zone <zone> --project <project_id>

Step 4: Deploy App to Kubernetes
  - kubectl apply -f k8s/
  
Step 5: Access the App
  - kubectl get svc appstore
    - http://loadbalancer/gandalf
    - http://loadbalancer/colombo
    - http://loadbalancer/metrics

Step 6: Install Prometheus via Ansible
  - Update inventory.ini with Prometheus VM IP  
    <VM_PUBLIC_IP> ansible_user=your-ssh-user ansible_ssh_private_key_file=~/.ssh/id_rsa - The <VM_PUBLIC_IP> can be taken once it is created with terraform.

 - Once the VM IP is updated then run the ansible playbook to install Prometheus inside the VM
   - ansible-playbook -i inventory.ini playbook.yml

Step 7: Access Prometheus UI
  - http://<VM_PUBLIC_IP>:9090 - The VM can be accessed with Public IP cretead for the VM.

Below queries can be used to fetch Query metrics:
- gandalf_requests_total
- colombo_requests_total

The below job is scheduled and configured to scrape the app on port 80:
```
 - job_name: "appstore_metrics"
    static_configs:
      - targets: ["flask-app:80"]
        labels:
          app: "appstore"
```
Ensure the DNS name or service name matches your deployment.

Screenshots for reference:

**/**
<img width="1918" height="950" alt="image" src="https://github.com/user-attachments/assets/1604d530-f4d7-427a-b97a-73f47fa7c7c7" />

**/gandalf**
<img width="1897" height="962" alt="image" src="https://github.com/user-attachments/assets/d0a42860-219f-4695-baa6-8b65499b5166" />

**/colombo**
<img width="1918" height="883" alt="image" src="https://github.com/user-attachments/assets/5769da16-977f-4f47-810d-437f65f35f44" />

**/metrics**
<img width="1918" height="956" alt="image" src="https://github.com/user-attachments/assets/80d9747d-57da-4e39-846e-8d312e5b210d" />

**Prometheus UI to query metrics:**
<img width="1918" height="691" alt="image" src="https://github.com/user-attachments/assets/2ad059b6-fee7-4e8d-ad45-61648f31c3d5" />








