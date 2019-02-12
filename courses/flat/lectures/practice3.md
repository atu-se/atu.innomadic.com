---
title: Formal Languages & Automata Theory
subtitle: RE Practice
date: February 11, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: "./practice3-html.html"
    pandoc_args: ["-t", "revealjs", "-V",  "revealjs-url=../../../presentation/revealjs", "--standalone"]
---

# Regular Expression Practice

[Reference: Aduni](http://www.aduni.org/courses/theory/courseware/handouts/Recitation_03.html)

*Give one string that is in the language and one that is not:*

1.  `a*b*`
2.  `a(ba)*b`
3.  `a* + b*`
4.  `(b + aaa)*`
5.  `aba+bab`

*Write a regular expression*

6.    That accepts the set of all strings.

7.    That accepts the set of all strings not containing 00 as a substring.



*Convert to regular expressions:*

8.
```dot
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q3;
    node [shape = point ]; qi

    node [shape = circle];
    qi -> q1;
    q1  -> q2 [ label = "a" ];
    q2  -> q3 [ label = "b" ];
}
```

9.
```dot
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q3;
    node [shape = point ]; qi

    node [shape = circle];
    qi -> q1;
    q1  -> q2 [ label = "a" ];
    q2  -> q2 [ label = "c" ];
    q2  -> q3 [ label = "b" ];
}
```


10.
```dot
digraph finite_state_machine {
    rankdir=LR;
    size="8,5"

    node [shape = doublecircle]; q3, q4;
    node [shape = point ]; qi

    node [shape = circle];
    qi -> q1;
    q1  -> q2 [ label = "a" ];
    q2  -> q2 [ label = "c" ];
    q2  -> q3 [ label = "b" ];
    q2  -> q4 [ label = "d" ];
}
```

*Convert to an NFA:*

11.  `(001)*(1+e)`
12.  `(01*0 + e + 00)`
13.  `(001)*(1+e)(01*0 + e + 00)`

*Short Answer*

14. How long does a string in the following language have to be before we are guaranteed to have a loop?
15. Is the set of all strings that are palindromes regular? Why or why not?
16. Show that the set of all strings of zeros that have length that is a perfect cube can not be described by a regular expression.
