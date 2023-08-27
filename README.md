# CrewAndCompanions

Step by Step setup guide
I will be using bash commands so if you are working on Windows I suggest using Git Bash (https://git-scm.com/downloads). 

Install python 3.11 on your machine.

Open project folder command line and create virtual environment. 

```
python -m venv env
```

Activate your virtual environment.
```
source env/Scripts/activate
```
Next you will need to install django. 
```
pip install django
```
After short break for drinking etc. you will need to install tailwind. (It requires node to work so please install it before hand and goodspeed with that.
```
pip install django-tailwind[reload]
```
At this point you should be able to run project without tailwind and all it can bring to it. So to check if you are on a good track and all things server work try 
```
python manage.py runserver
```
and open http://127.0.0.1:8000/ in browser. It wont be glorious but it should work. 

To access mod panel (http://127.0.0.1:8000/admin), create admin account by running 
```
python manage.py createsuperuser
```
and following prompts.

Run command
```
python manage.py tailwind install
```
to install tailwind dependencies. 

And we are almost done. Open second command line tab to run tailwind server
```
python manage.py tailwind start
```
and you can run your django project in first tab with
```
python manage.py runserver
```
