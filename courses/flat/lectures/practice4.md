---
title: Formal Languages & Automata Theory
subtitle: Practice #4
date: February 13, 2019
export_on_save:
  pandoc: true

---

# Pumping Lemma

In our previous lecture we learned how to use the Pumping Lemma to prove that a language is not regular.  

In this exercise, I am going to provide an outline of the proof, which is complete through step 4.  

Work in a group to complete the proof by choosing a value for i and then demonstrate that all possible divisions of xy^i^z result in contradictions.

---


Let A = { ww | w $\isin$ {0,1} ^*^ }

1. Assume A is regular.
2. Let p be the pumping length from the pumping lemma
3. Choose a string s to be _\_0^p^10^p^1\___ ^*^
4. Because s is a member of A, the pumping lemma guarantees these three properties:
    1. s can be broken into three parts x,y, and z such that xy^i^z is in A
    2. |xy| <= p
    3. |y| > 0
5. Choose a value for i, _____.
6. Consider all of the valid possible divisions of s into x,y, and z.  If you choose well in step 3 and if the language is not regular, you will be able to demonstrate that there is no possible way to divide s into x, y, and z while still maintaining the properties the Pumping Lemma prescribes, then you can show that there is a logical contradiction.
7. If you have shown that each possible division of s into x, y, and z meeting all three conditions of the Pumping Lemma results in a contradiction, you can conclude that the language is not regular.






*. This is your choice and could make or break your proof.  You may have to choose another string to properly prove that a non-regular language is not regular.
