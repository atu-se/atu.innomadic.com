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

# Sources

* [https://docs.sqlalchemy.org/en/14/tutorial/engine.html](SQLAlchemy Tutorial)
