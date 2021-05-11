You will need to choose whether you use Powershell or the Command Prompt.

*Note: if you cannot run `python` from the terminal. try reinstalling Python with "Change environment variables" checked.*

*Note2: If you call your virtual environment .venv as outlined below, VSCode may notice the new virtual environment and ask you if you want to use it in your workspace.  You can say yes, and if you create a new Terminal, it may automatically activate the virtual environment for you.

# Option 1 - Powershell 

1. Install Python with "Change environment variables" option
2. Open Powershell as administrator and run `Set-ExecutionPolicy Unrestricted`
3. Open VScode and create a new folder
4. Open the terminal (set it to Powershell if it is not already)
5. `python -m venv .venv`
6. Activate the environment `.\venv\Scripts\Activate.ps1`
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
2. Open VScode and create a new folder
3. Open the terminal and set the shell to Command Prompt
4. `python -m venv .venv`
5. Activate the environment `.\venv\Scripts\activate`
6. pip install Flask
7. Create hello.py:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```

8. Create environment variables
```
set FLASK_APP=hello.py
set FLASK_ENV=development
```
9. `flask run`