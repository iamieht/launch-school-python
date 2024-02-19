# Data Types (Q&A)

1. Name all primitive data types, including category and class?

2. Name all non-primitive data types, including category and class?

3. Which data types are mutable and which ones not?

4. What kind of data types are functions and NoneType?

5. What is the definition of literals?

6. Which Python objects have no literal form, so we need to use the type constructor to create them?

7. Are these valid integer values?

```python
int1 = 123.456.678
int2 = 123,456,678
int3 = 123_456_678
int4 = 123456678
```
8. Are these valid floats values?

```python
float1 = 1.0
float2 = 42,348.35
float3 = 42.348,35
float4 = 42_348.35
float5 = 42348.35
```

8. What is the result of this expression?

```python
3 + True
```

9. What is the difference between a text sequence and an ordinary sequence?

**A**: *Ordinary sequences contain zero or more objects, but a text sequence does not contain any objects: it simply contains the characters (or bytes) that make up the text sequence. Those characters or bytes are not objects; they are simply part of the value.*

10. String literals with an `r` prefix are called?

**A**: *raw string literals*

11. String literals with an `f` prefix are called?

**A**: *formatted string literals* or **f-strings**.

12. What is **string interpolation**?

**A**: is an operation to merge Python expressions with strings and they are enabled by **f-strings**

13. What's the difference between an ordered and unordered sequence?

14. Name the three types of Sequences

**A**: ranges, tuples and lists

15. Name the similarities and differences between Tuples and Lists

**A**: 
* *The order of the elements is significant.*
* *Lists are mutable; tuples are immutable.*
* *Use indexing syntax to retrieve specific elements.*
* *Use indexing syntax to reassign specific list elements.*
* *Index numbers are non-negative integers starting from 0 and ending at the sequence's length minus 1.*

16. How to define a Tuple with a single element?

**A**: `my_tuple = (1,)`

17. Explain the concept of **indexed reassignment** or **element reassignment**

**A**: *It is a way to mutate a list using the indexing syntax to the left of the `=` in an assignment.*
```python
>>> my_list[3] = 'New value'
>>> my_list
[1, 'xyz', True, 'New value']
```

18. What is a lazy sequence?

19. What is the result of this code and explain why?

```python
my_dict = {
...     'dog': 'barks',
...     'cat': 'meows',
...     ['pig']: 'oinks',
... }
```

20. Name the ordered sequences in Python?

21. Name the unordered sequences in Python?

22. How are called the objects in a list/tuple?

23. How are sometimes called the objects in a set?

24. What is the result of this code and why?

```python
set1 = {2, 3, 4, [5, 6, 7]}
```

25. How do you create an empty set?

26. What are the differences between a set and a frozenset?
