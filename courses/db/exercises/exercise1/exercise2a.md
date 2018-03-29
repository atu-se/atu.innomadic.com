# Introduction

For this exercise, you should have sqlite3 installed on your computer.  You should be able to run sqlite3 from the Command Prompt.  Are you familar with the command prompt? Take a look at this tutorial on the [command prompt](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands).

Your computer should have [sqlite](http://sqlite.org/) installed on it.  

There are two notable resources from the sqlite documentation that you may refer to often:
1. [SQL Syntax](http://sqlite.org/lang.html)
2. [sqlite dot-commands](http://sqlite.org/cli.html#special_commands_to_sqlite3_dot_commands_)

You can also [download all of the documentation](http://sqlite.org/2018/sqlite-doc-3220000.zip) to your computer for offline access.  (This documentation was included in the database software that I shared with your via flash drive, so you may already have it on your computer.  **See if you can open it and view the documentation offline.**)

I have one important word of advice before we get started.  **Spelling Matters**.  If you make typographic errors, you will not get the output you expect.  You should follow the tutorial carefully.  If you are not able to touch-type, you should also practice typing.

With that out of the way, let's get started.

# 1. Open the Command Prompt
Open the command prompt.  You can find this in the start menu.  For quickest access, hit the Windows Key and type cmd and enter.

The command prompt should open up.  

In this tutorial I will identify the command prompt commands in this way:

```shell
$>
```

and I will identify the sqlite shell in this way:

```sqlite
sqlite>
```

The commands that you will type will be shown after the ">".

The command prompt will allow you to issue command-line commands to Windows, while the sqlite shell will allow you to run SQL queries and other related functions.

Try entering this in the command prompt:

```shell
$>dir
```

What is the output? It should show you the contents of the folder in whic you are located.

# 2. Opening and Closing the sqlite Shell
Now, open sqlite from the command like this:

```sqlite
$>sqlite3
```

An output like this should result:

```sqlite
SQLite version 3.19.3 2017-06-27 16:48:08
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite>
```

Exit the sqlite shell like this:

```sqlite
sqlite>.exit
```

This will put you back at the command prompt.

Re-open the sqlite shell with:

```shell
$>sqlite3
```

# 3. Help!

At the sqlite shell, you can enter SQL queries.  But sqlite also has its own "dot-commands" for doing things like listing all tables (`.tables`), listing the schema (`.schema`), save the current database (`.save`), exiting the application (`.exit`).  You can also get information about the basic dot-commands like this:

```sqlite
sqlite>.help
```

Try it out.  Can you find the command to list the names and files of attached databases?

When you've completed this, move on to [Exercise 2b](exercise2b).
