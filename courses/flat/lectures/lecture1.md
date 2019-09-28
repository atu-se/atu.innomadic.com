---
title: FLAT
subtitle: 1. Finite Automata and Regular Langauges
date: September 28, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture1-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "theme=white", "-V", "revealjs-url=../../../presentation/reveal.js", "--slide-level=2", "--standalone"]
---

# Course Information


## Essentials

* Formal Language & Automata Theory (FLAT)
* Course Website - [atu-se.github.io/courses/flat](https://atu-se.github.io/courses/flat/)
* Primary Textbook - Introduction to the Theory of Computation, 3rd Edition (Sipser)]
* Lectures built around [UC San Diego Lectures](https://cseweb.ucsd.edu/classes/fa08/cse105)

## Meeting Times


## How to Succeed

* Attend all lectures
* Take notes (not all materials will be distributed as slides)
* Ready and study your textbook
* Do all assignments
* Ask questions
* Work many practice problems

## Academic Integrity

* Read the academic integrity policy in the syllabus
* You are encouraged to discuss the topics among yourselves.
* Unless otherwise noted, your work should be your own and you should not share your work with others
* Copying or cheating on homework, exams, etc. may result in failing grades

# Finite Automata and Regular Languages

## Introduction

Computer Science stems from two starting points:

* Mathematics -- What can be be computed? (And what _cannot_ be computed?)
* Electrical Engineering -- How can we build computers?

This course focuses on the first question

## Introduction

* Computability Theory deals with the mathematical basis for Computer Science, yet it has some interesting practical ramifications
that I will try to point out sometimes.
* The questions we will try to answer in this course are:
    * What can be computed? 
    * What cannot be computed
    * Where is the line between the two?”

## Computational Models

* A Computational Model is a mathematical object (defined on paper) that enables us to reason about computation and to study the properties and limitations of computing.
* We will deal with three principal computational models in increasing order of Computational Power.

## Computational Models

We will deal with three principal models of computations:
1. Finite Automaton (in short FA) -- recognizes Regular Languages
2. Push-down or Stack Automaton -- recognizes Context Free Languages
3. Turing Machine (in short TM) -- recognizes Computable Languages 

## Alan Turing - A Short Detour

Dr. Alan Turing is one of the founders of Computer Science (he was an English Mathematician)

1. “Invented” Turing machines.
2. “Invented” the Turing Test.
3. Broke the German submarine transmission coding machine “Enigma”.
4. The movie Imitation Game is loosely based on his life.

# Finite Automaton Example

## Washing Machine

* The control of a washing machine is a very simple example of a finite automaton.
* The most simple washing machine accepts quarters and operation does not start until at least 3 quarters were inserted.
* Credit: Vadim Lyubasehvsky

## Coins

Washing machines take coins.  Our machine costs $0.75 to operate.  We will use this notation:

* Q = Quarter (0.25)
* H = Half-dollar (0.50)
* D = Dollar (1)

## Washing Machine 1

* Accepts Three Quarters
* Put in three (or more quarters) -- it begins operation
* Put in less -- it does nothing

## Washing Machine 1 

```dot 
digraph G{
    null [label= "", shape=none]
    null -> 0.00
    0.00 -> 0.25 [label="Q"]
    0.25 -> 0.50 [label="Q"]
    0.50 -> 0.75 [label="Q"]
    0.75 -> 0.75 [label="Q"]
}
```

## Washing Machine 2

* Now imagine we have a more advanced machine which can accept both quarters (Q) and half-dollars (D).  
* How does the automata change?

## Washing Machine 2


## Washing Machine 2

```dot 
digraph G{
    null [label= "", shape=none]
    null -> 0.00
    0.00 -> 0.25 [label="Q"]
    0.25 -> 0.50 [label="Q"]
    0.50 -> 0.75 [label="Q, H"]
    0.75 -> 0.75 [label="Q, H"]
    0.00 -> 0.50 [label="H"]
    0.25 -> 0.75 [label="H"]
}
```

## Washing Machine 3

```dot 
digraph G{
    null [label= "", shape=none]
    null -> 0.00
    0.00 -> 0.25 [label="Q"]
    0.25 -> 0.50 [label="Q"]
    0.50 -> 0.75 [label="Q, H, D"]
    0.75 -> 0.75 [label="Q, H, D"]
    0.00 -> 0.50 [label="H"]
    0.25 -> 0.75 [label="H, D"]
    0.00 -> 0.75 [label="D"]
}
```