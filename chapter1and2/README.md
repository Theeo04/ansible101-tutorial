# Commands used ad-hoc + inventory:

```
ansible multi -i inventory -a "hostname" # Paralelism
ansible multi -i inventory -a "hostname" -f 1 # In order 
ansible -i inventory db -m setup # Info about the servers
ansible -i inventory multi -b -m apt -a "name=ntp state=present" # -b ruleaza ca sudo; -m modul, -a argumentele modului
```