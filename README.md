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
Follow [full tutorial](https://timonweb.com/django/https-django-development-server-ssl-certificate/) __*just step 1 !*__  
Or use these commands in your terminal (for linux, if you use windows enter the link, if you use Mac just run the last command). 

```bash
sudo apt install libnss3-tools
```  
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```  
```bash
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/user/.profile
```  
```bash
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"$ euxbrew/bin/brew shellenv)"' >> /home/usecho 'eval "$(/home/linuxbrew/.linu
```  
```bash
sudo apt-get install build-essential
```  
```bash
brew install gcc
```  
```bash
brew install mkcert
```


7. Start the https server  
```bash
python manage.py runserver_plus --cert-file cert.pem --key-file key.pem
```  

8. Enter the site in your chrome url "https://127.0.0.1:8000"  


9. Enter the admin path to see your models and the stuff in the DB now "https://127.0.0.1:8000/admin/"  


10. After registration, start playing with "clients" screen on "https://127.0.0.1:8000/clients/"
 
