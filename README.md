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

5. Create your admin user  
```bash
django-admin createsuperuser
```  
This would tell you what's your username, email and password
6. Install mkcert package to run https self-signed certificate.  
Follow [this](https://timonweb.com/django/https-django-development-server-ssl-certificate/) tutorial __*just step 1 !*__  

7. Start the https server  
```bash
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```  

8. Enter the site in your chrome url "https://127.0.0.1:8000"  


9. Enter the admin path to see your models and the stuff in the DB now "https://127.0.0.1:8000/admin/"  


10. After registration, start playing with "clients" screen on "https://127.0.0.1:8000/clients/"
 
