---
title: Formal Languages & Automata Theory
subtitle: Practice #4
date: February 13, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: "./practice4-html.html"
---

# Pumping Lemma Practice

In our previous lecture we learned how to use the Pumping Lemma to prove that a language is not regular.  

In this exercise, I am going to provide an outline of the proof, and I will assist you by choosing the string (step 4) and the value for i (step 5).  This means that all you have to do is identify why it is a contradiction.

Work in a group to complete the proof by demonstrating that all possible divisions of xy^i^z result in contradictions.

---


Let A = { ww | w $\in$ {0,1}^\*^ }

1. Assume A is regular.
2. Let p be the pumping length from the pumping lemma
3. Choose a string s: _\___0^p^10^p^1\___
4. Because s is a member of A, the pumping lemma guarantees these three properties:
    1. s can be broken into three parts x,y, and z such that xy^i^z is in A
    2. |xy| <= p
    3. |y| > 0
5. Choose a value for i: __\_2\___.
6. Consider all of the valid possible divisions of s into x,y, and z.  If you choose well in step 3 and if the language is not regular, you will be able to demonstrate that there is no possible way to divide s into x, y, and z while still maintaining the properties the Pumping Lemma prescribes, then you can show that there is a logical contradiction.
7. If you have shown that each possible division of s into x, y, and z meeting all three conditions of the Pumping Lemma results in a contradiction, you can conclude that the language is not regular.






NOTE:  The choices in step 4 and step 5 are choices you would normally make as part if your effort to prove that a language is non-regular.  There is no algorithm to tell you what to choose.  This is your choice and could make or break your proof.  You may have to choose another string to properly prove that a non-regular language is not regular. In today's exercise, I have supplied you with these values.
