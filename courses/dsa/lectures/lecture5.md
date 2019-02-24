---
title: DSA Lecture
subtitle: 5. Developing Efficient Algorithms
date: February 24, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture5-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "revealjs-url=../../../presentation/reveal.js", "-V", "theme=beige", "--slide-level=2", "--standalone", "--katex"]
---

# Introduction (22.2)

## Objectives

* To estimate algorithm efficiency using the Big O notation (§22.2).
* To explain growth rates and why constants and nondominating terms
can be ignored in the estimation (§22.2).
* To determine the complexity of various types of algorithms (§22.3).
* To analyze the binary search algorithm (§22.4.1).
* To analyze the selection sort algorithm (§22.4.2).

## Objectives

* To analyze the Tower of Hanoi algorithm (§22.4.3).
* To describe common growth functions (constant, logarithmic, log- linear, quadratic, cubic, exponential) (§22.4.4).
* To design efficient algorithms for finding Fibonacci numbers using dynamic programming (§22.5).
* To find the GCD using Euclid’s algorithm (§22.6).
* To find prime numbers using the sieve of Eratosthenes (§22.7).


## Objectives

* To design efficient algorithms for finding the closest pair of points using the divide-and-conquer approach (§22.8).
* To solve the Eight Queens problem using the backtracking approach (§22.9).
* To design efficient algorithms for finding a convex hull for a set of points (§22.10).

## Introduction

* Algorithm design is to develop a mathematical process for solving a problem. Algorithm analysis is to predict the performance of an algorithm.
* This chapter will use a variety of examples to introduce common algorithmic techniques (dynamic programming, divide-and-conquer, and backtracking) for developing efficient algorithms
* Before introducing developing efficient algorithms, we need to address the question on how to measure algorithm efficiency.

# Measuring Efficiency (22.2)

## Big O Notation

* The Big O notation obtains a function for measuring algorithm time complexity based on the input size.
* You can ignore multiplicative constants and nondominating terms in the function.

## Comparing Search Algorithms

* Suppose two algorithms perform the same task, such as search (*linear search* vs. *binary search*).
* Which one is better?

## Measuring Runtime

* To answer this question, you might implement these algorithms and run the programs to get execution time. But there are two problems with this approach:
  - First, many tasks run concurrently on a computer. The execution time of a particular program depends on the *system load*.
  - Second, the execution time depends on *specific input*. Consider, for example, linear search and binary search. If an element to be searched happens to be the first in the list, linear search will find the element quicker than binary search.

## Growth Rates

* It is very difficult to compare algorithms by measuring their execution time.
* To overcome these problems, a theoretical approach was developed to analyze algorithms independent of computers and specific input.
* This approach approximates the effect of a change on the size of the input.
* In this way, you can see how fast an algorithm’s execution time increases as the input size increases, so you can compare two algorithms by examining their **growth rates**.

## Measuring Runtime

* For the same input size, an algorithm’s execution time may vary, depending on the input.
* An input that results in the shortest execution time is called the best-case input,
* An input that results in the longest execution time is the worst-case input.

## Measuring Runtime

* **Best-case analysis** and **worst-case analysis** are to analyze the algorithms for their best-case input and worst-case input.
* Best-case and worst-case analysis are not representative
* Worst-case analysis is very useful. You can be assured that the algorithm will never be slower than the worst case.

## Measuring Runtime

* An **average-case analysis** attempts to determine the average amount of time among all possible inputs of the same size.
* Average-case analysis is ideal, but difficult to perform, because for many problems it is hard to determine the relative probabilities and distributions of various input instances.
* Worst-case analysis is easier to perform, so the analysis is generally conducted for the worst case.


## Example: Linear Search

*  The linear search algorithm compares the key with the elements in the array sequentially until the key is found or the array is exhausted.
* If the key is not in the array, it requires n comparisons for an array of size n.
* If the key is in the array, it requires n/2 comparisons on average.
* The algorithm’s execution time is proportional to the size of the array.

## Example: Linear Search

*  If you double the size of the array, you will expect the number of comparisons to double.
* The algorithm grows at a linear rate. The growth rate has an order of magnitude of n.
* Computer scientists use the Big O notation to represent the “order of magnitude.”
* Using this notation, the complexity of the linear search algorithm is O(n), pronounced as “order of n.”

## Example: Linear Search

n\\f(n) | n   | n/2 | 100n   
-------|-----|-----|--------
100    | 100 | 50  | 10,000
200    | 200 | 100 | 20,000  

* f(n) = n, f(n) = n/2 and f(n) = 100n are all linear functions
* Doubling the size of n does yields the same growth rate for all three functions

## Example: Array Maximum

* Consider the algorithm for finding the maximum number in an array of n elements.
* To find the maximum number if n is 2, it takes one comparison;
* if n is 3, two comparisons.
* In general, it takes n - 1 comparisons to find the maximum number in a list of n elements.
* So what is the order of magnitude for this algorithm?  Hint: it's not O(n-1)

##  Example: Array Maximum

* Algorithm analysis is for large input size.
* If the input size is small, there is no significance in estimating an algorithm’s efficiency.
* As n grows larger, the n part in the expression n - 1 dominates the complexity.
* **The Big O notation allows you to ignore the nondominating part** (e.g., -1 in the expression n - 1) and **highlight the important part** (e.g., n in the expression n - 1).
* Therefore, the complexity of this algorithm is O(n).

## Constant Time

* If the time is not related to the input size, the algorithm is said to take constant time with the notation O(1).
* For example, a method that retrieves an element at a given index in an array takes *constant time*, because the time does not grow as the size of the array increases.

## Other Examples

* So far you have seen examples of:
  - O(n) "Linear"
  - O(1) "Constant time"
* There are other orders of magnitude

## Other Examples

$$1 + 2 + 3 + ... + (n-2) + (n-1) = \frac{n(n-1)}{2} = O(?)$$

## Other Examples

$$1 + 2 + 3 + ... + (n-2) + (n-1) = \frac{n(n-1)}{2} = O(n^2)$$

## Other Examples

$$1 + 2 + 3 + ... + (n-1) + (n) = \frac{n(n+1)}{2} = O(?)$$

## Other Examples

$$1 + 2 + 3 + ... + (n-1) + (n) = \frac{n(n+1)}{2} = O(n^2)$$

## Other Examples

$$a^0 + a^1 + a^2 + a^3 + ... + a^(n-1) + a^n  = \frac{a^(n+1) - 1}{a-1} = O(?)$$

## Other Examples

$$a^0 + a^1 + a^2 + a^3 + ... + a^(n-1) + a^n  = \frac{a^(n+1) - 1}{a-1} = O(a^n)$$


## Other Examples

$$2^0 + 2^1 + 2^2 + 2^3 + ... + 2^(n-1) + 2^n  = \frac{2^(n+1) - 1}{2-1} = O(?)$$

## Other Examples

$$2^0 + 2^1 + 2^2 + 2^3 + ... + 2^(n-1) + 2^n  = \frac{2^(n+1) - 1}{2-1} = O(2^n)$$

## Orders of Magnitude Covered

* O(1) "Constant time"
* O(n) "Linear"
* O(n^2)
* O(2^n)

## Two Complexity Measures

* *Time complexity* is a measure of execution time using the Big-O notation. Similarly, you can also measure space complexity using the Big-O notation.
* *Space complexity* measures the amount of memory space used by an algorithm.
  * The space complexity for most algorithms presented in the book is O(n). i.e., they exibit linear growth rate to the input size.
  * For example, the space complexity for linear search is O(n).

# Determining Big O

## Big O Example 1

Consider the time complexity for the following loop:

```java
for (int i = 1; i <= n; i++) {
  k = k + 5;
}
```

## Big O Example 1

* The statement `k = k + 5;` is a constant time, *c*.  
* When it is put inside of the for loop, `for (int i = 1; i <= n; i++)`, the time complexity becomes:


T(n) = ( a constant _c_ ) * n = O(n)

## Big O Example 2

Consider the time complexity for the following loop:

```java
for (int i = 1; i <= n; i++) {
  for (int j = 1; j <= n; j++) {
    k = k + i + j;
  }
}
```

## Big O Example 2

* The statement `k = k + i + j;` is a constant time, *c*.  
* The inner loop runs j times
* The outer loop runs i times
* So how many total times does the addition statement run?

## Big O Example 2


The time complexity for this loop is:

T(n) = (a constant *c*) * n * n = O(n^2^)

* O(n^2^) is called a quadratic algorithm.  When input size is doubled, the time quadruples
* Nested loops often create quadratic Big O's

## Big O Example 3

Consider the time complexity for the following loop:

```java
for (int i = 1; i <= n; i++) {
  for (int j = 1; j <= i; j++) {
    k = k + i + j;
  }
}
```

## Big O Example 3

* The outer loop runs n times
* The inner loop is executed 1 time, then 2 times, then 3 times... up to n times.
* What is the time complexity?

## Big O Example 3

$$ \begin{aligned}T(n) &= c + 2c + 3c + 4c + ... + nc \\ &= cn (n+1)/2 \\ &= (c / 2) n^2 + (c / 2) n \\ &= O(n^2)
 \end{aligned} $$

## Big O Example 4

Consider the time complexity for the following loop:

```java
for (int i = 1; i <= n; i++) {
  for (int j = 1; j <= 20; j++) {
    k = k + i + j; }
}
```

## Big O Example 4

* The inner loop executes 20 times, and the outer loop n times.  Therefore, the time complexity for the loop is:

$$ \begin{aligned}T(n) &= 20*c*n \\ &= O(n)
 \end{aligned} $$


## Big O Example 5

 Consider the time complexity for the following loop:

 ```java
 for (int j = 1; j <= 10; j++) {
   k = k + 4;
 }
 for (int i = 1; i <= n; i++) {
   for (int j = 1; j <= 20; j++) {
     k = k + i + j;
   }
}
```

## Big O Example 5

* The first loop executes 10 times
* The second loop executes 20*n times
* What is the Big O for this code?

 $$ \begin{aligned}T(n) &= 10*c + 20*c*n \\ &= O(?)
  \end{aligned} $$

## Big O Example 5

* The first loop executes 10 times
* The second loop executes 20*n times
* What is the Big O for this code?

  $$ \begin{aligned}T(n) &= 10*c + 20*c*n \\ &= O(n)
   \end{aligned} $$


## Big O Example 6

```java
if (list.contains(e)) {     
  System.out.println(e);
}
else
  for (Object t: list) {
    System.out.println(t);
  }
```

* Suppose the list contains n elements
* The execution time for list.contains(e) is O(n)
* The loop in the else clause takes O(n) time.
* What is the time complexity for the entire statement?

## Big O Example 6

```java
if (list.contains(e)) {     
  System.out.println(e);
}
else
  for (Object t: list) {
    System.out.println(t);
  }
```

$$ \begin{aligned}T(n) &= if\ test\ time + worstcase\ test\ time \\ &= O(n) + O(n) \\ &= O(?)
 \end{aligned} $$

## Big O Example 6

```java
if (list.contains(e)) {     
 System.out.println(e);
}
else
 for (Object t: list) {
   System.out.println(t);
 }
```

$$ \begin{aligned}T(n) &= if\ test\ time + worstcase\ test\ time \\ &= O(n) + O(n) \\ &= O(n)
\end{aligned} $$

## Big O Example 7

```java
result = 1;
for (int i = 1; i <= n; i++)
  result *= a;
```

What is the execution time?

## Big O Example 7

```java
result = 1;
for (int i = 1; i <= n; i++)
  result *= a;
```

$$ O(n) $$

## Big O Example 7

```java
result = 1;
for (int i = 1; i <= n; i++)
  result *= a;
```

What if we knew that $n=2^k$ for some k?

We could improve the algorithm like this:

```java
result = a;
for (int i = 1; i <= k; i++)
  result = result*result;
```
