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

* .Net - NuGet
* Python - PIP
* Perl - CPAN
* Java - no direct parallel, but automation tools like [Maven](https://softwarerecs.stackexchange.com/questions/36017/install-java-packages-and-their-dependancies-like-pip-for-python) can automatically download dependencies

## Package Management in Python

* `pip` is installed with Python (usually) and is used for installing packages
* An index of packages is available at [PyPI.org](https://pypi.org/)
* Some packages are actually installable applications, while others provide libraries or frameworks which can be used from a Python application by importing a module

## Demo

## Challenge

* Install the `youtube-dl` package
* Use youtube-dl to download this youtube video: https://www.youtube.com/watch?v=Pi4QapbHFms
