# More Stuff

## Function Composition

- **Composition** occurs when a function call is used as an argument to another function call, which may, in turn, be passed to another function call.
- The return value of the inner function call is used as the argument to the outer function.

```python
print(list(range(3, 17, 4)))
```

**Note**: Ask Simone about what she understands about this sentence: "Composition works best when each function except the outermost returns a usable value." What is an unusable value?

## Method Chaining

- Is similar to function composition but applies to methods rather than functions.

```python
tv_show = "Monty Python's Flying Circus"
tv_show = tv_show.upper().split()
# ['MONTY', "PYTHON'S", 'FLYING', 'CIRCUS']
```
- To use method chaining, you start by calling a method on an appropriate object. If that method returns another object, you can use it to call another method.
- You can chain as many method calls as necessary, though it can get messy if you chain more than 2 or 3 methods on a single line.
- Chaining only works when each method in the chain (except the last) returns an object with at least one helpful method.

