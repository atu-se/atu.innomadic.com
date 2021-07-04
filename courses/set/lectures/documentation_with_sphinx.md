# Documentation with Sphinx

* We are going to use Sphinx to produce high quality HTML documentation that we write
* We are going to use sphinx-autoapi to automatically extract API documentation from Python code

## Installing Sphinx

1. Run `python -m pip install -U sphinx`
2. If sphinx-quickstart does not run from the command line, you may need to add it to your PATH system environment variable

## Beginning a new Sphinx documentation project

1. Create a project folder with a `docs` subfolder.  (Your code would go in a folder called `src`.)
2. Open the `docs` folder in a terminal
3. Run `sphinx-quickstart` (You can choose the defauls for almost everything: add your own project name and name.)
4. Run `.\make.bat html` to generate the HTML documentation

## Installing sphinx-autoapi

Run `python -m pip install -U sphinx`

## Adding api documentation to your project

1. Place a Python file in the `src` folder.
2. Add the following lines to the end of your `docs/conf.py` file

```
extensions = ['autoapi.extension']
autoapi_dirs = ['../src']
```

3. Run `.\make.bat html` to generate the HTML documentation

## Publishing a Sphinx documentation project to ReadTheDocs

1. Create a virtual environment and install `sphinx-autoapi` into it
2. Run `pip freeze > requirements.txt`
3. Publish as a public repo on Github (Important: do not include the .venv in the repository!)
4. Create account at readthedocs.org
5. Link to your repository
6. In advanced settings add requirements.txt


## References

* [Sphinx Project](https://www.sphinx-doc.org/en/master/usage/quickstart.html?highlight=auto#autodoc)
* [Sphinx Auto-API](https://sphinx-autoapi.readthedocs.io/en/latest/tutorials.html)
* [Docstrings](https://www.python.org/dev/peps/pep-0257/)