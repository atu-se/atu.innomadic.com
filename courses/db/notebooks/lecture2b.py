# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 1.0.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

load_ext sql

# %%sql 
mysql+pymysql://instructor:password@localhost/
drop database if exists lecture2;
create database lecture2;
use lecture2;

# # Lecture 2b

# First, let's recreate the instructor table -- this time with no foreign key.

# %%sql 
drop table if exists instructor;
create table instructor (
    ID         char(5),
    name       varchar(20) not null,
    dept_name  varchar(20),
    salary     numeric(8,2),
    primary key (ID)
);

# # Show Tuples

# %%sql 
select * from instructor;

# # Updates to Tables
#
# ## Insert
#
# ```sql
# insert into instructor values (‘10211’, ’Smith’, ’Biology’, 66000);
# ```
#

# %%sql 
insert into instructor (ID, name, dept_name, salary) 
values ('10211', 'Smith', 'Biology', 66000);

# %%sql 
select * from instructor;

# %%sql
insert into instructor values ('55532', 'Ahmed', 'Chemistry', 150000);

# ## Delete
#
# Remove all tuples from the a relation
#
# `delete from <table>;`
#

# %%sql 
delete from instructor;

# %%sql 
select * from instructor;

# ## Delete Table

# %%sql 
drop table instructor;

# %%sql 
show tables;

# %%sql 
create table department (
     dept_name varchar(20),
     primary key (dept_name)
);

# %%sql 
desc department;

# ## Alter

# ## Adding an Attribute 
#
# alter table r add A D;

# %%sql 
alter table department add ID char(3);

# %%sql 
desc department;

# ## Dropping an Attribute 
#
# alter table r drop A;
#
# * where A is the name of an attribute in relation _r_
# * Dropping of attributes is not supported by some databases

# %%sql 
alter table department drop ID;

# %%sql 
desc department;

# # Basic Query Structure
#
# *  A typical SQL query has the form:
#
# ```mysql
# select A1, A2, ..., An
# from r1, r2..., rn
# where P
# ```
#
# * Ai represents an attribute
# * Ri represents a relation
# * P is a predicate
#
# * The result of a SQL query is... a relation.
#
# ### Example
#
# First, let's recreate the instructor table and add some tuples.

# %%sql 
drop table if exists instructor;
create table instructor (
    ID         char(5),
    name       varchar(20) not null,
    dept_name  varchar(20),
    salary     numeric(8,2),
    primary key (ID)
);

# %%sql 
insert into instructor (ID, name, dept_name, salary) values ('10211', 'Smith', 'Biology', 50000);
insert into instructor (ID, name, dept_name, salary) values ('10212', 'Yusuf', 'Mathematics', 55000);
insert into instructor (ID, name, dept_name, salary) values ('10215', 'Yusuf', 'English', 52000);
insert into instructor (ID, name, dept_name, salary) values ('10213', 'Asma', 'Mathematics', 60000);
insert into instructor (ID, name, dept_name, salary) values ('10214', 'Thomas', 'Literature', 65000);

# Now, let's query for instructor names:

# %%sql
select *
from instructor;

# Now, let's add a predicate:

# %%sql 
select dept_name, salary
from instructor 
where name = 'Yusuf';


