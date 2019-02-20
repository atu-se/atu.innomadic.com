# Assignment 1

## Overview
Assignment one is worth **5 marks** for the semester.

You will modify [Case Study 20.7](MultipleBounceBall.java) as specified below.

## Group Work Requirements

**For this exercise you may work alone or in groups of two.  You may not discuss or share your solution with other students or other groups.  If cheating is detected, all involved parties may receive a failing grade.**

## Specification and Rubric

First, examine, compile, and run the code.  Study the code to understand how it works.  You may wish to modify parts of the code to see how it works.  

Then, make the following changes to the code:

1. **1 Mark** Modify the code to remove the first ball in the list when the button is clicked, instead of the last ball.
2. **1 Mark** Modify the code so that that each ball will get a random radius between 10 and 20?
3. **1 Mark** Create a new button labeled "++" that adds two balls at the same time.  
   - Choose a number between 50 and 60.  
   - Make the (x,y) coordinates of the second ball begin at the number you chose -- for x and y.  
   - For example, if your number was 100, then the ball would start at x=100, y=100.  Your numbers should be between 50 and 60.
4. **1 Mark** Create a new button labeled "Clear".  When this button is pressed it should call a recursive method which will remove the balls from the data structure one by one.
    - Hint: your function signature should look like this: `public void clear()`
5. **1 Mark** Create a new button labeled "Color".  When "Color" is selected
    - Hint: use the moveBall function as an example of how to iterator over the list of Balls in order to change their colors.
    - Choose a color from the [Color class](https://docs.oracle.com/javafx/2/api/javafx/scene/paint/Color.html).
    - Ball extends the [Circle class](https://docs.oracle.com/javase/8/javafx/api/javafx/scene/shape/Circle.html).  
    - Note that Circle has a [setFill() function](https://docs.oracle.com/javase/8/javafx/api/javafx/scene/shape/Shape.html#setFill-javafx.scene.paint.Paint-).  You will need to use the `setFill` function and you will need to define a new Color (see the `add()` function for how to create a color).
6. Your submission should compile and run using Java Runtime 1.8

## Submission Requirements


1. Add a comment near the top of your java file with "Group: <yourname> <otherpersonsname>" (if you worked alone, just put your name).
2. Add a comment near the top of your java file with a line that says Assignment 1
3. Attach your java file to an email
4. In the body of your email, list your name as it is written on the class roster.
5. Email it to your instructor by the deadline.  Late work **may be** considered for **reduced credit**.
