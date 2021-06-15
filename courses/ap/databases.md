---
title: Advanced Python
subtitle: 11. Databases Continued
date: June 2021
export_on_save:
  pandoc: true
output:
  custom_document:
    path: databases-continued-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "theme=white", "-V", "revealjs-url=../../presentation/reveal.js-4.1.js", "--slide-level=2", "--standalone"]
---

<style>
.container{
    display: flex;
}
.col{
    flex: 1;
}
</style>

# SQLAlchemy

* Can you to send SQL directory
* Or via an ORM (Object-Relational Mapper)

# Creating DB

```python
from sqlalchemy import create_engine
engine = create_engine(
    "sqlite+pysqlite:///:memory:", 
    echo=True, 
    future=True
)
```

# Execute SQL

```python
from sqlalchemy import text

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())
```
# Insert

```python
with engine.connect() as conn:
    conn.execute(
        text("CREATE TABLE some_table (x int, y int)")
    )
    conn.execute(
    text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
         [
             {"x": 1, "y": 1}, 
             {"x": 2, "y": 4},
         ]
        )
    conn.commit()
```
# Transactions

# Object-Relational Mappers

# ORM Imports 

```python
from sqlalchemy import create_engine
from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
```

# ORM Setup

```python
# Create the DB (in memory)
engine = create_engine("sqlite:///:memory:", echo=True)
# Create the Base object for our models to inherit from
Base = declarative_base()
```

# Example Class

```python
class Parent(Base):
    __tablename__ = "parent"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __repr__(self):
        return f"<Parent(id='{self.id}' name='{self.name}')>"
```
# Example Class 

```python 
class Child(Base):
    __tablename__ = "child"
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey("parent.id"))
    def __repr__(self):
        return f"<Child(id='{self.id}', parent_id='{self.parent_id}'>"
```
# More Setup

```python
# Create tables using the classes defined before
Base.metadata.create_all(engine)

# Create a session object to manage our connections
Session = sessionmaker(bind=engine)
session = Session()
```

# Add New Records

```python
parent1 = Parent(name="Susan")
parent2 = Parent(name="Mary")
session.add(parent1)
session.add(parent2)
session.commit()
```

# View Records

```python 
parents = session.query(Parent).all()
print(parents)
print(parents[0].id)
```

# Add New Records

```python
child1 = Child(parent_id = parents[0].id)
child2 = Child(parent_id = parents[1].id)
session.add_all(
    [child1, child2]
)
session.commit()
```

# View Records

```python 
children = session.query(Child, Parent).join(Parent).all()

for child in children:
    print(child)
```

# Join Records

```python
child, parent = session.query(Child, Parent).join(Parent).first()
print (parent.name)
```

# Filter Records

```python
child = session.query(Child, Parent).join(Parent).filter(Parent.name=='Mary').all()
print (f'here we have filtered for parents named mary: {child}')
```

# Sources

* [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/14/tutorial/engine.html)
