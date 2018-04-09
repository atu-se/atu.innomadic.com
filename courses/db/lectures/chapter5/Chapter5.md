
# Chapter 5

## SQL: Queries, Programming, Triggers

For this lecture, we will be using this Jupyter notebook to demonstrate queries.  We require the *ipython-sql* module, and the following lines load the module and create an in-memory database:


```python
%load_ext sql
%sql sqlite://
```

    The sql extension is already loaded. To reload it, use:
      %reload_ext sql





    'Connected: @None'



# Table Creation 

Now let's create some tables for sailors example and then add some data to them.  

We will create a table for:
* sailors
* boats
* reservations

*Note: I have added in a command to DROP the tables if they already exist.  This makes it easier to re-run these commands if necessary.*


```python
%%sql 

DROP TABLE IF EXISTS sailors; 

CREATE TABLE sailors ( 
    sailor_id INTEGER PRIMARY KEY, 
    sailor_name varchar(20), 
    rating int, 
    age float);
```

     * sqlite://
    Done.
    Done.





    []




```python
%%sql 

DROP TABLE IF EXISTS boats;

CREATE TABLE boats (
    boat_id INTEGER PRIMARY KEY,
    color VARCHAR(20)
);
```

     * sqlite://
    Done.
    Done.





    []




```python
%%sql 
INSERT INTO BOATS (boat_id, color)
VALUES ( 101, 'red' );
INSERT INTO BOATS (boat_id, color)
VALUES ( 103, 'green');
```

     * sqlite://
    1 rows affected.
    1 rows affected.





    []




```python
%%sql 

DROP TABLE IF EXISTS reservations;

CREATE TABLE reservations (
    sailor_id INTEGER, 
    boat_id INTEGER, 
    date int, 
    FOREIGN KEY(sailor_id) REFERENCES sailors(sailor_id));
```

     * sqlite://
    Done.
    Done.





    []




```python
%%sql 
INSERT INTO SAILORS (sailor_id, sailor_name, rating, age)
VALUES ( 22, 'Dustin', 7, 45.0 );
INSERT INTO SAILORS (sailor_id, sailor_name, rating, age)
VALUES ( 31, 'Lubber', 8, 55.5 );
INSERT INTO SAILORS (sailor_id, sailor_name, rating, age)
VALUES ( 58, 'Rusty', 10, 35.0 );
INSERT INTO SAILORS (sailor_id, sailor_name, rating, age)
VALUES ( 28, 'Yuppy', 9, 45.0 );
INSERT INTO SAILORS (sailor_id, sailor_name, rating, age)
VALUES ( 48, 'Guppy', 5, 35.0 );
```

     * sqlite://
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.





    []




```python
%%sql
DELETE FROM reservations;


INSERT INTO RESERVATIONS (sailor_id, boat_id, date)
VALUES ( 22, 101, date('1996-10-10') );
INSERT INTO RESERVATIONS (sailor_id, boat_id, date)
VALUES ( 58, 103, date('1996-11-12') );
INSERT INTO RESERVATIONS (sailor_id, boat_id, date)
VALUES ( 58, 101, date('1996-11-15') );


```

     * sqlite://
    0 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.





    []



# Review the Data
Let's take a look at all the data we just created:


```python
%sql SELECT * from sailors;
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
        <th>sailor_name</th>
        <th>rating</th>
        <th>age</th>
    </tr>
    <tr>
        <td>22</td>
        <td>Dustin</td>
        <td>7</td>
        <td>45.0</td>
    </tr>
    <tr>
        <td>28</td>
        <td>Yuppy</td>
        <td>9</td>
        <td>45.0</td>
    </tr>
    <tr>
        <td>31</td>
        <td>Lubber</td>
        <td>8</td>
        <td>55.5</td>
    </tr>
    <tr>
        <td>48</td>
        <td>Guppy</td>
        <td>5</td>
        <td>35.0</td>
    </tr>
    <tr>
        <td>58</td>
        <td>Rusty</td>
        <td>10</td>
        <td>35.0</td>
    </tr>
</table>




```python
%sql SELECT * from boats;
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>boat_id</th>
        <th>color</th>
    </tr>
    <tr>
        <td>101</td>
        <td>red</td>
    </tr>
    <tr>
        <td>103</td>
        <td>green</td>
    </tr>
</table>




```python
%sql SELECT * from reservations;
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
        <th>boat_id</th>
        <th>date</th>
    </tr>
    <tr>
        <td>22</td>
        <td>101</td>
        <td>1996-10-10</td>
    </tr>
    <tr>
        <td>58</td>
        <td>103</td>
        <td>1996-11-12</td>
    </tr>
    <tr>
        <td>58</td>
        <td>101</td>
        <td>1996-11-15</td>
    </tr>
</table>



# Example of Conceptual Evaluation


```python
%%sql

SELECT s.sailor_name 
FROM sailors s, reservations r
WHERE s.sailor_id=r.sailor_id AND r.boat_id=103;
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_name</th>
    </tr>
    <tr>
        <td>Rusty</td>
    </tr>
</table>



Notice that the following queries return the same results, despite not having or not using the range variables *s* and *r*:


```python
%%sql 

SELECT s.sailor_name 
FROM sailors s, reservations r
WHERE s.sailor_id=r.sailor_id AND boat_id=103;
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_name</th>
    </tr>
    <tr>
        <td>Rusty</td>
    </tr>
</table>




```python
%%sql 

SELECT sailor_name from sailors, reservations
WHERE sailors.sailor_id=reservations.sailor_id AND boat_id=103;
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_name</th>
    </tr>
    <tr>
        <td>Rusty</td>
    </tr>
</table>



# Find sailors who've reserved at least one boat


```python
%%sql 

SELECT s.sailor_id
FROM sailors s, reservations r
WHERE s.sailor_id=r.sailor_id;
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
    </tr>
    <tr>
        <td>22</td>
    </tr>
    <tr>
        <td>58</td>
    </tr>
</table>



Notice how the query below uses arithmetical expressions in its result, and pattern matching with the *LIKE* keyword:


```python
%%sql 

SELECT s.sailor_name, s.age, S.age-5 AS age1, 2*s.age AS age2
FROM sailors s
WHERE s.sailor_name LIKE 'Y_%Y';
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_name</th>
        <th>age</th>
        <th>age1</th>
        <th>age2</th>
    </tr>
    <tr>
        <td>Yuppy</td>
        <td>45.0</td>
        <td>40.0</td>
        <td>90.0</td>
    </tr>
</table>



# Find sailor_ids for sailors who've reserve a red *or* a green boat


```python
%%sql 

SELECT s.sailor_id
FROM sailors s, boats b, reservations r
WHERE s.sailor_id=r.sailor_id 
    AND r.boat_id=b.boat_id 
    AND (B.color='red' OR b.color='green');
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
    </tr>
    <tr>
        <td>22</td>
    </tr>
    <tr>
        <td>58</td>
    </tr>
</table>



# What if we replace the OR with AND?


```python
%%sql 

SELECT s.sailor_id
FROM sailors s, boats b, reservations r
WHERE s.sailor_id=r.sailor_id 
    AND r.boat_id=b.boat_id 
    AND (b.color='red' AND b.color='green');
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
    </tr>
</table>



This query probably isn't doing what we wanted it to.  It is looking for boats that are both red and green!  

Another way to get these same results as the original *OR* query is to do a union of two queries.

*Note: they must be union-compatible.*


```python
%%sql 

SELECT s.sailor_id
FROM sailors s, boats b, reservations r
WHERE s.sailor_id=r.sailor_id 
    AND r.boat_id=b.boat_id 
    AND (B.color='red')

UNION

SELECT s.sailor_id
FROM sailors s, boats b, reservations r
WHERE s.sailor_id=r.sailor_id 
    AND r.boat_id=b.boat_id 
    AND (B.color='green')
    ;
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
    </tr>
    <tr>
        <td>22</td>
    </tr>
    <tr>
        <td>58</td>
    </tr>
</table>



In the same place as the UNION keyword, we could use the EXCEPT keyword.


```python
%%sql 

SELECT s.sailor_id
FROM sailors s, boats b, reservations r
WHERE s.sailor_id=r.sailor_id 
    AND r.boat_id=b.boat_id 
    AND (B.color='red')

EXCEPT

SELECT s.sailor_id
FROM sailors s, boats b, reservations r
WHERE s.sailor_id=r.sailor_id 
    AND r.boat_id=b.boat_id 
    AND (B.color='green')
    ;
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
    </tr>
    <tr>
        <td>22</td>
    </tr>
</table>



# Find the sailor_ids of sailors who've reserved a red *and* a green boat


```python
%%sql 

SELECT s.sailor_id 
FROM sailors s, boats b1, reservations r1, boats b2, reservations r2
WHERE s.sailor_id=r1.sailor_id 
    AND r1.boat_id=b1.boat_id
    AND s.sailor_id=r2.sailor_id
    AND r2.boat_id=b2.boat_id
    AND (b1.color='red' AND b2.color='green');
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
    </tr>
    <tr>
        <td>58</td>
    </tr>
</table>



## We can implement the same query by taking the intersection of two queries.


```python
%%sql 

SELECT s.sailor_id
FROM sailors s, boats b, reservations r
WHERE s.sailor_id=r.sailor_id 
    AND r.boat_id=b.boat_id 
    AND (B.color='red')

INTERSECT

SELECT s.sailor_id
FROM sailors s, boats b, reservations r
WHERE s.sailor_id=r.sailor_id 
    AND r.boat_id=b.boat_id 
    AND (B.color='green')
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
    </tr>
    <tr>
        <td>58</td>
    </tr>
</table>



# Nested Queries


```python
%%sql 

SELECT s.sailor_name
FROM sailors s
where s.sailor_id IN (
        SELECT r.sailor_id
        FROM reservations r
        WHERE r.boat_id=103)
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_name</th>
    </tr>
    <tr>
        <td>Rusty</td>
    </tr>
</table>




```python
%%sql 

SELECT s.sailor_name
FROM sailors s
WHERE EXISTS (
        SELECT *
        FROM reservations r
        WHERE r.boat_id=103
            AND s.sailor_id=r.sailor_id);
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_name</th>
    </tr>
    <tr>
        <td>Rusty</td>
    </tr>
</table>



# Set Comparison Operators

Our slides make use of the keyword *ANY*.  SQLite does not implement this keyword, but we can create a similar outcome by using the *MIN* function. 


```python
%%sql 

SELECT * 
FROM sailors s
WHERE s.rating > (
    SELECT MIN(s2.rating) 
    FROM sailors s2
    WHERE s2.sailor_name='Dustin');
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
        <th>sailor_name</th>
        <th>rating</th>
        <th>age</th>
    </tr>
    <tr>
        <td>28</td>
        <td>Yuppy</td>
        <td>9</td>
        <td>45.0</td>
    </tr>
    <tr>
        <td>31</td>
        <td>Lubber</td>
        <td>8</td>
        <td>55.5</td>
    </tr>
    <tr>
        <td>58</td>
        <td>Rusty</td>
        <td>10</td>
        <td>35.0</td>
    </tr>
</table>



# Rewriting INSERSECT Queries Using IN


```python
%%sql 

SELECT s.sailor_id
FROM sailors s, boats b, reservations r
WHERE s.sailor_id=r.sailor_id 
    AND r.boat_id=b.boat_id
    AND b.color='red'
    AND s.sailor_id IN (
        SELECT S2.sailor_id
        FROM sailors s2, boats b2, reservations r2
        WHERE s2.sailor_id=r2.sailor_id 
            AND r2.boat_id=b2.boat_id
            AND b2.color='green')
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_id</th>
    </tr>
    <tr>
        <td>58</td>
    </tr>
</table>



Can you change the above query to return the sailor's name instead of the sailor_id?

# Division in SQL

Here is the "easy" way:


```python
%%sql 

SELECT s.sailor_name
FROM sailors s
WHERE NOT EXISTS (
    SELECT b.boat_id
    FROM boats b
    EXCEPT 
        SELECT r.boat_id
        FROM reservations r
        WHERE r.sailor_id=s.sailor_id) ;
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_name</th>
    </tr>
    <tr>
        <td>Rusty</td>
    </tr>
</table>




```python
%%sql 

SELECT s.sailor_name
FROM sailors s
WHERE NOT EXISTS(
    SELECT b.boat_id
    FROM boats b
    WHERE NOT EXISTS (
        SELECT r.boat_id
        FROM reservations r
        WHERE r.boat_id=b.boat_id
            AND r.sailor_id=s.sailor_id));
```

     * sqlite://
    Done.





<table>
    <tr>
        <th>sailor_name</th>
    </tr>
    <tr>
        <td>Rusty</td>
    </tr>
</table>


