# Without running the following code, determine what each print statement should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)   # => True
print('Butter' in cats)         # => False
print('Butter' in cats[3])      # => True
print('cheddar' in cats)        # => False

# Note 1: "string in list" must match a list element exactly.
# Note 2: cats[3] is 'Butterscotch' and 'Butter' is in 'Butterscotch'.