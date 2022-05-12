# Computer Security Project - Communication LTD  
### Description:  
This is a fictional company's site that handles customers data packages for several sectors.  
This site also manages users and permissions.  

### How to start:  
1. Clone this project  
```bash
git clone {THIS PROJECTS HTTPS PATH}
```  


2. Enter communicationLTD project dir  
```bash
cd communicationLTD
```  


3. Install all this project packages (dont worry if postgreSQL gives you errors for the meantime)  
```bash
pip install -r requirements.txt
```  


4. Run this project migrations to the DB on the SQLite3 temp django DB  
```bash
python manage.py migrate
```  


5. Create your admin user. This would tell you what's your username, email and password.  
```bash
django-admin createsuperuser
``` 


6. Installing package to run https self-signed certificate:  
   Here is how to install mkcert, you can choose to install any SSL you'd like on your computer.  
Follow [full tutorial](https://medium.com/@millienakiganda/creating-an-ssl-certificate-for-localhost-in-django-framework-45290d905b88)  


7. Start the https server  
```bash
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```  


8. Enter the site in your chrome url "https://127.0.0.1:8000"  


9. You can test your TLS connection version with openssl cli tool with the folowing command  
```bash
openssl s_client -connect 127.0.0.1:8000
```  
The version is shown:  
```bash
...
Post-Handshake New Session Ticket arrived:
SSL-Session:
    Protocol  : TLSv1.3
    Cipher    : TLS_AES_256_GCM_SHA384
...
```  

10. Enter the admin path to see your models and the stuff in the DB now "https://127.0.0.1:8000/admin/"  


11. After registration, start playing with "clients" screen on "https://127.0.0.1:8000/clients/"  


12. If you are trying Max login attempts, you'll need to release your user/ip, for this studing purposes use:  
```bash  
python manage.py axes_reset_ip ip 127.0.0.1
```
