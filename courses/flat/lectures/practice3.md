---
title: Formal Languages & Automata Theory
subtitle: NFA Proof Practice
date: October 12, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: "./practice3-slides.html"
    pandoc_args: ["-t", "revealjs", "-V",  "theme=white", "-V",  "revealjs-url=../../../presentation/reveal.js", "--standalone" , "--katex=../../../presentation/katex/"]
---

# NFA Practice  

$$
\begin{aligned}
  A &= \{ w | w \text{ ends in ab }\} \\
  B &= \{ w | w \text{ contains a substring } aba\} \\ 
  C &= \{ w | w \text{  as an odd number of } a’s \} \\ 
\end{aligned}
$$

1. Construct an NFA that will recognize  $A \cup B$
2. Construct an NFA that will recognize  $A \cup C$
3. Construct an NFA that will recognize  $B \cup C$

# NFA Practice 

$$
\begin{aligned}
  A &= \{ w | w \text{ ends in ab }\} \\
  B &= \{ w | w \text{ contains a substring } aba\} \\ 
  C &= \{ w | w \text{  as an odd number of } a’s \} \\ 
\end{aligned}
$$

1. Construct an NFA that will recognize  $A \circ B$
2. Construct an NFA that will recognize  $B \circ A$
3. Construct an NFA that will recognize  $A \circ C$

# NFA Practice 

$$
\begin{aligned}
  A &= \{ w | w \text{ ends in ab }\} \\
  B &= \{ w | w \text{ contains a substring } aba\} \\ 
  C &= \{ w | w \text{  as an odd number of } a’s \} \\ 
\end{aligned}
$$

1. Construct an NFA that will recognize  $A^*$
2. Construct an NFA that will recognize  $B^*$
3. Construct an NFA that will recognize  $C^*$
