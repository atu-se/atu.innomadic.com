# Assignment 3

This is a solo assignment.  You should not share your work with other students or use their work.  

Create a database that follows [this entity relationship diagram](https://creately.com/diagram/example/h7cw0wrb1/+E-R+Diagram+of+Library+Management+System)

# Specifications

* Be sure to designate all foreign key relationships.
* If a foreign key may not be NULL, specify that in your schema.
* Remember that dates in sqlite may be stored as integers or strings.
* Use the following resources to help you:
  - Use [this notation description](https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning) to help you interpret whether the relationships are one-to-one, one-to-many, zero or many, etc.
  - Implementing [1:1 Relationships](http://www.databaseprimer.com/pages/relationship_1to1/) in SQL
  - If an entity totally participates in a relationship, that means that when it is referred to by the foreign key, it cannot be NULL
  - If a relationship is one to one then a UNIQUE key constraint is necessary for the foreign key

# Data

Create some of your own data (or making personal selections from actual books) and add to your database:
* Add at least four books to your database.  Complete all fields.
* Add at least four members
* Add at least six borrows
* Add at least two publishers

# File name
Save your database using this file name schema:
firstname_secondname_thirdname_assignment3_(morning|evening).db

# Submission

Email your database to your professor by May 1.
