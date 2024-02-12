# What does this program print? Why?

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# bar because the we pass the variable foo initialize in the global scope as argument of the print function. The new variable foo initialized in the function set_foo definition is local to the function, shadowing the foo variable in line 3, so line 6 doesn't change the value of foo from line 3.