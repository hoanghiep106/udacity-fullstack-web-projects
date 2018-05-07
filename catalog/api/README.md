# Catalog project.

### Prerequisite
- Python2

https://www.python.org/downloads/

- Virtualenv
```
pip install virtualenv
```

### Install the project

- Create a virtual environment inside the project
```
virtualenv --python=python2.7 venv
```

- Start the virtual environment
```
source venv/bin/activate
```
Can also stop by:
```
deactivate
```

- Install dependencies:
```
pip install -r requirements.txt
```

- Start the project:
```
python app.py
```

- Access http://localhost:5001