# Definitions

Below I have highlighted definitions, terms, theorems, corollaries, etc. from our textbook for your convenience.  You should know all of these terms very well.

# Definition 1.5: Finite Automaton
A finite automaton is a 5-tuple (Q, Σ, δ, q<sub>0</sub>, F ), where
1. Q is a finite set called the states,
2. Σ is a finite set called the alphabet,
3. δ : Q × Σ → Q is the transition function,1 4. q<sub>0</sub> ∈ Q is the start state, and
5. F ⊆ Q is the set of accept states.

# Definition 1.16: Regular Language
A language is called a regular language if some finite automaton recognizes it.

# Definition 1.23: Regular Operations
Let A and B be languages. We define the regular operations union,
concatenation, and star as follows:

| Operation     | Definition                                                                           |
|---------------|--------------------------------------------------------------------------------------|
| Union         | A∪B = { x\| x ∈ A or x ∈ B}                                                              |
| Concatenation | A◦B = { xy \| x ∈ A and y ∈ B }                                                          |
| Star          | A* ={x<sub>1</sub>x<sub>2</sub>...x<sub>k</sub> \| k≥0 and each x<sub>i </sub> ∈ A } |


# Theorem 1.25
The class of regular languages is closed under the union operation.
In other words, if A<sub>1</sub> and A<sub>2</sub> are regular languages, so is A<sub>1</sub> ∪ A<sub>2</sub>.


# Theorem 1.26
The class of regular languages is closed under the concatenation operation.
In other words, if A<sub>1</sub> and A<sub>2</sub> are regular languages then so is A<sub>1</sub> ◦ A<sub>2</sub>.

# Definition 1.37: Nondeterministic Finite Automaton
A nondeterministic finite automaton is a 5-tuple (Q,Σ,δ,q0,F),
where
1. Q is a finite set of states,
2. Σ is a finite alphabet,
3. δ : Q × Σ<sub>ε</sub> → P (Q) is the transition function, 4. q<sub>0</sub> ∈ Q is the start state, and
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
4. (R<sub>1</sub> ∪ R<sub>2</sub>), where R<sub>1</sub> and R<sub>2</sub> are regular expressions,
5. (R<sub>1</sub> ◦ R<sub>2</sub>), where R<sub>1</sub> and R<sub>2</sub> are regular expressions, or
6. (R<sub>1</sub>∗), where R<sub>1</sub> is a regular expression.

In items 1 and 2, the regular expressions *a* and ε represent the languages {*a*} and {ε}, respectively. In item 3, the regular expression ∅ represents the empty language. In items 4, 5, and 6, the expressions represent the languages obtained by taking the union or concatenation of the languages R<sub>1</sub> and R<sub>2</sub>, or the star of the language R<sub>1</sub>, respectively.
