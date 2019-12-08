---
title: FLAT
subtitle: 10. Review
date: November 23, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture8-slides.html
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



# Machine Overview

<div class="container">
<div class="column">
### Finite Automaton Schematic

![](images/lecture8-diagram1.png){}
</div>
<div class="column">
### Pushdown Automaton Schematic

![](images/lecture8-diagram2.png){}

</div>

<div class="column">

### Turing Machine Schematic

![](images/lecture10-diagram1-tmschematic.png){}

</div>

</div>



# Correlations 

|                         | Regular Languages           | Context-Free Languages | Turing-Recognizable |
|-------------------------|-----------------------------|------------------------|---------------------|
| **Language Recognizer** | Finite Automaton (NFA, DFA) | Pushdown Automaton     | Turing Machine      |
| **Language Generator**  | Regular Expression          | Context-Free Grammar   |                     |



# References, Resources

* [ADUni.org Lectures](https://www.youtube.com/playlist?list=PL601FC994BDD963E4)
* [UC San Diego Lecture Slides](https://cseweb.ucsd.edu/classes/fa08/cse105/)