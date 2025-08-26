# Chapter 4: Installing and Configuring Solr with Ansible

This chapter demonstrates how to automate the installation and configuration of Apache Solr using Ansible. Solr is a powerful search platform used for indexing and searching large datasets.

---

## Playbook Overview

The `main.yaml` playbook automates the following tasks:

1. **Install Java**: Installs the Java runtime environment required by Solr.
2. **Download Solr**: Downloads the specified version of Solr from the Apache archive.
3. **Extract Solr**: Unarchives the Solr tarball to the specified directory.
4. **Run Installation Script**: Executes the Solr installation script to set up Solr as a service.
5. **Start Solr Service**: Ensures the Solr service is started and enabled to run at boot.

---

## Modules Used in the Playbook

### 1. `apt` Module
The `apt` module is used to manage packages on Debian-based systems.

#### Example:
```yaml
- name: Install Java
  apt:
    name: openjdk-11-jre
    state: present
```

#### Explanation:
- `name`: Specifies the package to install (e.g., `openjdk-11-jre`).
- `state`: Ensures the package is `present` (installed). Other options include `absent` (uninstalled).

---

### 2. `get_url` Module
The `get_url` module is used to download files from a URL to a specified location.

#### Example:
```yaml
- name: Download Solr
  get_url:
    url: "https://archive.apache.org/dist/lucene/solr/{{ solr_version }}/solr-{{ solr_version }}.tgz"
    dest: "{{ download_dir }}/solr-{{ solr_version }}.tgz"
    checksum: "{{ solr_checksum }}"
```

#### Explanation:
- `url`: The URL of the file to download.
- `dest`: The destination path where the file will be saved.
- `checksum`: Verifies the integrity of the downloaded file using the provided checksum.

---

### 3. `unarchive` Module
The `unarchive` module is used to extract archive files (e.g., `.tar.gz`).

#### Example:
```yaml
- name: Create Solr directory
  unarchive:
    src: "{{ download_dir }}/solr-{{ solr_version }}.tgz"
    dest: "{{ solr_dir }}"
    remote_src: yes
    creates: "{{ solr_dir }}/README.md"
```

#### Explanation:
- `src`: The path to the archive file to extract.
- `dest`: The directory where the archive will be extracted.
- `remote_src`: Set to `yes` if the archive is already on the remote machine.
- `creates`: Skips extraction if the specified file or directory already exists.

---

### 4. `command` Module
The `command` module is used to run commands on the remote machine.

#### Example:
```yaml
- name: Run Solr installation script
  command: >
    {{ solr_dir }}/solr-{{ solr_version }}/bin/install_solr_service.sh
    {{ solr_dir }}/solr-{{ solr_version }}.tgz
    -i /opt
    -d /var/solr
    -u solr
    -s solr
    -p 8983
  creates: "{{ solr_dir }}/bin/solr"
```

#### Explanation:
- The command runs the Solr installation script with various options:
  - `-i`: Installation directory.
  - `-d`: Data directory for Solr.
  - `-u`: User to run the Solr service.
  - `-s`: Service name.
  - `-p`: Port number.
- `creates`: Skips the command if the specified file or directory already exists.

---

### 5. `service` Module
The `service` module is used to manage services on the remote machine.

#### Example:
```yaml
- name: Ensure Solr service is enabled and started
  service:
    name: solr
    state: started
    enabled: yes
```

#### Explanation:
- `name`: The name of the service to manage (e.g., `solr`).
- `state`: Ensures the service is `started`. Other options include `stopped` and `restarted`.
- `enabled`: Ensures the service is enabled to start at boot.

---

## Variables

The `vars.yaml` file defines important variables used in the playbook:

- `download_dir`: Directory where the Solr tarball will be downloaded.
- `solr_dir`: Directory where Solr will be installed.
- `solr_version`: Version of Solr to install.
- `solr_checksum`: Checksum to verify the integrity of the downloaded Solr tarball.

---

## Troubleshooting

- **Checksum Mismatch**: If the checksum verification fails, ensure the `solr_checksum` in `vars.yaml` matches the checksum of the downloaded file.
- **Service Issues**: If the Solr service fails to start, check the logs in `/var/solr/logs/`.

---

## Learn More

- [Apache Solr Documentation](https://solr.apache.org/)
- [Ansible Documentation](https://docs.ansible.com/)

---

## How to Use

### Step 1: Test the Playbook Syntax
Before running the playbook, check for syntax errors:
```bash
ansible-playbook -i inventory main.yaml --syntax-check
```

### Step 2: Run the Playbook
Run the playbook to install and configure Solr:
```bash
ansible-playbook -i inventory main.yaml
```


Happy automating!