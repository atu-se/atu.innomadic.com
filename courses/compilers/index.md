*Lectures Adapted from Stanford Compilers*

# 23-Apr-2018

* *Announcement*: There will be a quiz covering the introductory lessons to parsing (lectures through 22-Apr-2018).  You should study *Engineering a Compiler* chapter 3.
* *New Assignments*:  Complete Exercise 1 and Exercise 2.  These are graded solo assignments, though you may consult with your peers for help.  The source files which are found in the git repository for the class.  Use the instructions for cloning the git [repository here](exercises/exercise1).  You may complete the exercise by showing your instructor your working output with the modifications listed below:
  * Exercise 1: Modify the flex specification file (exercise1.l) so that when the user inputs *teacher*, the program will output *nick*.  When the user inputs *for*, the program will output *keyword*
  * Exercise 2: Modify the flex specification file (exercise2.l) so that it also counts the number of a's in the user input and prints them in the summary after the user enters *Control+D* to close the application.  It should still print out the number of lines and number of characters.
  * To do these exercises you will become familiar with some aspects of:
    - the Linux shell
    - an SSH client (Putty)
    - the *nano* text editor
    - *gcc*
    - *flex*
  * Do you want to run these exercises on your own computer?  The easiest method may be installing Linux or, perhaps better, running a Linux virtual machine.  You will want to install flex, gcc, and bison, if they are not already available.

# 22-Apr-2018

* Announcement:  Quiz tomorrow on Lexical Analysis and Syntax Analysis
  - Including all lecture material:
    - Engineering a Compiler - Chapters 1-2
    - Compilers: Principles, Techniques, and Tools - Chapter 3
* Reading Assignment:
  - Engineering a Compiler - Chapters 3
  - Compilers: Principles, Techniques, and Tools - Chapter 1, Chapter 4.1-4.3
* Today's [Practical Lab 1](exercises/exercise1)

# 16-Apr-2018

* [Lecture 3 - Syntax Analysis](lectures/Slides02.pdf)

# 9-Apr-2018
* Practical Exercises
  - Today we continued in lecture 2 linked below
  - [Exercise 1](exercises/exercise1/sample1.lex)
  - [Exercise 2](exercises/exercise2/sample2.lex)
  - [Flex/Bison Tutorial](http://www.capsl.udel.edu/courses/cpeg421/2012/slides/Tutorial-Flex_Bison.pdf)

# 7-Apr-2018
* [Lecture 1 - Introduction](lectures/Slides00.pdf)
* [Lecture 2 - Lexical Analysis](lectures/Slides01.pdf)
* Assigned Reading:
  - Engineering a Compiler - Chapters 1-2
  - Compilers: Principles, Techniques, and Tools - Chapter 3
  - [Handout: Introduction to Flex](handouts/050 Flex In A Nutshell.pdf)
* Supplemental Reading
  - [Handout: Lexical Analysis](handouts/040 Lexical Analysis.pdf)
* Please prepare your computer for practical exercises by installing [Flex and Bison](https://sourceforge.net/projects/winflexbison/files/win_flex_bison3-latest.zip/download).
