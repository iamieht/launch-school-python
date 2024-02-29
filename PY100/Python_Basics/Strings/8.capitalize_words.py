# Write code that capitalizes the words in the string 'launch school tech & talk'
def capitalize(string):
    new_string = ''
    for word in string.split():
        new_string += word.capitalize() + ' '

    return new_string


def capitalize_words(string):
    return string.title()


string = 'launch school tech & talk'

print(capitalize(string))
print(capitalize_words(string))
