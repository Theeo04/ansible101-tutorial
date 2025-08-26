# Ansible 101: Automating Server Configuration

Welcome to the Ansible 101 project! This repository contains Ansible playbooks and configurations to help you automate server setup and application deployment. Whether you're new to Ansible or looking to expand your automation skills, this project is designed to be beginner-friendly.

---

## What is Ansible?

Ansible is an open-source automation tool that simplifies IT tasks like configuration management, application deployment, and orchestration. It uses YAML files (called playbooks) to describe the desired state of your systems.

---

## Project Structure

Here’s an overview of the key files and directories in this project:

- **chapter3/**: Contains playbooks for setting up and configuring Apache HTTP server.
  - `inventory`: Defines the servers (hosts) Ansible will manage.
  - `playbook.yaml`: Automates the installation and configuration of Apache.
  - `README.md`: Explains the playbook tasks in detail.

- **chapter4/**: Contains playbooks for installing and configuring Solr.
  - `vars.yaml`: Defines variables like Solr version and installation paths.
  - `main.yaml`: Automates the installation of Solr.
  - `README.md`: Provides instructions for running the Solr playbook.

---

## Prerequisites

Before running the playbooks, ensure you have the following:

1. **Ansible Installed**: Install Ansible on your control node (your local machine or a server).
   ```bash
   sudo apt update
   sudo apt install ansible
   ```

2. **Vagrant Installed**: Install Vagrant to manage virtual machines.
   ```bash
   sudo apt install vagrant
   ```

3. **VirtualBox Installed**: Install VirtualBox as the provider for Vagrant.
   ```bash
   sudo apt install virtualbox
   ```

4. **SSH Access**: Ensure you can SSH into the target servers using the private key specified in the inventory file.

---

## How to Use

### Step 1: Set Up Virtual Machines
Use the `Vagrantfile` in `chapter4/` to create virtual machines for testing:
```bash
cd chapter4
vagrant up
```

### Step 2: Run the Apache Playbook
Navigate to the `chapter3/` directory and run the playbook to install and configure Apache:
```bash
cd ../chapter3
ansible-playbook -i inventory playbook.yaml
```

### Step 3: Run the Solr Playbook
Navigate to the `chapter4/` directory and run the playbook to install and configure Solr:
```bash
cd ../chapter4
ansible-playbook -i inventory main.yaml
```

---

## Testing Your Playbooks

You can test your playbooks for syntax errors before running them:
```bash
ansible-playbook -i inventory playbook.yaml --syntax-check
ansible-playbook -i inventory main.yaml --syntax-check
```

---

## Key Concepts for Beginners

1. **Inventory File**: Lists the servers Ansible will manage. Example:
   ```ini
   [app]
   192.168.60.4
   192.168.60.5
   ```

2. **Playbook**: A YAML file that describes the tasks Ansible will perform. Example:
   ```yaml
   - name: Install Apache
     hosts: all
     tasks:
       - name: Install Apache package
         apt:
           name: httpd
           state: present
   ```

3. **Variables**: Store reusable values like file paths or versions. Example:
   ```yaml
   solr_version: 8.5.0
   ```

---

## Troubleshooting

- **SSH Errors**: If you encounter SSH errors, ensure the private key path in the inventory file is correct.
- **Host Key Verification**: If you see a host key verification error, run:
  ```bash
  ssh-keygen -f ~/.ssh/known_hosts -R <IP_ADDRESS>
  ```

---

## Learn More

- [Ansible Documentation](https://docs.ansible.com/)
- [Vagrant Documentation](https://www.vagrantup.com/docs)
- [VirtualBox Documentation](https://www.virtualbox.org/manual/)

Happy automating!
