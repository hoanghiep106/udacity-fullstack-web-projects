# Blog app

## Demo
https://udacity-202010.appspot.com

## How to install

1. Download Python 2

https://www.python.org/downloads/

2. Install Google App Engine SDK for Python 

https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python

3. Create a virtual enviroment

In the course2 directory run

```
virtualenv -p /home/username/opt/python-2.7.7/bin/python blog
```

4. Install dependencies

```
pip install -r requirements.txt
```

5. Run app in development env

```
dev_appserver.py
```

6. Deploy

```
gcloud app deploy
```
