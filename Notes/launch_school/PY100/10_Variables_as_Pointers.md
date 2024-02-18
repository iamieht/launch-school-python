
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

## Equality and Identity

- Two objects, `obj1` and `obj2`, are said to be **equal** when `obj1 == obj2` returns `True`.
- The objects are the same object when `obj1 is obj2` returns `True`.
- We can also say that `obj1` and `obj2` have the same identity since `id(obj1)` and `id(obj2)` return the same value when `obj1 is obj2` returns `True`.

```python
numbers = [1, 2, 3]
numbers2 = numbers

print(numbers)                # [1, 2, 3]
print(numbers == numbers2)    # True
print(numbers is numbers2)    # True
```

```python
numbers = [1, 2, 3]
numbers2 = [1, 2, 3]

print(numbers)                # [1, 2, 3]
print(numbers == numbers2)    # True
print(numbers is numbers2)    # False
```

- In both cases, `numbers` and `numbers2` are equal since `numbers1 == numbers` returns `True`.
- In example 2, they are entirely different objects even though they have the same values.
- numbers2 = [1, 2, 3] creates a new object, which we assigned to `numbers2`. Thus, assuming that the new object is at address 4344281536, memory now looks like this:

![[Pasted image 20240218084557.png]]

## Shallow vs. Deep Copies

- Most copies created by Python are shallow copies.
- The `copy.copy` and `copy.deepcopy` functions from the built-in `copy` module are Python's primary ways to create shallow and deep copies, respectively.
- Built-in constructors create shallow copies as well:

```python
my_list = [[1, 2], 3, 4]
shallow = list(my_list)
print(shallow[0] is my_list[0])         # True

my_dict = {'abc': [1, 2, 3]}
shallow = dict(my_dict)
print(shallow['abc'] is my_dict['abc']) # True
```

### Shallow Copies

- A **shallow copy** of an object is a duplicate of the original object's outermost (topmost) level. Any nested objects within the copied object aren't duplicated; they still reference the nested objects from the original object. Thus, if you mutate the nested objects in the original, those mutations will be visible in the duplicate.
- Thus, our shallow copy only duplicated the outermost level of the original list object. The inner list remains shared between the original and duplicate lists.

```python
import copy

orig = [[1, 2], 3, 4]
dup = copy.copy(orig)

print(orig is dup)           # False
print(orig == dup)           # True
orig[2] = 44
print(dup)                   # [[1, 2], 3, 4]

print(orig[0] is dup[0])     # True
orig[0][1] = 22
print(dup[0])                # [1, 22]
```

- For completeness, here's what memory looks like now.

![[Pasted image 20240218090226.png]]

### Deep Copies

- A **deep copy** of an object is an exact duplicate of the original object at the outermost (or topmost) level and every nested object, no matter how deeply nested. There's basically nothing you can do to the original object that can be seen in the duplicate or vice versa.

```python
import copy

orig = [[1, 2], 3, 4]
dup = copy.deepcopy(orig)

print(orig is dup)           # False
print(orig == dup)           # True
orig[2] = 44
print(dup)                   # [[1, 2], 3, 4]

print(orig[0] is dup[0])     # False
orig[0][1] = 22
print(dup[0])                # [1, 2]
```

- Here's our final look at the memory picture. We now have two independent "Inner list" objects.

![[Pasted image 20240218092136.png]]

- frozensets do not implement the copy nor deepcopy function, so they always return a new object when using shallow or deep copies.
### Should I make deep or shallow copies?

- The answer to this question depends on your data structure, whether your data structure has mutable content.
- In practice, shallow copies are frequently okay. They work best when:
	- working with objects that are not collections, e.g., integers and booleans.
	- working with immutable objects with no mutable components, e.g., strings.
	- working with collections that have no mutable elements, e.g., tuples that don't contain mutable elements.
	- needed for performance reasons. Shallow copies are always faster.
	- you don't care if the mutable components of an object are shared.
- You should use deep copies when shallow copies are not okay. In particular, they work best when working with collections that have mutable elements, e.g., nested lists.