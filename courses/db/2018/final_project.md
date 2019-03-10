# Final Project

* See front page for deadline information, which has been updated.

## Overview

For this project you work alone to design a university database.  You will track student enrollment by class and department.  The database will require an authenticated login.  

## Design Requirements

* Entity Relationship diagram
  - Designed in Yed
  - Include the following features:
    - Entities
    - Relationships
    - 1:1 Relationship Notation (Arrows)
    - Total Participation Notation (Bold lines)
* SQLite database
  - Create a SQL database including
    - All relations and fields
    - Proper designation of constraints such as:
      - Primary keys
      - Unique fields
      - Foreign keys
      - Non-null fields
    - Include sample data as designated below.

## Data Description

It should include the following information.  All fields are required, unless otherwise noted.

* Departments
  - Name
* Students
  - Name
  - Phone Number
  - Admission Date
  - Birthdate
  - Student ID (Unique)
  - Gender (Optional)
* Classes
  * Starting Year
  * Class (Freshman, Junior, Senior)
  * Room Number (Optional)
* System Users
  - Username
  - Password

## Sample Data

Include the following sample data:
* All of Abaarso's current departments
* Three classes
* At least four students in each class
* At least seven students in Software Engineering
* AT least seven students in International Relations & Development
* At least two system users

## Access Application Scenarios

You should support the following scenarios:
* Login
* Data View
* Updating
* Data Creation
* Data Deletion
* Search
* Queries/Reports
  - Show all students in a particular department
  - Show all students in a particular class
  - Show one student's detailed information

The following screens:
* Login
* Home
* Create/Delete
* Search/Update
* Queries/Reports

# Grading

## Overview of Marks

| Component              | Marks |
|------------------------|-------|
| ER Diagram in Yed      | 6%    |
| SQLite Database        | 10%   |
| Access Tables/Data     | 8%    |
| Access Forms           | 8%    |
| Access Queries/Reports | 8%    |
| *Total Marks*          | 40%   |


## Rubric

* Entity Relationship Diagram
  - Proper Notation
    - Entities, Relationships
    - Including any 1:1 relationships
    - Total Participation
* SQL Database Design
  - Correct relations and fields
  - Correct integrity constraints (primary keys, foreign keys, unique, etc.)
  - Test Data
* Access Database Application
  - Schemas/Instance (Is the table design accurate? Do you have sample data?)
  - Forms (Do you have all forms working?)
  - Queries/Reports
