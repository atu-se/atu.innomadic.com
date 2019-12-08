---
title: FLAT
subtitle: 8b. PDA Equivalence Properties
date: November 23, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture8b-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "theme=white", "-V", "revealjs-url=../../../presentation/reveal.js", "--slide-level=1", "--standalone", "--katex=../../../presentation/katex/"]
---

<style>
.ninety {
   font-size: 90%;
}

.eighty {
   font-size: 80%;
}

.seventy {
   font-size: 70%;
}

.container{
    display: flex;
}
.col{
    flex: 1;
}
</style>

# Review 



# Properties of Pushdown Automata

# Theorem 2.20

>A language is context free if and only if some pushdown automaton recognizes it.

# CFG Equivalence

## Lemma 2.21

>If a language is context free, then some pushdown automaton recognizes it.

# CFG Equivalence

## Lemma 2.27

>If a pushdown automaton recognizes some language, then it is context free.

# Proof Idea

Let's attempt to prove the first half of the theorem, Lemma 2.21:

>If a language is context free, then some pushdown automaton recognizes it.

# Proof Idea

* Since L is a CFL there exists a CFG G such that L = L(G). 
* We will present a PDA P that recognizes L.
* The PDA P starts with a word $w \in \Sigma*$ on its input
* In order to decide whether $w \in L(G)$, P simulates the erivation of w.

# Proof Idea

* Recall that a derivation is a sequence of strings, where each string contains variables and terminals
* The first string is always the start symbol of G and each string is obtained from the previous one by a single activation of some rule. 

# Proof Idea

* A string may allow activation of several rules and the PDA  P  non deterministically guesses the next rule to be activated.
* The initial idea for the simulation is to store each intermediate string on the stack. 
* Upon each production, the string on the stack is before production is transformed to the string after production.

# Proof Idea

* Unfortunately, this idea does not quite work since at any given moment, P can only access the top symbol on the stack.
* To overcome this problem, the stack holds only a suffix of each intermediate string where the top symbol is the variable to be substituted during the next production. 

# Intermediate string aaSbb

![aaSbb](images/lecture8b-diagram1.png){.stretch}


# Informal Description of P

1. Push the marker $ and the start symbol S on the stack
2. Repeat:
    * If the top symbol is a variable V, replace V by the right hand side of some non-deterministically chosen rule whose left hand side is V
    * ...
    
# Informal Description of P    

1. Push the marker $ and the start symbol S on the stack
2. Repeat:
    * ...
    * If the top symbol is a terminal compare it with the next symbol on the input. If equal – advance the input and pop the variable else – reject.

# Informal Description of P    

1. Push the marker $ and the start symbol S on the stack
2. Repeat:
    * ...
    * If the top symbol is $ and the input is finished – accept  else – reject  

# The Proof

* We start by defining *extended transitions*
* Assume that PDA P is in state q, it reads $a \in \Sigma$ from the input and pops $s \in \Gamma$ from the stack and then moves to state r while pushing $u = u_1, u_2, ... u_l$ onto the stack.
* This is denoted by $(r,u) \in \delta (q, a, s)$
* Next, extended transitions are implemented.

# Extended Transitions {.ninety}

* Add states $q_1, q_2, ..., q_l-1$
* Set the transition function $\delta$ as follows:
    * Add $(q_1, u_l)$
    * Set $\delta(q_1, \epsilon, \epsilon) = \{q_2, u_{l-1}\}$
    * Set $\delta(q_2, \epsilon, \epsilon) = \{q_2, u_{l-2}\}$
    * ...
    * Set $\delta(q_{l-1}, \epsilon, \epsilon) = \{r, u_1\}$

# Extended Transitions

![$(r,xyz) \in \delta(q,a,s)$](images/lecture8b-diagram2.png){.stretch}

# The Proof

* Let G be an arbitrary CFG. Now we are ready to construct the PDA, P such that that
$$L(P) = L(G)$$           
* The states of P are $Q = \{q_{start}, q_{loop}, q_{accept}\} \cup E$, where E contains all states needed to implement the extended transitions presented in the previous slide
* The PDA P is as follows

# Resulting PDA

![This PDA completes the proof](images/lecture8b-diagram3.png){.stretch}

* So, if we have a context-free language L, there is a pushdown automaton P which recognizes it.

# Example 

Consider the following context-free grammar G:

$$S \longrightarrow aTb\ |\ b \\ T \longrightarrow Ta\ |\ \epsilon$$

Let us use the proof from this lemma to produce an equivalent DFA.




# CFLs and Regular Languages

> Every regular language is context free.

![Diagram 3](images/lecture8-diagram3.png){.stretch}




# Correlations 

.                       | Regular Languages           | Context-Free Languages
------------------------|-----------------------------|-----------------------
**Language Recognizer** | Finite Automaton (NFA, DFA) | Pushdown Automaton
**Language Generator**  | Regular Expression          | Context-Free Grammar


# References, Resources

* [ADUni.org Lectures](https://www.youtube.com/playlist?list=PL601FC994BDD963E4)
* [UC San Diego Lecture Slides](https://cseweb.ucsd.edu/classes/fa08/cse105/)

# Review of Properties of PDAs and CFLs

