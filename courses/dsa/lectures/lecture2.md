---
title: DSA Lecture
subtitle: 2. Generics
date: February 6, 2019
export_on_save:
  pandoc: true
output:
  custom_document:
    path: lecture2-slides.html
    pandoc_args: ["-t", "revealjs", "-V",  "revealjs-url=../../../presentation/reveal.js", "-V", "theme=beige", "--slide-level=2", "--standalone"]
---

# Review

# Practice Exercises

## A Tale of Two Factorials

* Factorial
* Tail Recursive Factorial
* What makes the second one tail-recursive?

# Generics

## Objectives

1. To describe the benefits of generics (§19.2).
2. To use generic classes and interfaces (§19.2).
3. To define generic classes and interfaces (§19.3).
4. To explain why generic types can improve reliability and readability (§19.3).
5. To define and use generic methods and bounded generic types (§19.4).

## Objectives

6. To develop a generic sort method to sort an array of Comparable
objects (§19.5).
7. To use raw types for backward compatibility (§19.6).
8. To explain why wildcard generic types are necessary (§19.7).
9. To describe generic type erasure and list certain restrictions and limitations on generic types caused by type erasure (§19.8).
10. To design and implement generic matrix classes (§19.9).

## Introduction (19.1)

* Generics enable you to detect errors at compile time rather than at runtime.
* The motivation for using Java generics is to detect errors at compile time.

# Motivations and Benefits (19.2)

## Comparable

### Previously

~~~java
package java.lang;
public interface Comparable {       
  public int compareTo(Object o)
}
~~~

### Comparable

~~~java
package java.lang;
public interface Comparable<T> {    
  public int compareTo(T o)
}
~~~

## Comparable

### Previously

~~~java
Comparable c = new Date();
System.out.println(c.compareTo("red"));
~~~

### Now with Generics

~~~java
Comparable<Date> c = new Date();
System.out.println(c.compareTo("red"));
~~~

## ArrayList

* Since JDK 1.5, ArrayList is a generic class.

```java
ArrayList<String> list = new ArrayList<>();
```

* What happens if you try to add an integer to this ArrayList?

# Generic Classes and Interfaces (19.3)

## Generic Classes and Interfaces

* A generic type can be defined for a class or interface.
* A concrete type must be specified when using the class to create an object or using the class or interface to declare a reference variable.

## Casting

### Previously

~~~java
String s = (String)(list.get(0));
// Casting needed prior to JDK 1.5
~~~

### Now with Generics

~~~java
String s = list.get(0);
// No casting is needed
~~~

## Example: Generic Stack

~~~java
public class GenericStack<E> {
private java.util.ArrayList<E> list = new java.util.ArrayList<>();

  public int getSize() {
    return list.size();
  }

  public E peek() {
    return list.get(getSize() - 1);
  }

  public void push(E o) {
    list.add(o);
  }
~~~

## Example: Generic Stack

```java
  public E pop() {
    E o = list.get(getSize() - 1);
    list.remove(getSize() - 1);
    return o;
  }

  public boolean isEmpty() {
    return list.isEmpty();
  }

  @Override
  public String toString() {
    return "stack: " + list.toString();
  }
}
```

## Example: Generic Stack

```java
GenericStack<String> stack1 = new GenericStack<>();
stack1.push("London");
stack1.push("Paris");
stack1.push("Berlin");
```

## Example: Generic Stack

```java
GenericStack<Integer> stack2 = new GenericStack<>();
// can use = new GenericStack<>();
// or      = new GenericStack<Integer>();
stack2.push(1);
// autoboxing 1 to new Integer(1)
stack2.push(2);
stack2.push(3);
```

## Benefits

* Instead of using a generic type, you could simply make the type element Object, which can accommodate any object type.
* However, using generic types can improve software reliability and readability, because certain errors can be detected at compile time rather than at runtime.
* For example, because stack1 is declared GenericStack<String>, only strings can be added to the stack.
* It would be a compile error if you attempted to add an integer to stack1

# Generic Methods (19.4)

## Generic Methods

* A generic type can be defined for a static method.

## Example: Generic Methods

```java
public class GenericMethodDemo {
  public static void main(String[] args ) {
    Integer[] integers = {1, 2, 3, 4, 5};
    String[] strings = {"London", "Paris", "New York", "Austin"};
    GenericMethodDemo.<Integer>print(integers);
    GenericMethodDemo.<String>print(strings);
  }
```

## Example: Generic Methods

```java
  public static <E> void print(E[] list) {
    for (int i = 0; i < list.length; i++)
      System.out.print(list[i] + " ");
    System.out.println();
  }
}
```

## Example: Method Declaration

```java
public static <E> void print(E[] list) {
  for (int i = 0; i < list.length; i++)
    System.out.print(list[i] + " ");
  System.out.println();
}
```

## Example: Method Invocation

```java
    GenericMethodDemo.<Integer>print(integers);
    GenericMethodDemo.<String>print(strings);
    //or, alternatively
    print(integers);
    print(strings);
    //the compiler figures out the types in the above method
```

## Bounded vs. Unbounded

* A generic type can be specified as a subtype of another type.
* An unbounded generic type `<E>` is the same as `<E extends Object>`.

## Example: Bounded Type

```java
import chapter13.Circle;
import chapter13.GeometricObject;
import chapter13.Rectangle;

public class BoundedTypeDemo {
  public static void main(String[] args ) {
    Rectangle rectangle = new Rectangle(2, 2);
    Circle circle = new Circle(2);

    System.out.println("Same area? " +
      equalArea(rectangle, circle));
  }
```

## Example: Bounded Type

```java
  public static <E extends GeometricObject> boolean equalArea(
      E object1, E object2) {
    return object1.getArea() == object2.getArea();
  }
}
```

## Syntax Note

* To define a generic type for a class, place it after the class name, such as `GenericStack<E>`.
* To define a generic type for a method, place the generic type before the method return type, such as `<E> void max(E o1, E o2)`.

# Demo: Generic Sort

# Practice Exercises

## Practice #3

Choose and do one of the following two programming exercises:

1. Programming Exercise 19.2 on page 758.
2. Programming Exercise 19.7 on page 758.

# Raw Types (19.6)

## Raw Types and Backwards Compatibility

* A generic class or interface used without specifying a concrete type, called a *raw type*, enables backward compatibility with earlier versions of Java,

## Raw Types and Backwards Compatibility

```java
GenericStack stack = new GenericStack(); // raw type
```

* this is equivalent to...

```java
GenericStack<Object> stack = new GenericStack<Object>();
````

## Unsafe Raw Type

```java
public class Max {
  /** Return the maximum between two objects */
  public static Comparable max(Comparable o1, Comparable o2) {
    if (o1.compareTo(o2) > 0)
      return o1;
    else
      return o2;
  }
}
```

## Safer Generic

```java
public class MaxUsingGenericType {
  /** Return the maximum between two objects */
  public static <E extends Comparable<E>> E max(E o1, E o2) {
    if (o1.compareTo(o2) > 0)
      return o1;
    else
      return o2;
  }
}
```

# Wildcard Generic Types (19.7)

* You can use unbounded wildcards, bounded wildcards, or lower-bound wildcards to specify a range for a generic type.

## Example

```java
public class WildCardNeedDemo {
  public static void main(String[] args ) {
     GenericStack<Integer> intStack = new GenericStack<>();
     intStack.push(1); // 1 is autoboxed into new Integer(1)
     intStack.push(2);
     intStack.push(-2);
     System.out.print("The max number is " + max(intStack));
     //This will produce an error
  }
```

## Example

```java
/** Find the maximum in a stack of numbers */
public static double max(GenericStack<Number> stack) {
   double max = stack.pop().doubleValue(); // initialize max
   while (!stack.isEmpty()) {
     double value = stack.pop().doubleValue();
     if (value > max)
       max = value;
   }
   return max;
}
}
```

## Motivation for Wildcards

* The program above has a compile error in line 8 because intStack is not an instance of GenericStack<Number>.
* Thus, you cannot invoke max(intStack).
* The fact is that Integer is a subtype of Number, but GenericStack<Integer> is not a subtype of GenericStack<Number>.
* To circumvent this problem, use wildcard generic types.

## Wildcard Forms

A wildcard generic type has three forms.

* The first form, `?`, called a *non bounded wildcard*, is the same as `? extends Object`.
* The second form, `? extends T`, called a *bounded wildcard*, represents `T` or a subtype of `T`.
* The third form, `? super T`, called a *lower-bound wildcard*, denotes `T` or a supertype of `T`.

## Previous Example

```java
/** Find the maximum in a stack of numbers */
public static double max(GenericStack<Number> stack) {
   double max = stack.pop().doubleValue(); // initialize max
   while (!stack.isEmpty()) {
     double value = stack.pop().doubleValue();
     if (value > max)
       max = value;
   }
   return max;
}
}
```

## Adjustment

### Old

```java
public static double max(GenericStack<Number> stack)
```

### New

```java
public static double max(GenericStack<? extends Number> stack)
```

## Corrected: Bounded Wildcard

```java
/** Find the maximum in a stack of numbers */
public static double max(GenericStack<? extends Number> stack) {
   double max = stack.pop().doubleValue(); // initialize max
   while (!stack.isEmpty()) {
     double value = stack.pop().doubleValue();
     if (value > max)
       max = value;
   }
   return max;
}
}
```

## Example: Unbounded Wildcard

* The following example shows an example of using the `?` wildcard in the print method that prints objects in a stack and empties the stack.
* `<?>` is a wildcard that represents any object type. It is equivalent to `<? extends Object>`

## Example: Unbounded Wildcard

```java
public class AnyWildCardDemo {
  public static void main(String[] args ) {
     GenericStack<Integer> intStack = new GenericStack<>();
     intStack.push(1); // 1 is autoboxed into new Integer(1)
     intStack.push(2);
     intStack.push(-2);
     print(intStack);
  }
```

## Example: Unbounded Wildcard

```java
  /** Print objects and empties the stack */
  public static void print(GenericStack<?> stack) {
    while (!stack.isEmpty()) {
      System.out.print(stack.pop() + " ");
    }
  }
}
```

## Example: Unbounded Wildcard

* What happens if you replace `GenericStack<?>` with `GenericStack<Object>`?
* If you do that, it would be wrong to invoke `print(intStack)`, because `intStack` is not an instance of `GenericStack<Object>`.
* Note that `GenericStack<Integer>` is not a subtype of `GenericStack<Object>`, even though `Integer` is a subtype of `Object`.

## Super

* When is the wildcard `<? super T>` needed?
* Consider this example...

## Example: Lower Bound Wildcard

```java
public class SuperWildCardDemo {
  public static void main(String[] args) {
    GenericStack<String> stack1 = new GenericStack<String>();
    GenericStack<Object> stack2 = new GenericStack<Object>();
    stack2.push("Java");
    stack2.push(2);
    stack1.push("Sun");
    add(stack1, stack2);
    AnyWildCardDemo.print(stack2);
  }
```

## Example: Lower Bound Wildcard

```java
  public static <T> void add(GenericStack<T> stack1,
      GenericStack<? super T> stack2) {
    while (!stack1.isEmpty())
      stack2.push(stack1.pop());
  }
}
```

## Example: Lower Bound Wildcard

* `GenericStack<? super T>` is used to declare `stack2` in line 13.
* If `<? super T>` is replaced by `<T>`, a compile error will occur on `add(stack1, stack2)` in line 8,
* `stack1`’s type is `GenericStack<String>` and `stack2`’s type is `GenericStack<Object>`.
* `<? super T>` represents type `T` or a supertype of `T`. `Object` is a supertype of `String`.

## Super vs. Extends?

* The Bounded (*extends*) and Lower Bound (*super*) types are similar
* Use the following acronym to help you remember when to use *extends* vs. *super*: PECS
  - **P**roducer **E**xtends
  - **C**onsumer **S**uper

## Super vs. Extends?

* PECS: "Producer Extends, Consumer Super".
* "Producer Extends" - If you need a `List` to produce T values (you want to read `T`s from the list), you need to declare it with `? extends T`
* e.g. `List<? extends Integer>`
* But you cannot add to this list

## Super vs. Extends?

* PECS: "Producer Extends, Consumer Super".
* "Consumer Super" - If you need a `List` to consume `T` values (you want to write `T`s into the list), you need to declare it with `? super T`,
* e.g. `List<? super Integer>`.
* But there are no guarantees what type of object you may read from this list.

## Super vs. Extends?

* If you need to both read from and write to a list, you need to declare it exactly with no wildcards, e.g. List<Integer>.
* [See this excellent explanation on Stackoverflow](https://stackoverflow.com/questions/4343202/difference-between-super-t-and-extends-t-in-java).

# Erasure and Restrictions on Generics (19.8)

## Erasure

* The information on generics is used by the compiler but is not available at runtime.
* This is called type erasure.
* This approach enables the generic code to be backward compatible with the legacy code that uses raw types.
* Once the compiler confirms that a generic type is used safely, it converts the generic type to a raw type.

## Erasure

```java
ArrayList<String> list = new ArrayList<>();
list.add("Oklahoma");
String state = list.get(0);
```

is changed by the compiler into this:

```java
ArrayList list = new ArrayList();
list.add("Oklahoma");
String state = (String)(list.get(0));
```

## Erasure

```java
public static <E> void print(E[] list) {
  for (int i = 0; i < list.length; i++)
    System.out.print(list[i] + " ");
  System.out.println();
}
```

is changed by the compiler into this:

```java
public static void print(Object[] list) {
  for (int i = 0; i < list.length; i++)
    System.out.print(list[i] + " ");
  System.out.println();
}
```

## Erasure

```java
public static <E extends GeometricObject> boolean
equalArea( E object1, E object2) {
  return object1.getArea() == object2.getArea();
}
```

is changed by the compiler into this:

```java
public static boolean equalArea(
GeometricObject object1, GeometricObject object2) {
  return object1.getArea() == object2.getArea();
}
```

## Restrictions on Generics

1. Restriction: Cannot Use new E()
2. Restriction: Cannot Use new E[]
3. Restriction: A Generic Type Parameter of a Class Is Not Allowed in a Static Context
4. Restriction: Exception Classes Cannot Be Generic

## Restrictions on Generics

### Restriction 1: Cannot Use new E()
You cannot create an instance using a generic type parameter. For example, the following
statement is wrong:

`E object = new E();`

The reason is that new E() is executed at runtime, but the generic type E is not available at runtime.


## Restrictions on Generics

### Restriction 2: Cannot Use new E[]

You cannot create an array using a generic type parameter. For example, this statement is wrong:

`E[] elements = new E[capacity];`

You can work around this in this manner, but it will result in an unavoidable compiler warning:

`E[] elements = (E[])new Object[capacity];`

## Restrictions on Generics

### Restriction 3: A Generic Type Parameter of a Class Is Not Allowed in a Static Context

Since all instances of a generic class have the same runtime class, the static variables and methods of a generic class are shared by all its instances. Therefore, it is illegal to refer to a generic type parameter for a class in a static method, field, or initializer.

## Restrictions on Generics

### Restriction 3: A Generic Type Parameter of a Class Is Not Allowed in a Static Context

For example, the following code is illegal:

```java
public class Test<E> {
  public static void m(E o1) { // Illegal }
    public static E o1; // Illegal
    static {
          E o2; // Illegal
    }
}
```

## Restrictions on Generics

### Restriction 4: Exception Classes Cannot Be Generic

A generic class may not extend `java.lang.Throwable`, so the following class declaration would be illegal:

`public class MyException<T> extends Exception { }`

## Restrictions on Generics

### Restriction 4: Exception Classes Cannot Be Generic

The JVM has to check the exception thrown from the try clause ()`catch (MyException<T> ex)`) to see if it matches the type specified in a catch clause. This is impossible, because the type information is not present at runtime.

# Summary

## Summary

1. Generics give you the capability to parameterize types. You can define a class or a method with generic types, which the compiler replaces with concrete types.
2. The key benefit of generics is to enable errors to be detected at compile time rather than at runtime.

## Summary

3. A generic class or method permits you to specify allowable types of objects that the class or method can work with. If you attempt to use a class or method with an incompatible object, the compiler will detect the error.
4. A generic type defined in a class, interface, or a static method is called a formal generic type, which can be replaced later with an actual concrete type. Replacing a generic type is called a generic instantiation.

## Summary

5. A generic class such as ArrayList used without a type parameter is called a raw type. Use of raw types is allowed for backward compatibility with the earlier versions of Java.

## Summary

6. A wildcard generic type has three forms: `?` and `? extends T`, and `? super T`, where `T` is a generic type.
    1. The first form, `?`, called an unbounded wildcard, is the same as `? extends Object`.
    2. The second form, `? extends T`, called a bounded wildcard, represents `T` or a subtype of `T`.
    3. The third form, `? super T`, called a lower-bound wildcard, denotes `T` or a supertype of `T`.

## Summary

7. Generics are implemented using an approach called type erasure. The compiler uses the generic type information to compile the code but erases it afterward, so the generic information is not available at runtime. This approach enables the generic code to be backward compatible with the legacy code that uses raw types.
8. You cannot create an instance using a generic type parameter.

## Summary

9. You cannot create an array using a generic type parameter.
10. You cannot use a generic type parameter of a class in a static context.
11. Generic type parameters cannot be used in exception classes.
