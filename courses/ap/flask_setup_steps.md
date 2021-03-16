You will need to choose whether you use Powershell or the Command Prompt.

*Note: if you cannot run `python` from the terminal. try reinstalling Python with "Change environment variables" checked.*

# Option 1 - Powershell 

1. Install Python with "Change environment variables" option
2. Open Powershell as administrator and run `Set-ExecutionPolicy Unrestricted`
3. Open VScode and create a new folder
4. Open the terminal (set it to Powershell if it is not already)
5. `python -m venv venv`
6. Activate the environment `.\venv\Scripts\activate`
7. pip install Flask
8. Create hello.py:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```

9. Create environment variables

```
env:FLASK_APP = "hello.py"
$env:FLASK_ENV = "development"
```

10. `flask run`

## Option 2 - Command Prompt

1. Install Python with "Change environment variables" option

3. Open VScode and create a new folder
4. Open the terminal and set the shell to Command Prompt
5. `python -m venv venv`
6. Activate the environment `.\venv\Scripts\activate`
7. pip install Flask
8. Create hello.py:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```

9. Create environment variables
```
set FLASK_APP=hello.py
set FLASK_ENV=development
```
10. `flask run`