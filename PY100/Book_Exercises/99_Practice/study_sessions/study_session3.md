# Question 1: What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

# Question 2: There is a bug in this function, fix it:
def all_actions():
    counter = 0

    def increment_counter():
        global counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()

# Question 3: What will be printed? Why?
print(150_000_000)
print(15_000_0000)



# What will the following output, and why?
# print(0 in "bob")
# print(0 in ("bob"))
# 0 in ("bob",)     # False
print(({1} in set({5, 6}))) # works
print(([1] in set({5, 6}))) # error

# Question 1: What will be printed? Why?
# print(150_000_000)
# print(15_000_0000)

# What will the following output, and why?
# print(0 in "bob")
# print(0 in ("bob"))
# 0 in ("bob",)     # False
# print(({5} in set({5, 6}))) # works
# print(((3,[]) in set({5, 6}))) # error


# With sequences and sets, both operators (not in or in) compare the object for equality against each collection element.



# What elements will the object referenced by `s` contain when it is printed?

# s = {1, True, 0, 'hi', 1.0, (False)}
# print(s)

# What will the following code output? Why?
# https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

# Jane is confused as to why she is seeing the results below. Can you explain the problem?

l = [1,2,3,4,5]
rev = reversed(l)
print(3 in rev)     # True
print(1 in rev)     # True 
print(5 in rev)     # False


# 5 4 3 2 1
# 
