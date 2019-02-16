---
title: DSA Lecture
subtitle: 3. Lists, Stacks, Queues, and Priority Queues
date: February 15, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture3-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "revealjs-url=../../../presentation/reveal.js", "-V", "theme=beige", "--slide-level=2", "--standalone"]
---

# Introduction (20.1)

## Introduction

* Choosing the best data structures and algorithms for a particular task is one of the keys to developing high-performance software.
* A data structure is a collection of data organized in some fashion. The structure not only stores data but also supports operations for accessing and manipulating the data.
* In object-oriented thinking, a data structure, also known as a container or container object, is an object that stores other objects, referred to as data or elements.

# Collections (20.2)

## 20.2 Collections
The Collection interface defines the common operations for lists, vectors, stacks, queues, priority queues, and sets.

## Collections

The Java Collections Framework supports two types of containers:

* One for storing a collection of elements is simply called a collection.
* The other, for storing key/value pairs, is called a map.

## Maps

* Maps are efficient data structures for quickly searching an element using a key.
* We will introduce maps in the next chapter.

## Collections

* `Set`s store a group of non-duplicate elements.
* `List`s store an ordered collection of elements.
* `Stack`s store objects that are processed in a last-in, first-out fashion.
* `Queue`s store objects that are processed in a first-in, first-out fashion.
* `PriorityQueue`s store objects that are processed in the order of their priorities.

## Packaging

* All the interfaces and classes defined in the Java Collections Framework are grouped in the java.util package


## Design

* The design of the Java Collections Framework is an excellent example of using interfaces, abstract classes, and concrete classes.
  - The interfaces define the framework.
  - The abstract classes provide partial implementation.
  - The concrete classes implement the interfaces with concrete data structures.

## Collection\<E>

* +add(o: E): boolean
* +isEmpty(): boolean
* +contains(o: Object): boolean
* +size(): int


## Collection\<E>

* +containsAll(c: Collection<?>): boolean
* +remove(o: Object): boolean
* +addAll(c: Collection<? extends E>): boolean
* +equals(o: Object): boolean
* +clear(): void


## Collection\<E>

* +hashCode(): int
* +removeAll(c: Collection<?>): boolean
* +retainAll(c: Collection<?>): boolean
* +toArray(): Object[]

## Collection Interface

* The examples I have just shown used ArrayList
* But the methods are for the Collections interface
* All of the methods will also work for `HashSet`, `LinkedList`, `Vector`, and `Stack`.

## Additional Interfaces

* All the concrete classes in the Java Collections Framework implement the `java.lang.Cloneable` and `java.io.Serializable` interfaces
*  ... Except that java.util.PriorityQueue does not implement the `Cloneable` interface. Thus, all instances of `Cloneable` except priority queues can be cloned and all instances of `Cloneable` can be serialized.

# Iterators (20.3)

## Iterators

* Each collection is `Iterable`.
* You can obtain its `Iterator` object to traverse all the elements in the collection.

## `Iterator` Demo

# Lists (20.4)

## Lists

The `List` interface extends the `Collection` interface and defines a collection for storing elements in a sequential order. To create a list, use one of its two concrete classes: `ArrayList` or `LinkedList`.

## List\<E>

* +add(index: int, element: Object): boolean
* +addAll(index: int, c: Collection<? extends E>): boolean
* +get(index: int): E
* +indexOf(element: Object): int
* +lastIndexOf(element: Object): int

## List\<E>

* +listIterator(): ListIterator<E>
* +listIterator(startIndex: int): ListIterator<E>
* +remove(index: int): E
* +set(index: int, element: Object): Object
* +subList(fromIndex: int, toIndex: int): List<E>

## ArrayList vs. LinkedList

* The `ArrayList` class and the `LinkedList` class are two concrete implementations of the List interface.
* `ArrayList` stores elements in an array.
* `LinkedList` stores elements in a linked list.

## ArrayList vs. LinkedList

* If you need to support random access through an index without inserting or removing elements at the beginning of the list, ArrayList offers the most efficient collection.
* If, however, your application requires the insertion or deletion of elements at the beginning of the list, you should choose LinkedList.

## ArrayList

* `ArrayList` is a resizable-array implementation of the List interface.
* Each `ArrayList` instance has a capacity, which is the size of the array used to store the elements in the list.
* If the capacity of the array is exceeded, a larger new array is created and all the elements from the current array are copied to the new array.


## ArrayList

* It is always at least as large as the list size. As elements are added to an ArrayList, its capacity grows automatically.
* An ArrayList does not automatically shrink. You can use the trimToSize() method to reduce the array capacity to the size of the list.
* An ArrayList can be constructed using its no-arg constructor, ArrayList(Collection), or ArrayList(initialCapacity).

## ArrayList\<E>

* `ArrayList` provides methods for manipulating the size of the array used internally to store the list, as shown in Figure 20.5.
  - +ArrayList()
  - +ArrayList(c: Collection<? extends E>)
  - +ArrayList(initialCapacity: int)
  - +trimToSize(): void

## LinkedList

* A list can grow or shrink dynamically. Once it is created, an array is fixed. If your application does not require the insertion or deletion of elements, an array is the most efficient data structure.
* In addition to implementing the List interface, this class provides the methods for retrieving, inserting, and removing elements from both ends of the list.

## LinkedList\<E>

* +LinkedList()
* +LinkedList(c: Collection<? extends E>)
* +addFirst(element: E): void
* +addLast(element: E): void
* +getFirst(): E
* +getLast(): E
* +removeFirst(): E
* +removeLast(): E

## LinkedList and ArrayList Demo

# `Comparator` Interface (20.5)

## Comparator

* `Comparator` can be used to compare the objects of a class that doesn’t implement `Comparable`.
* The `Comparable` interface defines the compareTo method, which is used to compare two elements of the same class that implement the `Comparable` interface.
* What if the elements’ classes do not implement the `Comparable` interface? Can these elements be compared? * You can define a comparator to compare the elements of different classes. To do so, define a class that implements the `java.util.Comparator<T>` interface and overrides its `compare` method.

## Comparator Demo

```java
public class GeometricObjectComparator
    implements Comparator<GeometricObject>, java.io.Serializable {
  public int compare(GeometricObject o1, GeometricObject o2) {
    double area1 = o1.getArea();
    double area2 = o2.getArea();

    if (area1 < area2)
      return -1;
    else if (area1 == area2)
      return 0;
    else
      return 1;
  }
}
```

## Comparator Demo


# Static Methods (20.6)

The Collections class contains static methods to perform common operations in a collection and a list.

## List Static Methods

* +sort(list: List): void
* +sort(list: List, c: Comparator): void
* +binarySearch(list: List, key: Object): int
* +binarySearch(list: List, key: Object, c: * Comparator): int
* +reverse(list: List): void
* +reverseOrder(): Comparator

## List Static Methods

* +shuffle(list: List): void
* +shuffle(list: List, rmd: Random): void
* +copy(des: List, src: List): void
* +nCopies(n: int, o: Object): List
* +fill(list: List, o: Object): void

## Collection Static Methods

* +max(c: Collection): Object
* +max(c: Collection, c: Comparator): Object
* +min(c: Collection): Object
* +min(c: Collection, c: Comparator): Object
* +disjoint(c1: Collection, c2: Collection):
  boolean
* +frequency(c: Collection, o: Object): int

# Case Study:  Bouncing Balls (20.7)

# `Vector` and `Stack` Classes (20.8)

## Vectors and Stacks

* `Vector` is a subclass of `AbstractList`,
* `Stack` is a subclass of `Vector` in the
Java API.
* The Vector class preceded the creation of the Java Collections Framework
* These classes were redesigned to fit into the Java Collections Framework, but all their old-style methods are retained for compatibility.

## Vector

* Vector is the same as ArrayList, except that it contains synchronized methods for accessing and modifying the vector.
* Synchronized methods can prevent data corruption when a vector is accessed and modified by two or more threads concurrently
* For the many applications that do not require synchronization, using `ArrayList` is more efficient than using `Vector`.

## Stack

* In the Java Collections Framework, Stack is implemented as an extension of Vector, as illustrated in Figure 20.11.
* Vector is extended to provide a last-in, first out (LIFO) data structure

## Stack\<E>
* +Stack()
* +empty(): boolean
* +peek(): E
* +pop(): E
* +push(o: E): E
* +search(o: Object): int

# `Queues` and `PriorityQueue`s (20.9)

## Queues and PriorityQueues

* The `Queue` interface extends java.util.Collection with additional insertion, extraction,
and inspection operations
* A queue is a first-in, first-out (FIFO) data structure. Elements are appended to the end of the queue and are removed from the beginning of the queue.
* In a priority queue, elements are assigned priorities. When accessing elements, the element with the highest priority is removed first.

## Queue\<E>

* +offer(element: E): boolean
* +poll(): E
* +remove(): E
* +peek(): E
* +element(): E

## Deque and LinkedList

* The LinkedList class implements the `Deque` interface
* `Deque` extends `Queue`
* `Deque` supports element insertion and removal at both ends. The name "deque" is short for “double-ended queue” and is usually pronounced “deck".

## Priority Queue Demo

# Case Study: Evaluating Expressions (20.10)

## Evaluating Expressions

* Stacks can be used to evaluate expressions.

## Evaluating Expressions Demo


# Summary

## Summary

1. The Java Collections Framework supports sets, lists, queues, and maps. They are defined in the interfaces `Set`, `List`, `Queue`, and `Map`.
2. A list stores an ordered collection of elements.
3.  All the concrete classes except `PriorityQueue` in the Java Collections Framework implement the `Cloneable` and `Serializable` interfaces. Thus, their instances can be cloned and serialized.

## Summary

4. To allow duplicate elements to be stored in a collection, you need to use a list. A list not only can store duplicate elements but also allows the user to specify where they are stored. The user can access elements by an index.
5. Two types of lists are supported: `ArrayList` and `LinkedList`. `ArrayList` is a resizable-array implementation of the `List` interface. All the methods in `ArrayList` are defined in `List`.

## Summary

6. `LinkedList` is a linked-list implementation of the `List` interface. In addition to implementing the `List` interface, this class provides the methods for retrieving, inserting, and removing elements from both ends of the list.
7. Comparator can be used to compare the objects of a class that doesn’t implement Comparable.

## Summary

8. The `Vector` class extends the Abstract `List` class. Starting with Java 2, Vector has been the same as `ArrayList`, except that the methods for accessing and modifying the vector are synchronized. The Stack class extends the Vector class and provides several methods for manipulating the stack.
9. The `Queue` interface represents a queue. The `PriorityQueue` class implements `Queue` for a priority queue.
