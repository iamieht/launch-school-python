# 1. To what values do the following expressions evaluate?
False or (True and False)       # False
True or (1 + 2)                 # True
(1 + 2) or True                 # 3
True and (1 + 2)                # 3
False and (1 + 2)               # False
(1 + 2) and True                # True
(32 * 4) >= 129                 # False
False != (not True)             # False
True == 4                       # False
False == (847 == '847')         # True

# 2. Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.


def even_or_odd(integer):
    print('even' if integer % 2 == 0 else 'odd')


even_or_odd(10)
even_or_odd(3)
