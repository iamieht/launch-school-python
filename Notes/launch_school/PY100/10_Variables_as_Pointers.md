
# Variables as Pointers

## Variables as Pointers

- **references** and **pointers** are both the same.
- You can say that a variable points to or references an object in memory, and you can also say that the pointers stored in variables are references.
- All variables are pointers to objects. If you assign the same object to multiple variables, every one of those variables references (points to) the same object. They act like aliases for the object.
- When a reassignment involves the creation of a new object, Python first creates the new object. It then changes the variable's stack item to point to the new object.
- If a variable points to a mutable object and you do something to mutate that object, Python doesn't change the variable; it changes the object. Every variable that references that object will immediately see the object's new state.

## Variables and Objects
