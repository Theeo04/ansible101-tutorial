# Intro to playbooks

This playbook is designed to automate the installation and configuration of the Apache HTTP server on all target hosts. It consists of three main tasks:

## Tasks Overview

1. **Install Apache package**:
   - This task ensures that the Apache HTTP server and its development package (`httpd` and `httpd-devel`) are installed on the target systems.
   - The `apt` module is used for package management, which ensures that the specified packages are in the `present` state (installed).

2. **Copy configuration files**:
   - This task copies the required Apache configuration files (`httpd.conf` and `httpd-vhosts.conf`) from the control node to the target systems.
   - The `copy` module is used to handle file transfers, setting the correct ownership (`root`), group (`root`), and file permissions (`0644`).

3. **Ensure Apache is running**:
   - This task ensures that the Apache HTTP server is started and configured to start automatically at boot.
   - The `service` module is used to manage the state of the Apache service (`httpd`), ensuring it is in the `started` state and `enabled` to start at boot.

## Explanation of `with_items`

The `with_items` directive is used to iterate over a list of items. In this playbook, it is used to copy multiple files by specifying a list of source (`src`) and destination (`dest`) pairs. Each item in the list represents a file to be copied and its target location.

Here is how `with_items` is structured in the playbook:

```yaml
with_items:
  - src: httpd.conf
    dest: /etc/httpd/conf/httpd.conf
  - src: httpd-vhosts.conf
    dest: /etc/httpd/conf.d/httpd-vhosts.conf
```

For each item in the list:
- `src` specifies the path to the source file on the control node.
- `dest` specifies the target path where the file will be copied on the managed node.

This approach avoids duplicating the `copy` task for each file, making the playbook more concise and easier to maintain.

### Apply this the playbook: 

```bash
ansible-playbook -i inventory playbook.yaml
```