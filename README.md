# AWS-Deployed-Web-App-with-Django
Requirements: 
* Python 3.7 or later
* pip
* virtualenv
* awscli & awsebcli

commands used:  
under project directory:  
python3 -m venv venv && source venv/bin/activate  
pip install django==4.1.3  
pip freeze > requirements.txt  
mkdir .ebextensions  

dango.config:  
option_settings:  
  aws:elasticbeanstalk:application:environment:  
    DJANGO_SETTINGS_MODULE: "mysite.settings"  
    PYTHONPATH: "/var/app/current:$PYTHONPATH"  
  aws:elasticbeanstalk:container:python:  
    WSGIPath: "mysite.wsgi:application"  

.ebignore:  
venv  

deactivate  
eb init -p python-3.11 django-tutorial  
eb create django-env
eb status
change allowed hosts to CNAME
eb deploy
eb open
