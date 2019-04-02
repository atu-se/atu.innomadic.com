---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.0'
      jupytext_version: 1.0.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Notebook Setup

The following two commands are for the instructor's teacher notebook.  If you are following along using MySQL Workbench, you will just need to open the Workbench and connect to your server. You won't need to enter these commands.

```python
load_ext sql
```

```python
%%sql
mysql+pymysql://@localhost/
```


# Database Setup

## Database Creation

First we will create a database named chapter3insert.  To make it easier to re-run these commands, we are going to drop the database if it already exists.

In the future, if you are working with an existing database, you may choose to just add the `use` statement.  However, you must remember that you can't re-create a table that already exists.

```python
%%sql
drop database if exists chapter3insert;
create database chapter3insert;
use chapter3insert;
```

# Schema Definition

Next, we will four tables for our database.  Do you understand each part of the schema?

```python
%%sql
create table course (
    course_id		varchar(8),
	 title			varchar(50),
	 dept_name		varchar(20),
	 credits		numeric(2,0)
);
```

```python
%%sql
create table instructor(
    ID			varchar(5),
	 name			varchar(20) not null,
	 dept_name		varchar(20),
	 salary			numeric(8,2),
	 primary key (ID)
    );
```

```python
%%sql
create table student
	(ID			varchar(5),
	 name			varchar(20) not null,
	 dept_name		varchar(20),
	 tot_cred		numeric(3,0) check (tot_cred >= 0),
	 primary key (ID)
	);
```

```python
%%sql
create table department
	(dept_name		varchar(20),
	 building		varchar(15),
	 budget		        numeric(12,2) check (budget > 0),
	 primary key (dept_name)
	);
```

# Check our work.

Now let's examine what we created.  In WorkBench, just refresh the list of tables.

```python
%%sql
show tables;
```

# Insertion

When we want to add tuples to a table, we use the `insert` command.  

The format is like this:

`insert into <table>`
values (A~1~, A~2~, A~3~, A~4~)

```python
%%sql
insert into course       
values ('CS-437', 'Database Systems', 'Comp. Sci.', 4);
```


```python
%%sql
select * from course;
```

```python
%%sql
insert into course (course_id, title, dept_name, credits)            
values ('CS-437', 'Database Systems', 'Comp. Sci.', 4);
```

```python
%%sql
insert into course (course_id, title, dept_name)            
values ('CS-437', 'Database Systems', 'Comp. Sci.');
```

```python
%%sql
insert into course (title, course_id, dept_name)            
values ('Database Systems', 'CS-437', 'Comp. Sci.');
```

```python
%%sql
create table budget
(
    id varchar(2)
);
```

```python
%%sql
insert into budget
values (1, 'Comp. Sci.', 10000, 123);
```

```python
%%sql
select * from course;
```

```python
%%sql
insert into student
values ('3003', 'Green', 'Finance', null);
```


```python
%%sql
select * from student;
```

## Data Creation

Now that we know how insert works, let's add more sample data to our relations.

```python
%%sql
insert into instructor values ('10101', 'Srinivasan', 'Comp. Sci.', '65000');
insert into instructor values ('12121', 'Wu', 'Finance', '90000');
insert into instructor values ('15151', 'Mozart', 'Music', '40000');
insert into instructor values ('22222', 'Einstein', 'Physics', '95000');
insert into instructor values ('32343', 'El Said', 'History', '60000');
insert into instructor values ('33456', 'Gold', 'Physics', '87000');
insert into instructor values ('45565', 'Katz', 'Comp. Sci.', '75000');
insert into instructor values ('58583', 'Califieri', 'History', '62000');
insert into instructor values ('76543', 'Singh', 'Finance', '80000');
insert into instructor values ('76766', 'Crick', 'Biology', '72000');
insert into instructor values ('83821', 'Brandt', 'Comp. Sci.', '92000');
insert into instructor values ('98345', 'Kim', 'Elec. Eng.', '80000');
insert into department values ('Biology', 'Watson', '90000');
insert into department values ('Comp. Sci.', 'Taylor', '100000');
insert into department values ('Elec. Eng.', 'Taylor', '85000');
insert into department values ('Finance', 'Painter', '120000');
insert into department values ('History', 'Painter', '50000');
insert into department values ('Music', 'Packard', '80000');
insert into department values ('Physics', 'Watson', '70000');
```

```python
%%sql
select * from instructor;
```

```python
%%sql
select *
from department;
```

# Deletion

To delete use the `delete` command, in this format:

`delete from <table> where <predicate>`

Delete all instructors:

`delete from instructor`

Delete all instructors from the Finance department:

`delete from instructor
where dept_name= 'Finance';`

Delete all tuples in the instructor relation for those instructors associated with a department located in the Watson building:

`delete from instructor
where dept name in
    (
        select dept name
        from department
        where building = 'Watson'
    );`

## Examples

### Example 1 - Remove all tuples from a relation

```python
%%sql
select * from student;
```

```python
%%sql
delete from student;
select * from student;
```

### Example 2 - Delete tuples from a relation specified with a `where` clause

```python
%%sql
select * from instructor;
```

```python
%%sql
delete from instructor
where dept_name= 'Finance';
select * from instructor;
```

### Example 3 - Delete tuples from a relation using a nested query

```python
%%sql
select * from department;
```

```python
%%sql
select * from instructor;
```

The following query will delete all the instructors which are in a department that meets in the Watson building.

First let's see which departments meet in the Watson building:


```python
%%sql
select *
from department
where building='Watson';
```

We can also do a join query to see which instructors will be deleted:

```python
%%sql
select instructor.*
from instructor, department
where instructor.dept_name = department.dept_name
and department.building='Watson';
```

```python
%%sql
delete from instructor
where dept_name in (
    select dept_name
    from department                                                  
    where building = 'Watson'
);
```


```python
%%sql
select * from instructor;
```

# Drop vs. Delete

You can `drop` items from the schema:
* database
* table
* attribute

You delete tuples.



```python
%%sql
create table student
	(ID			varchar(5),
	 name			varchar(20) not null,
	 dept_name		varchar(20),
	 tot_cred		numeric(3,0) check (tot_cred >= 0),
	 primary key (ID)
	);

```

```python
%%sql
delete from student;
```

```python
%%sql
drop table student;
```

```python
%%sql
show tables;
```

```python

```
