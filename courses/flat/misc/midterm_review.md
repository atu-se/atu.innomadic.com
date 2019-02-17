# Midterm Review

## Topics Covered

* The midterm exam will cover Chapter 0 and Chapter 1
  - the material will especially focus on Chapter 1
  - However, Chapter 0 has foundation material from Discrete Mathematics with which you should be familiar.

## Topics Not on Exam



- You will not have problems directly related to graphs (Covered in Section 0.2)
- You will not have to *write* a proof (Section 0.4), though you should understand the theorems that have been proven in the textbook or in lecture

## Outline of Notable Topics


- 0.1
  - Automata Theory
  - Complexity Theory
  - Computability Theory
- 0.2
  - Sets
    - Subsets
    - Intersection
    - Union
    - Complement
    - power set
    - Cartesian product / cross product
  - Sequences
  - Tuples
  - Functions and Relations
    - Function
    - Domain
    - Range
  - Strings and Languages
    - alphabet
    - symbols
    - a string over an alphabet
    - length
    - empty string
    - reverse
    - substring
    - concatenation
  - Boolean Logic
  - Notation
    - $\mathbb{N}$
    - $\mathbb{Z}$
    - $\epsilon$
    - $\emptyset$
    - $\cup$
    - $\cup$
    - $\subset$
    - $\subseteq$
    - $\supset$
    - $\supseteq$
    - $\times$
    - $\in$
    - $\notin$
    - $\Sigma$
    - \|w|
  - 1.1
    - Definition 1.5 - finite automaton
    - Definition 1.16 - regular language
    - Definition 1.23 - Regular Operations of Languages
      - Union
      - Concatenation
      - Star
    - states
    - transition function ($\delta$)
      - understand how to document a transition function in three ways:
        - a list, e.g. () $\delta$ (A, 1) $\longrightarrow$ B, $\delta$ (A, 0) $\longrightarrow$ A, $\delta$ (B, 0) $\longrightarrow$ B, $\delta$ (B, 1) $\longrightarrow$ B )
        - or as a transition table,
        - or you can represent it in a state diagram
    - Notation
      - $\circ$
      - $\cup$
      - $\ast$
      - $\delta$
    - Understand the complement of a language and the complement of a finite automata.
  - 1.2 Nondeterminism
    - Nondeterminism vs. determinism
    - Definition 1.37 - NFA
    - Theorem 1.39 - Equivalence of NFAs and DFAs
    - Corollary 1.40 - Regular Languages and NFAs
    - Theorem 1.45 Closure Under Union
    - How to construct an NFA to recognize union (e.g. A $\cup$ B)
    - Theorem 1.47 Closure under concatenation
    - How to construct an NFA to recognize concatenation (e.g. A $\circ$ B)
    - Theorem 1.49 Closure under star
    - How to construct an NFA to recognize star (e.g. A$^{\ast}$)
    - Notation
      - { w | w is has a substring of ... }
      - { w | w is has a ends with ... }
      - { w | w is has a starts with ... }
      - { w | w is is of length... }
      - { w | w is has has at most / at least / exactly X $\sigma$'s }
      - { w | w has an odd/even number of $\sigma$'s}
      - { w | w ... }
  - 1.3 Regular Expressions
    - Definition 1.52 Regular Expressions
    - Theorem 1.54 Regular Languages and Regular Expressions
    - Lemma 1.55 Regular Languages and Regular Expressions
    - Know how to convert a regular expression to an NFA
    - Lemma 1.60 Regular Languages and Regular Expressions
    - Definition 1.64 GNFA
    - Know how to convert an DFA to a GNFA
    - Know how to convert a GNFA to a regular expression
    - Notation
      - $\circ$
      - $\cup$
      - $\ast$
      - $\Sigma$
      - $\epsilon$
      - $\emptyset$
      - L(R)
    - 1.4 Nonregular languages
      - Know the difference between a regular and non-regular language
      - Know the relationship between non-regular languages and finite automata
      - Understand the basic premise of the Pumping Lemma: *if the length of a string in a regular language exceeds the number of states in its corresponding finite automaton, there must be a loop.  This loop can be repeated ("pumped") to produce other strings in the language.*


## Some study tips

* Reread Chapters 0 and 1
* Study past homework
* Study practice exercises
* Study quizzes
* Work additional problems from textbook
* Review all notation
* Review all theorems, definitions, corollaries, lemmas
* Study lectures and notes
* Master these topics
  * Understand the relation between NFAs, DFAs, Regular Expressions, and Regular languages
  * Be able to formally define NFAs and DFAs
  * Understand the differences between NFAs and DFAs
  * Understand how to do computation with FAs (how determine whether the machine accept or rejects a word)
  * Be able to record the sequence of states an FA goes through given an input word
  * Be able to design FAs given a language
  * Be able to draw a state diagram given a formal definition of a FA
  * Be able to construct a formal definition of an FA given a state diagram
  * Be able to define a language given an FA or a Regular Expression
  * Be familiar with the formal notation for a language
