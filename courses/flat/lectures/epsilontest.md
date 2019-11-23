---
title: epsilon test
---

# Something 
```
try to run with:
pandoc -o test.html -t revealjs -V revealjs-url=https://revealjs.com --standalone 
```

# Something else

```dot
digraph G{
    q_1 [label=<q<SUB>1</SUB>>]
    q_1 -> q_2 [label="E"]
    q_1 -> q_3 [label="\&epsilon;"]
    q_1 -> q_4 [label="$\epsilon$"]
    q_1 -> q_5 [label="&#949;"]
}
```