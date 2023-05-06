# Software Engineering Tools

## Course Summary

This highly practical course will focus on introducing students to the daily tools of the trade in collaborative software engineering.  Examples include development environments, design tools, virtualization, re-using software packages, source code control, and testing tools.  This course should accelerate students' ability to be productive in applying lessons later in the program.

## Course Slack

* [Join #class_of_2021 and introduce yourself](https://join.slack.com/t/abaarsotechu/shared_invite/zt-mx9q0zzq-uaVHrxfdiRK58Jen1_FZkA)



## Lectures

| Lecture | Topic                                                                 |
|---------|-----------------------------------------------------------------------|
| 1.      | [Course Overview and Editors](lectures/lecture1/lecture1-slides.html) |
| 2.      | Vagrant, Shared Folders, Remote SSH                                   |
| 3.      | Docker                                                                |
| 4.      | Source Control                                                        |
| 5.      | [Package Management](lectures/package_management-slides.html)         |
| 6.      | [Documentation with Sphinx](lectures/documentation_with_sphinx)       |
| 7.      | Publishing Sphinx Documention to ReadTheDocs                          |
| 8.      | Code Quality Tools                                                    |
| 9.      | Deployment with Heroku                                                |

## Links

### Vim

* [Vim Cheatsheet](http://vimsheet.com/)
* [Vim Game Tutorial](https://vim-adventures.com)

## Updates

### Week of July 3

### Final Exam Topics

* Package Management
    * Python packages
    * pip
    * Python virtual environments
* Documentation
    * Sphinx
    * sphinx-autoapi
    * ReadTheDocs
* Code Quality
    * pep 8
    * flake8
    * black
    * git hooks
* Continous/Automated Deployment
    * Heroku/Git/Github


#### Code Quality

- Style
- for readability and not making mistakes

#### Guide

PEP 8

#### Linters

* flake8 - warns us about the problems
* black - helps us solve the problems !! :-)

### Week of June 26


#### Assignment

* [Assignment #3](https://classroom.github.com/a/3ue65c4H) has been posted.  It is due July 4 at 11:59 p.m.  You will submit via Github.

#### ReadTheDocs

* Instructions for integrating Sphinx with ReadTheDocs:

```
1. Create and activate a virtual environment
    py -m venv .venv
    .venv\Scripts\activate.ps1
2. pip install sphinx-autoapi
3. pip freeze > requirements.txt
4. Publish as a public repo on Github (no .venv!)
4. Create account at readthedocs.org
5. Link to your repository
6. In advanced settings add requirements.txt
7. Enjoy!
```

* Instructions for building Sphinx documentation

```
1. py -m pip install -U sphinx
2. Create a project folder with a `docs` subfolder.  
3. Open the `docs` folder in a terminal
4. Run `sphinx-quickstart` (You can choose the defaults for almost everything: add your own project name and name.)
5. Run `.\make.bat html` to generate the HTML documentation
```

* Note: to run sphinx-quickstart, you will need to have the Python Scripts folder in your Windows PATH environment variable.


### Week of June 5

* This week we will be looking at package management and we will use the Python ecosystem as an example

Instructions for setting up Python virtual environment:

1. Open Powershell as administrator and run `set-executionpolicy remotesigned`
2. Open a terminal to the folder you want to use 
3. python -m venv .venv
4. Activate the environment .venv\Scripts\Activate.ps1


### Week of April 3

For the mid-term exam, you should have an understanding of the concepts and practical aspects of:

* Text Editors, (vi, VSCode)
* Markdown
* Sequence Diagrams (e.g. Mermaid sequence Diagrams)
* Virtual Machines (Vagrant, Virtualbox)
* Containers (Docker)
* Version Control Software 
    * Git and Git workflows
    * Github and Github workflows
* Linux bash commands

You should be prepared to answer both practical "how-to" questions regarding these tools, in addition to answering conceptual questions about the benefits of these tools.


### Week of March 27

We looked at some Linux bash commands and programs:

1. `man`
2. `date`
3. `echo`
4. basic file system layout
5. `pwd`
6. `ls`
7. `$PATH`
8. `cd`
9. `~`
10. `clear`
11. `mv`
12. `|`
13. `ping`

### Week of March 20

* [Flask Docker Demo](https://github.com/innomadic/flask_docker_demo)
* [Git Notes](https://github.com/innomadic/git_lecture)
* [Git tutorial](https://git-scm.com/docs/gittutorial)
* [Atlassian Git tutorial](https://www.atlassian.com/git/tutorials/saving-changes)

* [Homework Assignemnt 2: Git Lab due March 29 11:59 PM](https://classroom.github.com/a/LcX6LbZR)

### Week of March 6

Create a sequence diagram using Markdown Preview Enhanced and Mermaid-JS.  The sequence diagram should model the process to purchase $1 of internet data using the short code interface for Zaad.