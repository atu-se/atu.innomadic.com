# Arden's Theoreom

Let P and Q be two regular expressions over alphabet

> R = Q ∪ RP

has a unique solution that is:
> R = QP<sup> * </sup>

How is this true?  Substitute the value of R into the right-hand side of the original equation:

> R = Q ∪ (Q ∪ RP)P = Q ∪ QP ∪ RP<sup>2</sup>

then

> R = Q ∪ (Q ∪ (Q ∪ RP)P)P = Q ∪ QP ∪ RP<sup>2</sup> ∪ RP<sup>3</sup>

Do you see the pattern?

> R = Q ∪ QP ∪ RP<sup>2</sup> ∪ RP<sup>3</sup> ∪ RP<sup>4</sup> ...

This pattern is equal to:

> R = QP<sup> * </sup>.

So this is Arden's Theorem:

> R = Q ∪ RP

is equivalent to

> R = QP<sup> * </sup>.


# Using Arden's Theorem to find Regular Expressions of a Deterministic Finite Automata

* Assuming the DFA is well-formed
  - There are no empty-string transitions
  - There is one start states
* States q<sub>0</sub> to q<sub>n</sub>
* q<sub>i</sub> is a final states
* w<sub>ij</sub> denotes the regular expression reprsenting the set of labels of edges from q<sub>i</sub> to q<sub>j</sub>.  We can create set of equations, with each equation being the union of the transitions to the state for which we are forming the equation.  For the starting state, the empty string (ϵ) will also be added.  The equations are designed as follows, with q<sub>1</sub> being treated as a start state:

q <sub>1 </sub> = q<sub>1</sub>w<sub>11</sub> ∪ q<sub>2</sub>w<sub>21</sub> ∪ ... ∪ q<sub>n</sub>w<sub>n1</sub> ∪ ϵ

q <sub>2 </sub> = q<sub>1</sub>w<sub>12</sub> ∪ q<sub>2</sub>w<sub>22</sub> ∪ ... ∪ q<sub>n</sub>w<sub>n2</sub>

q <sub>3 </sub> = q<sub>1</sub>w<sub>13</sub> ∪ q<sub>2</sub>w<sub>23</sub> ∪ ... ∪ q<sub>n</sub>w<sub>n3</sub>

## Example

Given the following DFA:
![Arden's Theorem Example](figure4-11.png)

We can use our algorithm to generate the following regular expressions:

q <sub>1 </sub> = q<sub>2</sub>b ∪ q<sub>3</sub>a ∪ ϵ

q <sub>2 </sub> = q<sub>1</sub>a

q <sub>3 </sub> = q<sub>1</sub>b

q <sub>4 </sub> = q<sub>2</sub>a ∪ q<sub>3</sub>b ∪ q<sub>4</sub>a ∪ q<sub>4</sub>b

Because q<sub>1</sub> is the final state, we need to solve for q<sub>1</sub> only.  As in a system of equations, we substitute the equations for q<sub>2</sub> and q<sub>3</sub> into q<sub>1</sub>, yielding:

q <sub>1 </sub> = q<sub>1</sub>ab ∪ q<sub>1</sub>ba ∪ ϵ

q <sub>1 </sub> = ϵ ∪ q<sub>1</sub>(ab ∪ ba)

Note:  Do you see the pattern from Arden's Theorem?  Here is Arden's Theorem again:

> R = Q ∪ RP

is equal to

> R = QP<sup> * </sup>

Therefore,

q <sub>1 </sub> = ϵ ∪ q<sub>1</sub>(ab ∪ ba)

is equal to:

q <sub>1 </sub> = ϵ(ab ∪ ba)<sup> * </sup>

q <sub>1 </sub> = (ab ∪ ba)<sup> * </sup>

## Classroom Exercises

Construct a regular expression corresponding to the the following state diagrams.

1.
![Regex to DFA Exercise 1](figure4-12.png)



2.
![Regex to DFA Exercise 2](figure4-13.png)
# Sources
* *An Introduction to Automata Theory and Formal Language, pp. 102-103*
