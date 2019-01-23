# Definitions

Below I have highlighted definitions, terms, theorems, corollaries, etc. from our textbook for your convenience.  You should know all of these terms very well.

# Definition 1.5: Finite Automaton
A finite automaton is a 5-tuple (Q, Σ, δ, q0, F ), where
1. Q is a finite set called the states,
2. Σ is a finite set called the alphabet,
3. δ : Q × Σ−→ Q is the transition function,1 4. q~0~ ∈ Q is the start state, and
5. F ⊆ Q is the set of accept states.

# Definition 1.16: Regular Language
A language is called a regular language if some finite automaton recognizes it.

# Definition 1.23: Regular Operations
Let A and B be languages. We define the regular operations union,
concatenation, and star as follows:
* Union: A∪B = { x| x∈A or x∈B}
* Concatenation: A◦B = { xy | x∈A and y∈B }
* Star: A* ={x~1~x~2~...x~k~ | k≥0 and each x~i~ ∈A }


# Theorem 1.25
The class of regular languages is closed under the union operation.
In other words, if A~1~ and A~2~ are regular languages, so is A~1~ ∪ A~2~.


# Theorem 1.26
The class of regular languages is closed under the concatenation operation.
In other words, if A~1~ and A~2~ are regular languages then so is A~1~ ◦ A~2~.

# Definition 1.37: Nondeterministic Finite Automaton
A nondeterministic finite automaton is a 5-tuple (Q,Σ,δ,q0,F),
where
1. Q is a finite set of states,
2. Σ is a finite alphabet,
3. δ : Q × Σ~ε~ −→ P (Q) is the transition function, 4. q~0~ ∈ Q is the start state, and
5. F ⊆ Q is the set of accept states.


# Theorem 1.39
Every nondeterministic finite automaton has an equivalent deterministic finite automaton.

# Corollary 1.40
A language is regular if and only if some nondeterministic finite automaton recognizes it.

# Theorem 1.45
The class of regular languages is closed under the union operation.

# Theorem 1.47
The class of regular languages is closed under the concatenation operation.

# Theorem 1.49
The class of regular languages is closed under the star operation.


# Definition 1.52: Regular Expression
Say that R is a regular expression if R is
1. *a* for some *a* in the alphabet Σ,
2. ε,
3. ∅,
4. (R~1~ ∪ R~2~), where R~1~ and R~2~ are regular expressions,
5. (R~1~ ◦ R~2~), where R~1~ and R~2~ are regular expressions, or
6. (R~1~∗), where R~1~ is a regular expression.

In items 1 and 2, the regular expressions *a* and ε represent the languages {*a*} and {ε}, respectively. In item 3, the regular expression ∅ represents the empty language. In items 4, 5, and 6, the expressions represent the languages obtained by taking the union or concatenation of the languages R~1~ and R~2~, or the star of the language R~1~, respectively.
