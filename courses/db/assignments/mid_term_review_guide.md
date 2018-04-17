# OverviewThe
*Update* the mid-term will now only cover chapters 1-3.

The midterm will cover chapters 1-3.  The test will include topics like: introductory material on databases, the relational model, entity relationship model, basic SQL queries, relational algebra, and tuple relational calculus.  In Chapter 4, Domain Relational Calculus will be excluded from the mid-term, but Relational Algebra and Tuple Relational Calculus will be included. You will also benefit if you study your previous quiz.


# Chapter 1
* What benefits to DBMSs provide?
* What are the three different levels of abstraction?  What do each of them mean?
* What is the relational model of data?
  - What is a relation?
  - What is a schema?
* What is data independence?
* What is currency control?
* What is a transaction?
* What is atomicity?
* What is a write-ahead log? Why is it valuable?
* What are some use cases for databases?

# Chapter 2
* Entity Relationship Model
  - Basic Concepts
    - Entities
    - Relationships
    - Attributes
  - How is an entity relationship model used?
  - Diagramming
    - Be able to properly *diagram*, *identify*, and *interpret* the basic concepts of the ER Model (attributes, entities, relationships)
    - Be able *identify* and *interpret* the following details from an entity relationship model:
      - Weak entities/relationships
      - Total vs. partial participation
      - Primary Keys
      - ISA Hierarchies

# Chapter 3
* Be able to *interpret* and *write* queries with features like these:

> SELECT * FROM Students S
WHERE S.age=18;

> SELECT name, age from Teachers S
WHERE T.gender='female';

> SELECT S.name, E.course_id FROM Students S, Enrolled E WHERE S.student_id=E.student_id and E.grade="A";

* Be able to *interpret* queries like these:

> CREATE TABLE students (student_id, int, name CHAR(20));

> DROP TABLE students;

> ALTER TABLE students ADD COLUMN firstYear integer;

> INSERT INTO students (student_id, name, age, gpa) VALUES (12345, "Ahmed Ahmed AbdiAziz", 22 4.0)

* Keys
  - Understand what a key is.  
  - What does a key guarantee? (That the the field or fields of the key will be unique in the relation).  
  - What happens if you try to add a new row that would provide a duplicated key?
  - What is a super key?
  - What is a foreign key?
* What is the purpose of the UNIQUE key word?
* Views
  - Be able to give examples of when or how a view might be useful?
* ER Model to Relational Model translation
  - Be able to match up an entity model with its corresponding relational model

# Chapter 4
* Is a Query Language of equivalent power with programming languages?  If not, which are more powerful?
* Be able to translate a query statement in plain English into a relational algebra query and a tuple relational calculus query.
