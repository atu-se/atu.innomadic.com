---
title: Software Engineering Tools
subtitle: Package Management
date: June 2021
export_on_save:
  pandoc: true
output:
  custom_document:
    path: package_management-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "theme=white", "-V", "revealjs-url=../../../presentation/reveal.js-4.1.js", "--slide-level=2", "--standalone"]
---

<style>
.container{
    display: flex;
}
.col{
    flex: 1;
}
</style>

## Package Management

* Re-use is a pillar of software engineering (we covered this in detail in ASE)
* Different ecosystems have different means for acquiring and managing source code libraries, frameworks, etc.
* While source code is often shared via a code sharing site like Github, the best way to install and use it may be by using a package manager in your development environment

## Package Managers

* NodeJS - NPM
* .Net - NuGet
* Python - PIP
* Perl - CPAN
* Java - no direct parallel, but automation tools like [Maven](https://softwarerecs.stackexchange.com/questions/36017/install-java-packages-and-their-dependancies-like-pip-for-python) can automatically download dependencies

## Package Management in Python

* `pip` is installed with Python (usually) and is used for installing packages
* An index of packages is available at [PyPI.org](https://pypi.org/)
* Some packages are actually installable applications, while others provide libraries or frameworks which can be used from a Python application by importing a module

## Example: Videos

* youtube-dl is a software package available on PyPI
* It provides an application which can be run from the command line to download videos
* Packages are installed using `pip install`, `python -m pip install`, or, on some Windows installations `py -m pip install`
* To install youtube-dl, you would issue a command like: `pip install youtube-dl`

## Challenge

* Install the `youtube-dl` package
* Use youtube-dl to download this youtube video: [https://www.youtube.com/watch?v=Pi4QapbHFms](https://www.youtube.com/watch?v=Pi4QapbHFms)

## Example: PDFs

* Imagine we want to programmatically work with a PDF:
  * Collected metadata
  * Extract text
* Package: PyPDF2

## Installation

* Install PyPDF2 with this command:

`pip install PyPDF2`

## Using PyPDF2

```python
from PyPDF2 import PdfFileReader
from pathlib import Path
# Prerequisite: have a PDF called textbook.pdf in the current working directory
pdf_path = (Path.cwd() / 'textbook.pdf')
pdf  = PdfFileReader(str(pdf_path))
print(f'Document Information:\n {pdf.documentInfo}\n')
print(f'Total number of pages is {pdf.getNumPages()}\n')
text = pdf.getPage(1).extractText()
print(f'Text on page 1 is:\n\n {text}')
```




# References

* [Tutorial on creating and modifying PDFs](https://realpython.com/creating-modifying-pdf)
* [PyPDF2](https://pythonhosted.org/PyPDF2/)
* [youtube-dl](https://pypi.org/project/youtube_dl/)