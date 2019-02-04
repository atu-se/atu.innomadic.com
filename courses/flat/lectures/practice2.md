---
title: Formal Languages & Automata Theory
subtitle: NFA Practice
date: February 2, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: "./practice2.html"
    pandoc_args: ["-t", "revealjs", "-V",  "revealjs-url=../../../presentation/revealjs", "--standalone"]
---

# NFA Practice

Design an NFA for each of the languages below.  For each language, $\Sigma$ = {a, b}.

1. { w \| w ends in ab }
2. { w \| w contains a substring *aba*}
3. { w \| w has an odd number of a’s }
4. { w \| w has an even length }
5. { w \| w starts with an a }
6. { w \| w's third symbol from the end is a b}

# NFA Practice
7. Identify the language in the following NFA:

```dot
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; 2;
    node [shape = point ]; qi

    node [shape = circle];
    qi -> 0;
    0  -> 2 [ label = "a" ];
    0  -> 1 [ label = "a" ];
    1  -> 2 [ label = "b" ];
}
```

# NFA Practice 

8. Identify the language in the following NFA:



```dot
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; 3;
    node [shape = point ]; qi

    node [shape = circle];
    qi -> 0;
    0 -> 0 [label="a"];
    0  -> 1 [ label = "a" ];
    0  -> 2 [ label = "b" ];
    0  -> 3 [ label = "b" ];
    2  -> 3 [ label = "a"];
    1  -> 3 [ label = "b" ];
    3  -> 1 [ label = "b" ];

}
```
