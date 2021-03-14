# Advanced Python

## Tentative Topics

* Package Management
* Advanced Python language features
* User interfaces
* Database integration
* Frameworks for rapid development

## Course Slack

* [Join #class_of_2022 and introduce yourself](https://join.slack.com/t/abaarsotechu/shared_invite/zt-mx9q0zzq-uaVHrxfdiRK58Jen1_FZkA)



## Lectures

| Lecture | Topic                                                                     |
|---------|---------------------------------------------------------------------------|
| 1.      | Course Overview and Python Packages                                       |
| 2.      | [Python Review](lecture2/lecture2-slides.html)                            |
| 3.      | [Python Review Continued](Lecture 3 - Python Basics Review.html)          |
| 4.      | [Object Oriented Programming](Lecture 4 - Object Oriented Programming.md) |
| 5.  | Web Frameworks

## Updates

### Week of 13-March

# Set Up for Flask app

1. Create and open a folder
    1. Open command prompt
    2. `mkdir flask_app`
    3. `cd flask_app`
2. Create a virtual environment `python -m venv flask_app`
3. Activate environment `.\flask_app\Scripts\activate`
4. Install flask `pip install Flask`
5. Open the folder in vscode and [create hello.py as directed in the Flask Quick Start](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
6. `set FLASK_APP=hello.py`
7. `set FLASK_ENV=development`
8. `flask run`

*Note: if you cannot run `python` from the command prompt. try reinstalling Python with "Change environment variables" checked.*