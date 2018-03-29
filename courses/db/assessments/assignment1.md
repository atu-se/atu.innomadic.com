# Assignment 1

For Assignment #1 you may work individually or in pairs.  Although you may discuss the problem set in general, you may *not* copy another person or group's work.  Consequences for those caught cheating will be harsh.  When you submit your assignment, clearly identify whether you are working alone or as a pair, and list the full name of the team member(s).

## Specification

Design and draw an ER diagram that captures the information about the university as described below. Use only the basic ER model here; that is, entities, relationships, and attributes. Be sure to indicate any key and participation constraints.

1. Professors have an identifier number, a name, an age, a rank, and a research specialty.
2. Projects have a project number, a sponsor name (e.g., NSF), a starting date, an ending date, and a budget.
3. Graduate students have an identifier number, a name, an age, and a degree program (e.g., M.S. or Ph.D.).
4. Each project is managed by one professor (known as the project’s principal investigator).
5. Each project is worked on by one or more professors (known as the project’s co-investigators).
6. Professors can manage and/or work on multiple projects.
7. Each project is worked on by one or more graduate students (known as the project’s research assistants).
8. When graduate students work on a project, a professor must supervise their work on the project. Graduate students can work on multiple projects, in which case they will have a (potentially different) supervisor for each one.
9. Departments have a department number, a department name, and a main office.
10. Departments have a professor (known as the chairman) who runs the department.
11. Professors work in one or more departments, and for each department that they work in, a time percentage is associated with their job.
12. Graduate students have one major department in which they are working on their degree.
13. Each graduate student has another, more senior graduate student (known as a student advisor) who advises him or her on what courses to take.

## ER Constraint Designation
* If an entity has at *most* one participant in a relationship (i.e. a key constraint), you should indicate this with an arrow from the entity to the relationship.  See textbook figure 2.6
* Key fields should be identified by underlining the attribute name.  The *did* field in figure 2.6 is an example of this.
* If the participation of an entity set in a relationship is **total**, the line between the entity and the relationship should be a **bold line**.  See for example figure 2.20, in which *Projects* participates totally in *Sponsors2*.
* In a *weak entity set*, draw a bold arrow between the weak entity and its identifying relationship.  Also draw the weak entity and its identifying relationship in bold rectangles.  The partial key in the weak entity set should be underlined with a dotted underline.  See figure 2.11 for an example of this.

## Style Requirements
* When creating identifier numbers, use a descriptive name such as "professor_id".
* Use lower-case for all attribute names.  Separate words with underscores.  e.g. use "professor_id" instead of "professorid".
* You may the diagram neatly by hand, or you may use an application such as Microsoft Word or another tools to help you draw the diagram.
* Email a PDF or a JPG of your assignment by
  * Morning Section: Tuesday, March 27 @ 9:00 a.m.
  * Evening Section: Tuesday, March 27 @ 12:00 p.m.
* The grades/marks on assignments sent after 9:00 a.m. on Tuesday will be reduced by 10% on the first day, and subsequent days late will receive additional penalties.
