# Write code that removes the items from grocery_list, one by one, until it is empty.
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

temp_grocery_lst = list(grocery_list)

for item in temp_grocery_lst:
    print(item)
    grocery_list.remove(item)

print(grocery_list)
