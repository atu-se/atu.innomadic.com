---
title: FLAT
subtitle: 1. Regular Languages
date: October 5, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture2-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "theme=white", "-V", "revealjs-url=../../../presentation/reveal.js", "--slide-level=2", "--standalone"]
---

<style> 
.container{
    display: flex;
}
.col{
    flex: 1;
}
</style>

# Languages

# Languages

* Definition: A *language* is a set of strings over some alphabet
* Examples:
    * $L_1 = \{ 0, 1, 10, 1110001\}$
    * $L_2 = \{ 0^m1^n | n, m\ are\ positive\ integers\}$
    * $L_3 = \{\text{bit strings whose binary value is a multiple of 4}\}$

# Languages 

* A language of an FA, $M, L(M)$, is the set of words (strings) that $M$ *accepts*
* If $L_a = L(M)$ we say that M *recognizes* $L_a$
* *If $L_a$ is recognized by some finite automaton A, $L_a$ is a regular language*

# Questions 

* Q1: How do you prove that a language $L_a$ is regular?
* A1: By presenting an FA, $M$, satisfying $L_a = L(M)$
* Q2: How do you prove that a language $L_a$ is not regular?
* A2: Hard! to be answered on later in the course.
* Q3: Why is it important?
* A3: Recognition of a regular language requires a controller with bounded memory.

# Regular Operations

* Just as we have arithmetical operations and set operations, regular languages also have operations.
    * Union
    * Concatenation
    * Star

# Regular Operations

* Let A and B be 2 regular languages over the same alphabet, $\Sigma$.  We define the 3 regular operations:
    * Union: $A \cup B = \{ x | x \in A\ or\ x \in B\}$
    * Concatenation: $A \circ B = \{ xy | x \in A\ and\ y \in B\}$
    * Star: $A^* = \{ x_1, x_2, ..., x_k | k \geq 0\ and\ x_k \in A\}$

# Regular Operations

* Given a language one can verify it is regular by
presenting an FA that accept the language.
* Regular operations give us a systematic way of constructing languages that are known to be regular. No verification is required.
 
# Regular Operations

* $A = \{good, bad \}$
* $B = \{girl, boy\}$
* $A \cup B =\{good, bad, girl, boy\}$
* $A \circ B = \{goodgirl, goodboy,badgirl,badboy\}$
* $A^* = \{ \epsilon , good , bad , goodgood , goodbad, goodgoodgoodbad, badbadgoodbad,...\}$

# Theorem

* The class of Regular languages, above the same alphabet, is closed under the union operation. 
* Meaning: The union of two regular languages is Regular.

# Example

* Consider:
    $$L_1 =\{w | \text{w starts with 1}\}, L_2 =\{w | \text{w ends with 0}\}$$
* The union set is the set of all bit strings that either start with 1, or end with 0.
* Each of these sets can be recognized by an FA with 3 states.
* Can you construct an FA that recognizes the union set?
 
# Proof idea

* If $A_1$ and $A_2$ are regular, each has its own recognizing automaton $N_1$ and $N_2$ , respectively.
* In order to prove that the language $A_1 \cup A_2$
is regular we have to construct an FA that accepts exactly the words in $A_1 \cup A_2$ .
* Note: $N_1$ followed by $N_2$ doesn’t work.


# Proof idea

* We construct an FA that *simulates* the
computations of, N~1~ and N~2~ simultaneously.
* Each state of the simulating FA represents a pair of states of N~1~ and of N~2~
respectively.
* Can you define the transition function and the final state(s) of the simulating FA?
 
# Wrap-Up

* We introduced the idea of *regular languages*
* We taught the three *regular operations*
    * Union
    * Concatenation
    * Star
* We showed how to prove that a language is regular
* We taught that regular languages are *closed* under *union*

# References, Resources

* [ADUni.org Lectures](https://www.youtube.com/playlist?list=PL601FC994BDD963E4)
* [UC San Diego Lecture Slides](https://cseweb.ucsd.edu/classes/fa08/cse105/)