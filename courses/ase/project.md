Revision: 4-March-2018

# Project Overview

Your team is responsible for developing a web-based mobile application for receiving, and reporting Road Problems Reports (RPRs) in your city.

# Functional Specification

## Required Scenarios

### Adding a New Road Problem Report

Amina is driving home from work when she notices a huge hole in the middle of the road.  It is very dangerous, so she pulls off to the side of the road and opens your application in her Android web browser.  She is prompted to take a photo and enter a text description.  The application gives her an error message if she attempts to save the report with no description.  When she submits the application, it loads the detail screen of the app, including the location and her photo, among other things. The first time she used the app, it will ask her for permission to access her location.

### Reviewing Road Problem Report Listing and Details

Yusuf works for a paving company and is looking for business.  He opens your web application and on the home page reads through a table listing all of the RPRs.  When he sees one that interests him, he taps a link and is taken to a Google map that shows the location of the RPR.

### Reviewing Road Problem Report Map

Town Councilman Abdi is up for re-election.  He is worried that he will not be re-elected.  He receives a call from Asia, who tells him about the problem she has with the huge pile of rocks near her house.  She mentions the RPR web application, and he opens the web application and sees an opportunity.  He opens the map view and sees that there are many RPRs for his district.  Immediately he begins making phone calls to repair all of the RPRs in his district.  His popularity increases and he wins his re-election.

### Profanity Filter

Asia's son Nux is a naughty boy.  When he saw his mom using the application, he decided to cause some mischief.  He opened the application and creates a RPR with foul language in English and Somali. When the page reloaded, though, he finds that his foul language has been replaced by a sequence of asterisks (e.g. "*****"", thwarting his mischief.

### Reviewing Road Problem Reports

# Non-Goals

* There is no login required to use the application (except if the team chooses to implement an administrator)
* Editing RPRs
* This is not a native mobile application -- it is a *web application*.

# Screens

Each screen should have a menu with the following buttons prominently displayed:
- Home
- Create Report
- Listing


## Home Screen

The home screen should display a google map below the menu, showing your city and a view of the current database entries.


## Listing Screen

This screen should have a table with the following columns:

|                                      | Description                                           |
|--------------------------------------|-------------------------------------------------------|
| [View Details](http://linktodetails) | There is a huge pile of rocks in front of my house    |
| [View Details](http://linktodetails) | There is a pothole in the middle of this intersection |
| [View Details](http://linktodetails) | This section of road needs to be paved                |


## Create Report Screen

Choosing this option should prompt the user to take or choose a picture, and then to enter description of the Road Problem.  It should give an error message for an empty description or a missing photo.

## Detail Screen
This screen should show the following piece of information for a single report:
* Description
* Date Created
* Photo
* Map View Highlighting this Report

#  Technical Specification

## Technology Overview
To build the RPR web application, you will use a variety of technologies:
- Distributed Systems (n-tier)
  - Thin Client (Web Browser)
  - Application/Web Server (Python, NodeJS)
  - Database Server (MariaDB)
- Services (Specifically, ResTful/Web APIs)
- Mobile Web
- Geographic Information System
- Web Frameworks (Flask, Django, or Express)

## Technology Requirements

### Application Server

Your team must choose one of the two platforms for application server development:
* [Python](https://www.python.org/) (Note:  Use Python 3, not Python 2!)
* [NodeJS](https://nodejs.org/en/)

### Web Server

In Python or NodeJS, you will use a web framework.

If you choose Python, you must choose either:
* [Django](https://www.djangoproject.com/) or
* [Flask](http://flask.pocoo.org/)

If you choose NodeJS, you must use [ExpressJS](https://expressjs.com/).

### Database server

You should use either [MySQL](https://www.mysql.com/) or [MariaDB](https://mariadb.org/) and document how to configure it.  

You should include a table called reports which will include the following fields:
* id int
* timestamp timestamp
* description text
* latitude decimal (10,8)
* longitude decimal (11,8)
* photo longblob

### Client

This web application is most suitable for mobile phones.  You app should support the stock Android and iPhone browsers.  It should also work in desktop browsers like Firefox and Chrome, but the user interface should function well in a mobile touchscreen platform.

### Mapping Service

Use the [Google Maps API](https://developers.google.com/maps/) to generate the overview map and the maps for individual reports.

### Content Filtering Service

Use the http://www.purgomalum.com/ API to filter description fields for profanity.  Use the "add" parameter to add at least five profanities from the Somali language to be filtered from the description.

### Geolocation

Use the [HTML5 Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation/Using_geolocation) to get the location for the RPRs.

### Code Sharing
* All code should be published to a [GitHub](github.com) repository and shared with your teacher

### Deployment
* You will need to be able to demonstrate your application running either on your local computer, or preferably via the internet.  You may find a free host such as [PythonAnywhere](https://www.pythonanywhere.com) that can host the application and database.

### Documentation
You should have a README file which documents how to install, configure, and operate the application and database server.

It should list all dependencies and give links for downloads.  What packages need to be installed from pip or npm?  Everything needed to reproduce the application should be documented.

# Grading

The grading will this project will be divided into five assessments.  Each will be equal in weight to a homework or quiz, as outlines in the course syllabus.

1. Create Basic RPR with location and description
2. Extend creation of RPR with photo and profanity filtering
3. RPR Table View
4. RPR Map View
5. Documentation

The majority of the grade for each assignment will come from the functionality of the app, but some consideration will be given to usability and style.

You will have in-class check-ins to present your progress, and occasionally you will have time in class to work as a team, but the majority of your work should be outside of lecture hours.

Due date:  March 31, 2018

**Note: Your teacher reserves the right to adjust the scoring/assignment as the project unfolds.  You will receive advanced notice if this happens.**
