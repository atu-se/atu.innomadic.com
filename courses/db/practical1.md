# Practical Day 1

## Prerequisites

Install the following prerequisites before moving on.
1. Install [Python 3](https://www.python.org/downloads/release/python-364/)
2. Install jupyter
>pip install jupyter

3. Install sql-magic
>pip install sql-magic

4. Install sqlite (if you don't already have it.  Not sure?  Try running sqlite3 at the command prompt.)

5. Install git.


## Stuff to go in the jupyter notebook?

### References
* [a SQL syntax guide for sqlite](https://www.sqlite.org/lang.html)
  * CREATE
  * ALTER TABLE
  * DELETE
  * DROP TABLE
  * INSERT
  * SELECT

### sqlite
First let's explore the [command line interface](https://www.sqlite.org/cli.html).  
Use sqlite to create a new database called "practical1.db":
>sqlite3 practical1.db

Did it open a shell?

Try this:

>.help

Now try

>.tables

Do you see that *artists* table?

Check its schema like this:

>.schema artists

Can you do a select query to view artists?

Now enter

>.mode column

Enter your select query again.  Does it look different?

Now try:
>headers on

Try the query again.

Now check the schema for albums.

What is the relation between artists and albums?

1. Can you create a query that shows you the albums of all artists?

Show your teacher the result.

2. Check out the list of genres.  Can you show a list of all songs in a particular genre?

Show your teacher the result.

3. Can you create a new genre for some type of Somali poetry or music?
Hint:  *insert*

Show your teacher the result.
