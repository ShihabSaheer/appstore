provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

resource "google_container_cluster" "gke" {
  name     = "appstore-cluster"
  location = var.zone

  initial_node_count = 1
  node_config {
    machine_type = "e2-medium"
  }
}

resource "google_compute_instance" "prometheus_vm" {
  name         = "prometheus-vm"
  machine_type = "e2-medium"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}
  }

  metadata = {
    ssh-keys = "${var.ssh_user}:${file(var.public_key_path)}"
  }

  tags = ["prometheus"]
}

output "prometheus_ip" {
  value = google_compute_instance.prometheus_vm.network_interface[0].access_config[0].nat_ip
}
