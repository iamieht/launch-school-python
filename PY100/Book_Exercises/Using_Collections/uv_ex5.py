# Which of the following values can't be used as a key in a dict object, and why?

"cat"
(3, 1, 4, 1, 5, 9, 2)
["a", "b"]  # => Can't be use as list are mutable and not hashable
{"a": 1, "b": 2}  # => Can't be use as dict are mutable and not hashable
range(5)
{1, 4, 9, 16, 25}  # => Can't be use as sets are mutable and not hashable
3
0.0
frozenset({1, 4, 9, 16, 25})
