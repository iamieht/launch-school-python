
# Variables as Pointers

## Variables as Pointers

- **references** and **pointers** are both the same.
- You can say that a variable points to or references an object in memory, and you can also say that the pointers stored in variables are references.
- All variables are pointers to objects. If you assign the same object to multiple variables, every one of those variables references (points to) the same object. They act like aliases for the object.
- When a reassignment involves the creation of a new object, Python first creates the new object. It then changes the variable's stack item to point to the new object.
- If a variable points to a mutable object and you do something to mutate that object, Python doesn't change the variable; it changes the object. Every variable that references that object will immediately see the object's new state.

## Variables and Objects

- Each variable has a unique address in memory, usually in an area called the **stack**, and sometimes in a different area called the **heap**.
- Objects are usually stored in the **heap** as this can be pretty much any size.
- Once the **heap** space is allocated, Python created and stores the objects at that location. The address is then copied to the variable's stack location.
- Thus, when you access a variable, Python first determines where the variable is on the stack. It then takes the object's heap address from the stack item and uses it to find the object. The variable is a pointer to a stack location, and the stack location is a pointer to the object.

Example:

- we're creating a variable named `numbers` and giving it an initial value of a list with 3 numbers:
```python
numbers = [1, 2, 3]
```

- Since `numbers` is a new variable, Python adds a new entry to the stack. For simplicity, we'll assume the variable's stack address is at memory location 10240.
- Next, Python allocates enough memory on the heap to hold the list and its elements (actually, the list object may contain pointers to the elements, but we'll ignore that for now). Let's say that Python allocates 32 bytes at address 4344278784 for the list and its elements. It then constructs an appropriate list object with its elements at address 4344278784.
- Finally, Python copies the address 4344278784 into the variable's stack address. Things now look something like this:

![[Pasted image 20240217192658.png]] 
- Suppose we now want to print the object assigned to `numbers`:
```python
print(numbers)
```
- To do this, Python looks up the name `numbers` in its list of variables and sees it is on the stack at address 10240. On the stack, Python can see that the object associated with `numbers` is at address 4344278784. Finally, it passes that address to `print`, which formats and prints the object.

## Variables and Shared Objects

```python
numbers2 = numbers
```

- Since `numbers2` is new, Python must create a new variable on the stack, which it does. We'll assume it's at address 10256. It then determines the memory address of the object assigned to `numbers` and stores that address in `numbers2`'s stack item. That means both `numbers` and `numbers2` now point to the same object. You can verify this by using the `id` function or the `is` operator:

```python
print(id(numbers) == id(numbers2))      # True
print(numbers is numbers2)              # True
```

- our variables and objects are now organized like this in memory:

![[Pasted image 20240218083317.png]]

- The variables are in different places on the stack. However, they both reference the same object.
- Pointers have a curious effect when you assign a variable that references an existing object to another variable. Instead of copying the object referenced by the variable on the right to the variable on the left, Python only copies the pointer. Thus, when we initialize `numbers2` with `numbers`, we make both `numbers` and `numbers2` point to the same list object: `[1, 2. 3]`. It's not just the same value but the same list at the same address. The two variables are independent, but since they point to the same list, that list depends on what you do with both `numbers` and `numbers2`.

## 