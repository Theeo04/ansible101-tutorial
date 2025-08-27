# Load Balancer + Appservers with Ansible & Vagrant

Acest proiect demonstrează configurarea unui mediu simplu de producție folosind Vagrant + Ansible:

- 2 servere aplicație (app1, app2) cu Nginx instalat și configurat.
- 1 server Load Balancer (lb) cu HAProxy, care face round-robin între cele două appservers.

### Structure

- Link: https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html#use-dynamic-inventory-with-clouds 
- Layout: Alternative Directory Layout

# Rulare:

- Pornire VM-uri:

```bash
vagrant up
```

- Rulare Playbook:

```bash
/LB_Ansible-Configuration$ ansible-playbook -i inventory/inventory playbooks/main.yaml
```

- Accesează load balancer-ul:
```bash
curl http://192.168.56.10/
```

### Note

- Variabile comune sunt definite în inventory/group_vars/
- Variabile specifice fiecărui host sunt în host_vars/
- Roles-urile (nginx_app, lb) sunt independente și pot fi reutilizate în alte proiecte