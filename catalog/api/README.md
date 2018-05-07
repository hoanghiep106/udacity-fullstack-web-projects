# Catalog project.

### Prerequisite
- Python3

https://www.python.org/downloads/

- Virtualenv
```
pip install virtualenv
```

### Install the project

- Create a virtual environment inside the project
```
virtualenv -p python3 venv
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