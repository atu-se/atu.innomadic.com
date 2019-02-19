---
title: DSA Lecture
subtitle: 4. Sets and Maps
date: February 20, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture4-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "revealjs-url=../../../presentation/reveal.js", "-V", "theme=beige", "--slide-level=2", "--standalone"]
---

# Introduction (21.2)

## Objectives

* To store unordered, nonduplicate elements using a set (§21.2).
* To explore how and when to use HashSet, LinkedHashSet, or TreeSet to store a set of elements.
* To compare the performance of sets and lists (§21.3).
* To use sets to develop a program that counts the keywords in a Java source file (§21.4).

## Objectives

* To tell the differences between Collection and Map and describe when and how to use HashMap, LinkedHashMap, or TreeMap to store values associated with keys (§21.5).
* To use maps to develop a program that counts the occurrence of the words in a text (§21.6).
* To obtain singleton sets, lists, and maps, and unmodifiable sets, lists, and maps, using the static methods in the Collections class (§21.7).

## Introduction (21.1)

* A set is an efficient data structure for storing and processing nonduplicate elements.
* A map is like a dictionary that provides a quick lookup to retrieve a value using a key.

# Sets (21.2)

## Sets

* You can create a set using one of its three concrete classes:
  * HashSet
  * LinkedHashSet
  * TreeSet.

## Sets

* The Set interface extends the Collection interface.
* **It does not introduce new methods or constants**, but it stipulates that an instance of Set contains no duplicate elements.

## HashSet

* The HashSet class is a concrete class that implements Set.
* Any duplicated that are added are removed
* There is no particular order for the elements in a hash set. To impose an order on them, you need to use the LinkedHashSet class, which is introduced in the next section.


## HashSet Example

```java
Set<String> set = new HashSet<>();

set.add("London");
set.add("Paris");
set.add("New York");
set.add("San Francisco");
set.add("Beijing");
set.add("New York");

System.out.println(set);
```

`[San Francisco, New York, Paris, Beijing, London]`

## Iterating the Hashset

```java
System.out.println(set);

// Display the elements in the hash set
for (String s: set) {
  System.out.print(s + " ");
}

// Process the elements using a forEach method
System.out.println();
set.forEach(e -> System.out.print(e + " "));

```



## HashSet Load Factor


* HashSets can be initialized with a loadFactor and an initialCapacity
* The load factor measures how full the set is allowed to be before its capacity is increased.
* Generally, the default load factor 0.75 is a good tradeoff between time and space costs. We will discuss more on the load factor in Chapter 27, Hashing.

## LinkedHashSet

* LinkedHashSet extends HashSet with a linked-list implementation that supports an ordering of the elements in the set.
* The elements in a HashSet are not ordered, but the elements in a LinkedHashSet can be retrieved in the order in which they were inserted into the set.


## LinkedHashSet Example

```java
Set<String> set = new LinkedHashSet<>();

// Add strings to the set
set.add("London");
set.add("Paris");
set.add("New York");
set.add("San Francisco");
set.add("Beijing");
set.add("New York");

System.out.println(set);
```

`[London, Paris, New York, San Francisco, Beijing]`

## TreeSet

* Treeset is an implementation of Set which provides sorting (via the SortedSet interface) and navigatability (via the NavigableSet interface)

## SortedSet Interface
* SortedSet provides these methods:
  - first()
  - last()
  - headSet(toElement)
  - tailSet(fromElement)

## NavigatableSet Interface

* NavigatableSet provides these methods
  * lower(e) < e
  * floor(e) <= e
  * higher(e) >
  * ceiling(e) >=

## TreeSet Demo

## Set Efficiency

* Always be thoughtful about which implementation you choose based on your needs
* If you don’t need to *maintain* a sorted set when updating a set, you should use a **hash set**, because it takes less time to insert and remove elements in a hash set.
* When you need a sorted set, you can create a tree set from the hash set.

# Comparing Performance (21.3)

## Comparing Performance of Sets and Lists

* Sets are more efficient than lists for storing nonduplicate elements.
* Lists are useful for accessing elements through the index.

## Performance Experiment

* Experiment: add 50,000 elements to each of the following collection types:
  - HashSet
  - LinkedHashSet
  - TreeSet
  - ArrayList
  - LinkedList
* Test membership of a random element 50,000 times
* Test removing all elements from collection in order

## Performance Demo

## Performance Demo

Sample results:

```
Member test time for hash set is 51 milliseconds
Remove element time for hash set is 43 milliseconds
Member test time for linked hash set is 37 milliseconds
Remove element time for linked hash set is 50 milliseconds
Member test time for tree set is 100 milliseconds
Remove element time for tree set is 115 milliseconds
Member test time for array list is 9828 milliseconds
Remove element time for array list is 6116 milliseconds
Member test time for linked list is 13235 milliseconds
Remove element time for linked list is 8531 milliseconds
```

## Test Results

@import "lecture4-performance_membership.json" {as="vega-lite"}

## Test Results

@import "lecture4-performance_removal.json" {as="vega-lite"}

# Case Study: Counting Keywords (21.4)

## Counting Keywords
* Testing for membership is a good use case for a Set
* This case study creates a HashSet of a list of Java keywords
* The program scans a Java source code file and counts the number of keywords in it

## Counting Keywords Demo

# Maps (21.5)

## Maps

* A map is a container object that stores a collection of key/value pairs.
* It enables fast retrieval, deletion, and updating of the pair *through the key*.
* A map stores the values along with the keys.
* The keys are like indexes.
  * In List, the indexes are integers.
  * In Map, the keys can be any objects.


## Maps

* Like other sets, a map cannot contain duplicate keys. Each key maps to one value.
* A key and its corresponding value form an entry stored in a map

## Maps Interface and Classes

* All maps implement the Map interface
* You can create a map using one of its three concrete classes: HashMap, LinkedHashMap, or TreeMap.

## Map Interface

* +clear(): void
* +containsKey(key: Object): boolean
* +containsValue(value: Object): boolean
* +entrySet(): Set<Map.Entry<K,V>>
* +get(key: Object): V
* +isEmpty(): boolean

## Map Interface

* +keySet(): Set<K>
* +put(key: K, value: V): V
* +putAll(m: Map<? extends K,? extends V>): void
* +remove(key: Object): V * +size(): int
* +values(): Collection<V>

## HashMap

* The HashMap class is efficient for locating a value, inserting an entry, and deleting an entry.
* The entries in HashMap are *not* ordered

## LinkedHashMap

* LinkedHashMap extends HashMap with a linked-list implementation that supports an ordering of the entries in the map.
* The entries in a LinkedHashMap can be retrieved either:
  * in the order in which they were inserted into the map (known as the insertion order) * or in the order in which they were last accessed, from least recently to most recently accessed (access order)

## TreeMap

* The TreeMap class is efficient for traversing the keys in a sorted order.
* TreeMap implements SortedMap and NavigableMap, which provided the convenient methods for traversing the TreeMap

## Map Demo

## Map Demo Observations

* HashMap entries are in random order


# Case Study: Occurrence of Words (21.6)

# Singleton and Unmodifiable Collections and Maps (21.7)

## Singleton and Unmodifiable Collections and Maps

* You can create singleton sets, lists, and maps and unmodifiable sets, lists, and maps using the static methods in the Collections class.
* The Collections class contains the static methods for lists and collections.
* It also contains the methods for creating immutable singleton sets, lists, and maps, and for creating read-only sets, lists, and maps

# Summary

1. A set stores nonduplicate elements. To allow duplicate elements to be stored in a collection, you need to use a list.
2. A map stores key/value pairs. It provides a quick lookup for a value using a key.
3. Three types of sets are supported: HashSet, LinkedHashSet, and TreeSet.HashSet stores elements in an unpredictable order. LinkedHashSet stores elements in the order they were inserted. TreeSet stores elements sorted. All the methods in HashSet, LinkedHashSet, and TreeSet are inherited from the Collection interface.
4. The Map interface maps keys to the elements. The keys are like indexes. In List, the indexes are integers. In Map, the keys can be any objects. A map cannot contain duplicate keys. Each key can map to at most one value. The Map interface provides the methods for querying, updating, and obtaining a collection of values and a set of keys.
5. Three types of maps are supported: HashMap, LinkedHashMap, and TreeMap.
    - HashMap is efficient for locating a value, inserting an entry, and deleting an entry.
    - LinkedHashMap supports ordering of the entries in the map.
    - The entries in a HashMap are not ordered, but the entries in a LinkedHashMap can be retrieved either in the order in which they were inserted into the map (known as the insertion order) or in the order in which they were last accessed, from least recently accessed to most recently (access order).
    - TreeMap is efficient for traversing the keys in a sorted order. The keys can be sorted using the Comparable interface or the Comparator interface.
