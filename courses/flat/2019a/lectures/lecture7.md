---
title: FLAT
subtitle: 7. Non-Context Free Languages
date: March 4, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture7-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "revealjs-url=../../../presentation/reveal.js", "-V", "theme=beige", "--slide-level=2", "--standalone", "--katex=../../../presentation/katex/"]
---

# Introduction

## Introduction

* In this section we present a technique for proving that certain languages are not context free.
* Recall that in Section 1.4 we introduced the pumping lemma for showing that certain languages are not regular.
* Here we present a similar pumping lemma for context-free languages.

## Pumping Lemma

* The pumping lemma for CFLs states that every context-free language has a special value called the pumping length such that all longer strings in the language can be “pumped.”
* This time the meaning of pumped is a bit more complex.
* It means that the string can be divided into five parts so that the second and the fourth parts may be repeated together any number of times and the resulting string still remains in the language.

## Pumping Lemma for Context-Free Languages

### Theorem 2.34

* If A is a context-free language, then there is a number p (the pumping length) where, if s is any string in A of length at least p, then s may be divided into five pieces s = uvxyz satisfying the conditions:

1. $for\ each\ i\geq 0, uv^i xy^i z\in A$,
2. $|vy| > 0$, and
3. $|vxy| \leq p$.

## Pumping Lemma for Context-Free Languages

### Theorem 2.34

* When s is being divided into uvxyz, condition 2 says that either v or y is not the empty string.
* Otherwise the theorem would be trivially true.
* Condition 3 states that the pieces v, x, and y together have length at most p.
* This technical condition sometimes is useful in proving that certain languages are not context free.

# Proof Idea

## Proof Idea

### Setup

* Let A be a CFL and let G be a CFG that generates it.

### The Objective

* We must show that any sufficiently long string s in A can be pumped and remain in A.

### The Proof Type

* We will prove by contradiction
* Just like the pumping lemma for regular languages!

## Proof Idea

* Let s be a very long string in A.
* Because s is in A, it is derivable from G and so has a parse tree.
* The parse tree for s must be very tall because s is very long.
* That is, the parse tree must contain some long path from the start variable at the root of the tree to one of the terminal symbols at a leaf.
* On this long path, some variable symbol R must repeat because of the pigeonhole principle.

## Proof Idea

### Pigeonhole Principle

The pigeonhole principle is a fancy name for the rather obvious fact that:

* if p pigeons are placed into fewer than p holes,
* some hole has to have more than one pigeon in it.

## Proof Idea

. | Pumping Up | Pumping Down
-|-|-
 ![PL for CFGs Diagram 1](lecture7-diagram1.png) | ![PL for CFGs Diagram 2](lecture7-diagram2.png) | ![PL for CFGs Diagram 3](lecture7-diagram3.png)


The repetition allows us to replace the subtree under the second occurrence of R with the subtree under the first occurrence of R and still get a legal parse tree.


## Proof Idea

* Therefore, we may cut s into five pieces $uvxyz$ as the figure indicates
* We may repeat the second and fourth pieces and obtain a string still in the language.
* In other words, $uv^i xy^i z \in A$ for any i ≥ 0.

# Proof

## Proof Part A

* Let G be a CFG for CFL A.
* Let b be the maximum number of symbols in the right-hand side of a rule (assume at least 2).
* In any parse tree using this grammar, we know that a node can have no more than b children. In other words, at most b leaves are 1 step from the start variable; at most b^2^ leaves are within 2 steps of the start variable; and at most b^h^ leaves are within h steps of the start variable.

## Proof Part A

* So, if the height of the parse tree is at most h, the length of the string generated is at most $b^h$.
* Conversely, if a generated string is at least $b^h + 1$ long, each of its parse trees must be at least h + 1 high.

## Proof Part B

* Say |V| is the number of variables in G.
* We set p, the pumping length, to be $b^{|V|+1}$.
* Now if s is a string in A and its length is p or more, its parse tree must be at least |V|+1 high
* because $b^{|V|+1} \geq b^{|V|}+1$.

## Proof Part B

* To see how to pump any such string s, let $\tau$ (tau) be one of its parse trees.
* If s has several parse trees, choose τ to be a parse tree that has the smallest number of nodes.
* We know that τ must be at least |V| + 1 high, so its longest path from the root to a leaf has length at least |V | + 1.
* That path has at least |V| + 2 nodes; one at a terminal, the others at variables. Hence that path has at least |V | + 1 variables.  

## Proof Part B

* With G having only |V| variables, some variable R appears more than once on that path.
* For convenience later, we select R to be a variable that repeats among the lowest |V | + 1 variables on this path.

## Proof Part C

* We divide s into uvxyz according to Figure 2.35.
* Each occurrence of R has a subtree under it, generating a part of the string s.
* The upper occurrence of R has a larger subtree and generates vxy,
whereas the lower occurrence generates just x with a smaller subtree.
* Both of these subtrees are generated by the same variable, so we may substitute one for the other and still obtain a valid parse tree.

## Proof Part C

* Replacing the smaller by the larger repeatedly gives parse trees for the strings uv^i^xy^i^z at each i > 1.
* Replacing the larger by the smaller generates the string uxz. That establishes condition 1 of the lemma. We now turn to conditions 2 and 3.

## Proof Part D


* To get condition 2, we must be sure that v and y are not both ε.
* If they were, the parse tree obtained by substituting the smaller subtree for the larger would have fewer nodes than τ does and would still generate s.
* This result isn’t possible because we had already chosen τ to be a parse tree for s with the smallest number of nodes.
* That is the reason for selecting τ in this way.

## Proof Part E

* In order to get condition 3, we need to be sure that vxy has length at most p.
* In the parse tree for s the upper occurrence of R generates vxy.
* We chose R so that both occurrences fall within the bottom |V| + 1 variables on the path, and we chose the longest path in the parse tree, so the subtree where R generates vxy is at most |V| + 1 high.
* A tree of this height can generate a string of length at most $b^{|V|+1} = p$.

# Example

## Language

Use the pumping lemma to show that the language B = {anbncn| n ≥ 0} is not context free.

## Proof by Contradiction

We assume that B is a CFL and obtain a contradiction.

## Proof

* Let p be the pumping length for B that is guaranteed to exist by the pumping lemma.
* Select the string s = a^p^b^p^c^p^. Clearly s is a member of B and of length at least p.
* The pumping lemma states that s can be pumped, but we show that it cannot.
*  In other words, we show that no matter how we divide s into uvxyz, one of the three conditions of the lemma is violated.

## Proof

* First, condition 2 stipulates that either v or y is nonempty.
* Then we consider one of two cases, depending on whether substrings v and y contain more than one type of alphabet symbol.

## Proof - Case 1
* When both v and y contain only one type of alphabet symbol, v does not contain both a’s and b’s or both b’s and c’s, and the same holds for y.
* In this case, the string uv^2^xy^2^z cannot contain equal numbers of a’s, b’s, and c’s.
* Therefore, it cannot be a member of B.
* That violates condition 1 of the lemma and is thus a contradiction.

## Proof - Case 2

* When either v or y contains more than one type of symbol, uv^2^xy^2^z may contain equal numbers of the three alphabet symbols but not in the correct order.
* Hence it cannot be a member of B and a contradiction occurs.

## Proof

* One of these cases must occur.
* Because both cases result in a contradiction, a contradiction is unavoidable.
* So the assumption that B is a CFL must be false.
* Thus we have proved that B is not a CFL.

# Example 2

## Setup  

* Let $D = \{ww| w ∈ {0,1}^*\}$.
* Use the pumping lemma to show that D is not a CFL.
* Assume that D is a CFL and obtain a contradiction.
* Let p be the pumping length given by the pumping lemma.

## Choosing string

This time choosing string s is less obvious.

* One possibility is the string 0^p 10^p1.
* It is a member of D and has length greater than p, so it appears to be a good candidate.
* But this string can be pumped by dividing it as follows, so it is not adequate for our purposes.

![Diagram 4](lecture7-diagram4.png)

uvxyz
Let’s try another candidate for s. Intuitively, the string 0p1p0p1p seems to capture more of the “essence” of the language D than the previous candidate did. In fact, we can show that this string does work, as follows.
We show that the string s = 0p1p0p1p cannot be pumped. This time we use condition 3 of the pumping lemma to restrict the way that s can be divided. It says that we can pump s by dividing s = uvxyz, where |vxy| ≤ p.
First, we show that the substring vxy must straddle the midpoint of s. Other- wise, if the substring occurs only in the first half of s, pumping s up to uv2xy2z moves a 1 into the first position of the second half, and so it cannot be of the form ww. Similarly, if vxy occurs in the second half of s, pumping s up to uv2xy2z moves a 0 into the last position of the first half, and so it cannot be of the form ww.
But if the substring vxy straddles the midpoint of s, when we try to pump s down to uxz it has the form 0p1i0j1p, where i and j cannot both be p. This string is not of the form ww. Thus s cannot be pumped, and D is not a CFL.


# Extra Resources

## Video Resource

See [Neso Academy lecture](https://www.youtube.com/watch?v=jRhqx1_KcCk) for an additional resource on the Pumping Lemma for CFLs

<iframe width="560" height="315" src="https://www.youtube.com/embed/jRhqx1_KcCk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Application from Neso

1. Assume that A is context free
2. It has to have a pumping length (we will call it p)
3. All strings longer than P can be pumped |S| >= P
4. Find a string 'S' in A such that |S| >= P
5. Divide S into uvxyz

## Application from Neso

6. Show that uvixyiz is not in A for some i
7. Then consider the ways that S can be divided into uvxyz
8. Show that none of these can satisfy all 3 pumping conditions at the same time
9. S cannot be pumped == Contradiction
