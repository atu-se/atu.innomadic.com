---
title: Formal Languages & Automata Theory
subtitle: DFA Practice
date: October 4, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: "./practice1-slides.html"
    pandoc_args: ["-t", "revealjs", "-V",  "theme=white", "-V",  "revealjs-url=../../../presentation/reveal.js", "--standalone"]
---

# DFA Practice

Design a DFA for each of the languages below.  For each language, $\Sigma$ = {0, 1}.

1. { w | w has at least two 1’s }
2. { w | w contains a substring *101*}
3. { w | w has an odd number of 1’s }
4. { w | was has an even length }
5. { w | w starts with an 0 }

# DFA Practice 

6. { w | w starts with an 0 and has at most two 1's}
7. { w | w has an odd number of 1’s and one or two 0’s}
8. { w | w has at least two 1’s and at least three 0’s}
9. { w | w has even length and an even number of 1’s}
