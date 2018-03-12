# Virtual Environments, PIP and Notebooks

## What is a virtual environment?
We all have different computers and some of those computers carry some baggage. Virtual environments allow us to start fresh which is pretty helpful if we are starting a new project working with teams.

## pip install all the things
If you don't have pip you will need to get it.
```
python get-pip.py
```
We will need to get this package before we can start using it.
```
pip install virtualenv
```

## Let's create a virtual environment
Let's play around with this environment and install some packages.
```
mkdir playing_with_virtualenvs
cd playing_with_virtualenvs
virtualenv first_env
source first_env/bin/activate
pip install jupyter
pip install ipython
pip install numpy
pip install pandas
pip freeze
pip freeze > requirements.txt
```
For windows
```
mkdir playing_with_virtualenvs
cd playing_with_virtualenvs
virtualenv first_env
source first_env/Scripts/activate
```

If you wanted to install a pre-made requirements.txt you do the following:
```
pip install -r requirements.txt in
```

## ipython
Let's check it out. And play around in it.
```
ipython
````

## Jupyter
Jupyter takes the concept to the next level by allowing an environment where you can play around in this interactive environment.
```
jupyter notebook
```

## datetime example
```
import datetime

time = datetime.datetime.now()

def greeting(time):
  name = 'Jess'
  print('Hello {}, the time is {}'.format(name, time))

greeting(time=time)
```

## How to close a virtual environment
```
deactivate
```

## Resources
- [User guide if you are having trouble with windows](https://virtualenv.pypa.io/en/stable/userguide/)
- [How to get pip](https://pip.pypa.io/en/stable/installing/)
