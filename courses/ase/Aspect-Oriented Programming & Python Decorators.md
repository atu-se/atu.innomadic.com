
In Python, decorators serve a role similar to Aspect Oriented Programming.

Image that our core requirements include building a calculator.  Sound familiar?



```python
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y
```

Let's test out our new functions.


```python
def test_calculator(x,y):
    print(add(x,y))
    print(subtract(x,y))
    print(multiply(x,y))
    print(divide(x,y))

test_calculator(4,4)
```

    8
    0
    16
    1.0


Looks good to me.  Our "core" requirements are fulfilled.  But what if we had a "cross-cutting concern" or a requirement that goes across all of our business functionality.  What if we needed to add a logging function before and after each operation.  

What if we wanted to log each time we entered one of our functions?  Maybe we could modify. it to look like this:


```python
def log(text):
    print(text)

def add(x,y):
    log("Entering add()")
    return x+y

def subtract(x,y):
    log("Entering subtract()")
    return x-y

def multiply(x,y):
    log("Entering multiply()")
    return x*y

def divide(x,y):
    log("Entering divide()")
    return x/y
```

Let's test the calculator again with our new logging.


```python
test_calculator(4,4)
```

    Entering add()
    8
    Entering subtract()
    0
    Entering multiply()
    16
    Entering divide()
    1.0


It worked!  It is a little bit repetitious, but it worked.

What if we want to log after the functions return?

That is a bit trickier. Any ideas?

We could store the result in a temporary variable and call the log functions before and after.  

Let's try that:




```python
def add(x,y):
    log("Entering add()")
    result = x+y
    log("Exiting add()")
    return result

def subtract(x,y):
    log("Entering subract()")
    result = x-y
    log("Exiting subtract()")
    return result

def multiply(x,y):
    log("Entering multiply()")
    result = x*y
    log("Exiting multiply()")
    return result

def divide(x,y):
    log("Entering divide()")
    result = x/y
    log("Exiting divide()")
    return result

```


```python
test_calculator(4,4)
```

    Entering add()
    Exiting add()
    8
    Entering subract()
    Exiting subtract()
    0
    Entering multiply()
    Exiting multiply()
    16
    Entering divide()
    Exiting divide()
    1.0


Okay.  Well, that is kind of what we wanted.  Really we would want to print "exited divide" after the output for the function, but that is hard to do.

Can you see that this logging feature is a kind of separate cross-cutting concern outside of the "core" concerns of our app (app, multiply, subtract, divide)?  

This is the type of scenario that **aspect-oriented programming** (AOP) was created to solve.  To use the language of AOP:

* **advice** is the code implementing a cross-cutting concern.  Our log function is an example of the cross-cutting concern.
* **aspects** tie the advice to a specific place in the code, known as the pointcut.  
* the start and end of our functions are **join points**.  They are places where an aspect may be woven.
* the **join point model** is the set of all the join points where the advice associated with an aspect may be included
* a **pointcut** is the exact place that we want to include an aspect.  The difference is a join point is a hypothetical or theoretical place where you could include an aspect.  A pointcut is the exact place you want to include the aspect.
* **weaving** is the process by which the aspects are included.  In Python, a process like this can be achieved through something called a *decorator*.

![AOP Diagram](aspect-oriented-programming/aop-term-diagram.png)

# Python Decorators

So let's look at Python decorators and see how they can be used



```python
class log(object):
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print("Entering", self.f.__name__+"()")
        result =  self.f(*args, **kwargs)
        print ("Exiting", self.f.__name__+"()")
        return result

@log
def myFunction():
    print ("Inside myFunction!")

print ("Finished decorating myFunction")

myFunction()
```

    Finished decorating myFunction
    Entering myFunction()
    Inside myFunction!
    Exiting myFunction()


so if we create another function, we can just decorate it in the same way, with @log


```python
@log
def myOtherFunction():
    print("Inside my other function")

myOtherFunction()
```

    Entering myOtherFunction()
    Inside my other function
    Exiting myOtherFunction()


So, what if we implemented our original calculator functions (with the logging added) using decorators?


```python
@log
def add(x,y):
    return x+y

@log
def subtract(x,y):
    return x-y

@log
def multiply(x,y):
    return x*y

@log
def divide(x,y):
    return x/y

test_calculator(4,4)
```

    Entering add()
    Exiting add()
    8
    Entering subtract()
    Exiting subtract()
    0
    Entering multiply()
    Exiting multiply()
    16
    Entering divide()
    Exiting divide()
    1.0


# References
* [Python 3 Patterns, Recipes and Idioms](http://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html)
* [Flask Decorators](http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/#login-required-decorator)    
* [Python Course](https://www.python-course.eu/python3_decorators.php)
