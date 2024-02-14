
This is quite simple when you visualise a number line: -6 -5 -4 -3 -2 -1 0 1 2 3 4 5 6Let's start at zero. Going right means the numbers _increase,_ whilst going left means the numbers _decrease_.So, integer division indeed returns the largest whole number _less than or equal to_ (<=) the floating-point result: 16//3 -> 5.33333...  -> 5 (because rounding 5.33333 _down_ gives us 5 (find the floating-point result on the number line and move _left_))So... now let's consider 16//-3.  
16//-3 -> -5.33333... -> ? (well, if we consult our number line again, our dear -5 "sits" between -6 and -5. Which of these two numbers is _less_ (i.e. to the _left_)? Well, -6. So, this means rounding -5.33333... _down_ results in -6)  ^Simones-explanation-Integer-Division

here, add this to your notes somewhere... it relates to reading the Python docs. It will probably come in handy down the road...
Python's asterisk and slash special parameters in the documentation:
|Left side|Divider|Right side|
|---|---|---|
|positional-only arguments |**`/`**|positional or keyword arguments |
|positional or keyword arguments |**`*`**|keyword-only arguments |
**Non-divider meaning/role**: `*args` means accepting an arbitrary numbers of *positional arguments* whereas `**kwargs` means accepting an arbitrary numbers of *keyword arguments*^Simones-python-docs


Put another way, the example is meant to show that the str.strip() method "works from the outside in" character by character; the string argument does not represent a substring, but rather a set of characters to remove whose order does not matter. So, imagine a simpler example such as "hello".strip("ol") : we are "searching" for two characters, "o" and "l", from the outside in. The algo says "hmmm, do I see an 'o' at either end? Yes! SNIP! (....breather...) hmmm, do I see an 'l' at either end? Yes! SNIP! (etc.....)" Note that "hello".strip("lo")  would result in the same final string because now, the algo says "hmmm, do I see an 'l' at either end? No! (...walks one char further...) hmmm, do I see an 'o' at either end? Yes! SNIP!" and then restarts the process from the beginning (that is, searching for 'l') until the answer to its question is always "No!" (so Mr Algo puts his little scissors away...)^'str'.strip() 

IMPORTANT: **expressions cannot contain statements** (e.g. the `for` and `if` flow control constructs within comprehensions are *NOT* statements; they are simply part of comprehension syntax)^list-comprehensions