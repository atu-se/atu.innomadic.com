# Option 1 -- Powershell 

1. Install Python with "Change environment variables" option
2. Open Powershell as administrator and run
`Set-ExecutionPolicy Unrestricted`
3. Open VScode and create a new folder
4. Open the terminal and run
`python -m venv venv`
5. Activate the environment
`.\venv\Scripts\activate`
6. `pip install Flask`
7. Create hello.py [https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/]
8. Create environment variables
`$env:FLASK_APP = "hello.py"`
`$env:FLASK_ENV = "development"`
6. `flask run`

## Option 2 - Command Prompt

1. Install Python with "Change environment variables" option

3. Open VScode and create a new folder
4. Open the terminal and set the shell to Command Prompt
5. Run 
`python -m venv venv`
6. Activate the environment
`.\venv\Scripts\activate`
7. `pip install Flask`
8. Create hello.py [As in the Flask docs](https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/)
9. Create environment variables
`set FLASK_APP=hello.py`
`set FLASK_ENV=development`
10. `flask run`