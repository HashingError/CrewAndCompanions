# CrewAndCompanions

### Step by Step setup guide
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
At this point you should be able to run project without tailwind and all it can bring to it. So to check if you are on a good track and all things server work try 
```
python manage.py runserver
```
and open http://127.0.0.1:8000/ in browser. It won't be glorious but it should work. 

To access mod panel (http://127.0.0.1:8000/admin), create admin account by running 
```
python manage.py createsuperuser
```
and following prompts.
