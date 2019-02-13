---
title: DSA Lecture
subtitle: 1. Recursion
date: February 2, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture1-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "theme=beige", "-V", "revealjs-url=../../../presentation/reveal.js", "--slide-level=2", "--standalone"]
---

# Course Information

## Essentials

* Data Structures and Algorithms (DSA)
* Course Website - [atu-se.github.io/courses/dsa](http://atu-se.github.io/courses/dsa)
* Primary Textbook - [Introduction to Java Programming, 10th Edition (Liang)]()

## Meeting Times

* Sunday @ 10:30 a.m.
* Tuesday @ 8:30 a.m.
* Wednesday @ 10:30 a.m.

## How to Succeed

* Attend all lectures
* Take notes (not all materials will be distributed as slides)
* Ready and study your textbook
* Do all assignments
* Ask questions

## Academic Integrity

* Read the academic integrity policy in the syllabus
* You are encouraged to discuss the topics among yourselves.
* Unless otherwise noted, your work should be your own and you should not share your work with others
* Copying or cheating on homework, exams, etc. may result in failing grades

# Lecture 1: Recursion

## Key Terms

* Recursion is a technique that leads to elegant solutions to problems that are difficult to program using simple loops.
* A recursive method is one that invokes itself.

## Recursion Example: Factorial

## Example: Factorial

$$ 0! = 1 $$
$$ n! = n \cdot(n-1)! \qquad \text{when} \geq 1 $$

## Example: Factorial

2! = 2 $\times$ 1! = 2 $\times$ 1 = 2

3! = 3 $\times$ 2! = 3 $\times$  2 $\times$ 1! = 3 $\times$ 2 $\times$ 1 = 6



## Example: Factorial

~~~
import java.util.Scanner;

public class ComputeFactorial {
    /** Main method */
    public static void main(String[] args) {
        // Create a Scanner
        Scanner input = new Scanner(System.in);
        System.out.print("Enter a non-negative integer:");
        int n = input.nextInt();
        // Display factorial
        System.out.println("Factorial of " + n + " is "
        + factorial(n));
    }
~~~

...

## Example: Factorial
...

~~~java
  /** Return the factorial for a specified number */
  public static long factorial(int n) {
      if (n == 0) // Base case
          return 1;
      else
          return n * factorial(n - 1); // Recursive call
  }
}
~~~

## What-If

What if our factorial function was like this?

~~~java
public static long factorial(int n) {
  return n * factorial(n - 1);
}
~~~

# Example: Fibonacci

## Example: Fibonacci

~~~java
import java.util.Scanner;
public class ComputeFibonacci {
  /** Main method */
  public static void main(String args[]) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);
    System.out.print("Enter an index for the Fibonacci number: ");
    int index = input.nextInt();
    // Find and display the Fibonacci number
    System.out.println(
      "Fibonacci number at index " + index + " is " + fib(index));
  }
~~~

## Example: Fibonacci 2

~~~java
/** The method for finding the Fibonacci number */
public static long fib(long index) {
  System.out.println("Called fib");
  if (index == 0) // Base case
    return 0;
  else if (index == 1) // Base case
    return 1;
  else  // Reduction and recursive calls
    return fib(index - 1) + fib(index - 2);
  }
}
~~~

# Example: Recursive Palindrome

## Example: Recursive Palindrome

~~~java
public class RecursivePalindrome {
  public static boolean isPalindrome(String s) {
    return isPalindrome(s, 0, s.length() - 1);
  }

  public static boolean isPalindrome(String s, int low, int high) {
    if (high <= low) // Base case
      return true;
    else if (s.charAt(low) != s.charAt(high)) // Base case
      return false;
    else
      return isPalindrome(s, low + 1, high - 1);
  }
~~~

## Example: Recursive Palindrome 2

~~~java
  public static void main(String[] args) {
    System.out.println("Is moon a palindrome? "
      + isPalindrome("moon"));
    System.out.println("Is noon a palindrome? "
      + isPalindrome("noon"));
    System.out.println("Is a a palindrome? " + isPalindrome("a"));
    System.out.println("Is aba a palindrome? " +
      isPalindrome("aba"));
    System.out.println("Is ab a palindrome? " + isPalindrome("ab"));
  }
}
~~~

# Example: Recursive Selection Sort

## Example: Selection Sort

* Find the smallest element in the list and swap it with the first element.
* Ignore the first element and sort the remaining smaller list recursively.

## Example: Selection Sort

~~~java
public class RecursiveSelectionSort {
  public static void sort(double[] list) {
    sort(list, 0, list.length - 1); // Sort the entire list
  }
~~~

## Example: Selection Sort

~~~java
public static void sort(double[] list, int low, int high) {
  if (low < high) {
    // Find the smallest number and its index in list(low .. high)
    int indexOfMin = low;
    double min = list[low];
    for (int i = low + 1; i <= high; i++) {
      if (list[i] < min) {
        min = list[i];
        indexOfMin = i;
      }
    }
~~~

## Example: Selection Sort

~~~java
    // Swap the smallest in list(low .. high) with list(low)
    list[indexOfMin] = list[low];
    list[low] = min;

    // Sort the remaining list(low+1 .. high)
    sort(list, low + 1, high);
  }
}
~~~

## Example: Selection Sort

~~~java
  public static void main(String[] args) {
    double[] list = {2, 1, 3, 1, 2, 5, 2, -1, 0};
    sort(list);
    for (int i = 0; i < list.length; i++)
      System.out.print(list[i] + " ");
  }
}
~~~

# Practice Exercises

## Practice Exercise 18.4

Write a recursive mathematical definition for computing 2^n^ for a positive integer n.

## Practice Exercise 18.4

$$ power\_of\_two(0) = 1 $$
$$ power\_of\_two(n) = 2*power\_of\_two(n-1) \qquad \text{when} > 0 $$


## Practice Exercise 18.7a

~~~java
public class Test {
  public static void main(String[] args) {
    xMethod(5);
  }
  public static void xMethod(int n) {
    if (n > 0) {
      System.out.print(n + " ");
      xMethod(n - 1); }
    }
}
~~~

## Practice Exercise 18.7b

~~~java
public class Test {
  public static void main(String[] args) {
    xMethod(5);
  }
  public static void xMethod(int n) {
    if (n > 0) {
      xMethod(n - 1);
      System.out.print(n + " "); }
    }
}
~~~

## Practice Exercise 18.8a

~~~java
public class Test {
  public static void main(String[] args) {
      xMethod(1234567);
  }
  public static void xMethod(double n) {
    if (n != 0) {
      System.out.println(n);
      xMethod(n / 10); }
    }
}
~~~

## Practice Exercise 18.8b

~~~java
public class Test {
  public static void main(String[] args) {
      Test test = new Test();
      System.out.println(test.toString());
    }
    public Test() {
      Test test = new Test();
    }
}
~~~

# Lecture 1b

## Problem Solving Using Recursion

All recursive methods have the following characteristics:

* The method is implemented using an if-else or a switch statement that leads to different cases.
* One or more base cases (the simplest case) are used to stop recursion.
* Every recursive call reduces the original problem, bringing it increasingly closer to a
base case until it becomes that case.

## Problem Solving Using Recursion

In general, to solve a problem using recursion, you break it into subproblems. Each subproblem is the same as the original problem but smaller in size. You can apply the same approach to each subproblem to solve it recursively.

## Recursive Coffee Drinking

~~~java
public static void drinkCoffee(Cup cup) {
  if (!cup.isEmpty()) {
      cup.takeOneSip(); // Take one sip
      drinkCoffee(cup);
    }
}
~~~

## Printing N Times

~~~java
public static void nPrintln(String message, int times)
{
  if (times >= 1) {
      System.out.println(message);
      nPrintln(message, times - 1);
  } // The base case is times == 0
}
~~~

# Recursive Binary Search (BS)

## BS Algorithm

Given an array that is sorted in increasing order, imagine searching for a single element (the key).

Begin by comparing the key to the middle element of the array.  There are three possibilities.

## BS Algorithm

* Case 1: If the key is less than the middle element, recursively search for the key in the first half of the array.
* Case 2: If the key is equal to the middle element, the search ends with a match.
* Case 3: If the key is greater than the middle element, recursively search for the key
in the second half of the array.

## BS Implementation

~~~java
public class RecursiveBinarySearch {
  public static int recursiveBinarySearch(int[] list, int key) {
    int low = 0;
    int high = list.length - 1;
    return recursiveBinarySearch(list, key, low, high);
  }
~~~

## BS Implementation

~~~java
  public static int recursiveBinarySearch(int[] list, int key,
      int low, int high) {
    if (low > high)  // The list has been exhausted without a match
      return -low - 1;

    int mid = (low + high) / 2;
    if (key < list[mid])
      return recursiveBinarySearch(list, key, low, mid - 1);
    else if (key == list[mid])
      return mid;
    else
      return recursiveBinarySearch(list, key, mid + 1, high);
  }
}
~~~

## Directory Size

~~~java
import java.io.File;
import java.util.Scanner;
public class DirectorySize {
  public static void main(String[] args) {
    // Prompt the user to enter a directory or a file
    System.out.print("Enter a directory or a file: ");    
    Scanner input = new Scanner(System.in);
    String directory = input.nextLine();

    // Display the size
    System.out.println(getSize(new File(directory)) + " bytes");
  }
~~~

## Directory Size

~~~java
  public static long getSize(File file) {
    long size = 0; // Store the total size of all files
    if (file.isDirectory()) {
      File[] files = file.listFiles(); // All files and subdirectories
      for (int i = 0; i < files.length; i++) {
        size += getSize(files[i]); // Recursive call
      }
    }
    else { // Base case
      size += file.length();
    }
    return size;
  }
}
~~~

# Tower of Hanoi

## Tower of Hanoi

The Tower of Hanoi problem is a classic problem that can be solved easily using recursion, but it is difficult to solve otherwise.

## Tower of Hanoi

![Tower of Hanoi](./lecture1/tower_of_hanoi.png) {r, fig.width=8*k, fig.height=6*k}

## Tower of Hanoi

There are n disks labeled 1, 2, 3, . . . , n and three towers labeled A, B, and C.

* No disk can be on top of a smaller disk at any time.
* All the disks are initially placed on tower A.
* Only one disk can be moved at a time, and it must be the smallest disk on a tower.

[Demonstration](https://www.mathsisfun.com/games/towerofhanoi.html)

## Tower of Hanoi

~~~java
import java.util.Scanner;
public class TowersOfHanoi {
  /** Main method */
  public static void main(String[] args) {
    // Create a Scanner
    Scanner input = new Scanner(System.in);
    System.out.print("Enter number of disks: ");
    int n = input.nextInt();
    // Find the solution recursively
    System.out.println("The moves are:");
    moveDisks(n, 'A', 'B', 'C');
  }
~~~

## Tower of Hanoi

~~~java
/** The method for finding the solution to move n disks
    from fromTower to toTower with auxTower */
  public static void moveDisks(int n, char fromTower,
      char toTower, char auxTower) {
    if (n == 1) // Stopping condition
      System.out.println("Move disk " + n + " from " +
        fromTower + " to " + toTower);
    else {
      moveDisks(n - 1, fromTower, auxTower, toTower);
      System.out.println("Move disk " + n + " from " +
        fromTower + " to " + toTower);
      moveDisks(n - 1, auxTower, toTower, fromTower);
    }
  }
}
~~~




# Recursion vs. Iteration

## Recursion vs. Iteration

* Recursion is an alternative form of program control. It is essentially repetition without a loop.
* Any problem that can be solved recursively can be solved nonrecursively with iterations.
* Recursion has some negative aspects: it uses up too much time and too much memory.

## Why Recursion?

* In some cases, using recursion enables you to specify a clear, simple solution for an inherently recursive problem that would otherwise be difficult to obtain.
* The rule of thumb is to use which- ever approach can best develop an intuitive solution that naturally mirrors the problem.
* If an iterative solution is obvious, use it. It will generally be more efficient than the recursive option.

# Tail Recursion

## Tail Recursion

* A tail recursive method is efficient for reducing stack size.
* A recursive method is said to be tail recursive if there are no pending operations to be performed on return from a recursive call

## Tail Recursion

### Non-tail recursion
```
...
...
recursive_method_call()
...
```

### Tail Recursion

```
...
...
...
recursive_method_call()
```

## Nontail-recursive Factorial
```java
/** Return the factorial for a specified number */
public static long factorial(int n) {
  if (n == 0) // Base case
    return 1;
  else
    return n * factorial(n - 1); // Recursive call
}
```

## Tail Recursive Factorial
```java
/** Auxiliary tail-recursive method for factorial */
private static long factorial(int n, int result) {
  if (n == 0)
    return result;
  else
    return factorial(n - 1, n * result); // Recursive call
}
```

# Chapter Key Points

## Chapter Key Points

1. A recursive method is one that directly or indirectly invokes itself. For a recursive method to terminate, there must be one or more base cases.
2. Recursion is an alternative form of program control. It is essentially repetition without a loop control. It can be used to write simple, clear solutions for inherently recursive problems that would otherwise be difficult to solve.

## Chapter Key Points

3. Sometimes the original method needs to be modified to receive additional parameters in order to be invoked recursively. A recursive helper method can be defined for this purpose.
4. Recursion bears substantial overhead. Each time the program calls a method, the system must allocate memory for all of the method’s local variables and parameters. This can consume considerable memory and requires extra time to manage the memory.

## Chapter Key Points

5. A recursive method is said to be tail recursive if there are no pending operations to be performed on return from a recursive call. Some compilers can optimize tail recursion to reduce stack size.
