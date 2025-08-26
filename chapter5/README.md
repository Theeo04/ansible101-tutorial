# Chapter 5

## 1️⃣ Cum funcționează handlers

Handler-ele sunt task-uri speciale care se execută doar dacă sunt notificate de un alt task. Ele sunt utile pentru operațiuni care trebuie efectuate doar atunci când anumite condiții sunt îndeplinite, cum ar fi repornirea unui serviciu după modificarea unui fișier de configurare.

### Caracteristici principale:
- Se execută la sfârșitul playbook-ului.
- Sunt declanșate o singură dată pentru fiecare host, chiar dacă sunt notificate de mai multe task-uri.

### Exemplu:

```yaml
handlers:
  - name: restart apache
    service:
      name: httpd
      state: restarted

tasks:
  - name: Deploy Apache configuration
    copy:
      src: /config/httpd.conf
      dest: /etc/httpd/conf/httpd.conf
    notify: restart apache
```

## 2️⃣ Ce se întâmplă dacă un task are o eroare?

Dacă un task care notifică un handler întâmpină o eroare și nu se finalizează cu succes, handler-ul nu va fi executat. Acest comportament previne modificări suplimentare care ar putea depinde de un task nereușit.

### Exemplu:

```yaml
tasks:
  - name: Deploy Apache configuration
    copy:
      src: /config/httpd.conf
      dest: /etc/httpd/conf/httpd.conf
    notify: restart apache
    when: false  # Simulăm o eroare

handlers:
  - name: restart apache
    service:
      name: httpd
      state: restarted
```

În acest caz, deoarece task-ul `Deploy Apache configuration` nu se execută (din cauza condiției `when: false`), handler-ul `restart apache` nu va fi notificat și nu va fi executat.

## 3️⃣ Cum putem executa un handler chiar dacă un task eșuează?

 - Ignore errors (nu recomand pentru producție):

```yaml
handlers:
  - name: restart myapp
    service:
      name: myapp
      state: restarted
    ignore_errors: yes
```

 - Rescue / block:

```yaml
tasks:
  - block:
      - name: Change config
        template:
          src: config.j2
          dest: /etc/myapp/config.conf
        notify: restart myapp
    rescue:
      - debug:
          msg: "Task failed, skipping handler"
```

- `failed_when` – poți decide când să consideri un handler ca fiind eșuat sau nu.