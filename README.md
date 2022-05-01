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
5. Start server  
```bash
python manage.py runserver
```  
5. Create your admin user  
```bash
django-admin createsuperuser
```  
This would tell you whats your usernamr, email and password
6. Enter the site in your chrome url "http://127.0.0.1:8000"  


7. Enter the admin path to see your models and the stuff in the DB now "http://127.0.0.1:8000/admin/"  


8. Start playing with "clients" screen on "http://127.0.0.1:8000/clients/"
 
