# Number Guessing

## Strategy
Guess the average of the lowest possible and the highest possible.

8 or fewer guesses -- always.
100

1. 50
2. 25
3. 12
4. 6
5. 3
6. 2
7. 1



```python
lowest = 1
highest = 100
result = 0
guess_count = 0
while not result=='3':
    print('Think of a number between 1 and 100.')
    guess = int((highest + lowest) / 2)
    guess_count += 1
    print(f"I guess your number is {guess}.")
    result = input(f"Is your number 1. higher than 2. lower than or 3. exactly {guess}?")
    if result == '1':
        lowest = guess + 1
    elif result == '2':
        highest = guess - 1
    elif result == '3':
        print(f"I win! Game over. I guessed it in {guess_count} guesses")
    else:
        print("hey! that's not valid choice. Try again.")
    

```

    Think of a number between 1 and 100.
    I guess your number is 50.
    Is your number 1. higher than 2. lower than or 3. exactly 50?3
    I win! Game over. I guessed it in 1 guesses


# Object-Oriented Programming

* classes
* objects 
* encapsulation
* inheritance
* member
* methods


```python
# University - people

class Person ():
    def __init__(self, name):
        self.name = name
    def set_birthdate(self, birthdate):
        self.birthdate = birthdate
        
nick = Person("Nicholas P")
nick.set_birthdate("January 1, 1999")
print(f"{nick.name}'s birthdate is {nick.birthdate}")
```

    Nicholas P's birthdate is January 1, 1999



```python
class Student(Person):
    def __init__(self, name, id):
        self.id = id
        super().__init__(name)

amiina = Student("Amiina Abdilaahi Abdilaahi", 1)
amiina.set_birthdate("February 7, 2002")
print(f"{amiina.name}'s birthdate is {amiina.birthdate}")
```

    Amiina Abdilaahi Abdilaahi's birthdate is February 7, 2002



```python
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        
muhammed = Teacher("Muhammed Daud")
print(f"This teacher is {muhammed.name}")
```

    This teacher is Muhammed Daud



```python
class Class ():
    def __init__(self, name):
        self.students = []
        self.name = name
    
    def add_student(self, new_student):
        self.students.append(new_student)
        
dsa = Class("Data Structures and Algorithms")
print(f"This class is {dsa.name}")

new_student = Student("Abdisamed", 2)
dsa.add_student(new_student)
dsa.add_student(amiina)

for student in dsa.students:
    print(student.name)
```

    This class is Data Structures and Algorithms
    Abdisamed
    Amiina Abdilaahi Abdilaahi

