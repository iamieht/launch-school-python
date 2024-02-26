"""
    - define a function, `find_substring` with two parameters: `string` and `substring`:
        - initialize variable `occurrences` to 0
        - initialize variable `should_search` to result of logical conditions:
            - `string` and `substring` both have a length greater than 0
            - `substring` has a length <= the length of `string`

        - if `should_search` is truthy:
            - initialize variable `start_index` to 0
            - initialize variable `stop_index` to (length of substring)
            - loop while `stop_index` is >= length of `string` (Comparison operator must be <= (less than) otherwise we run into an infinite loop)
                - if `string` sliced from `start_index` to `stop_index` is == `substring`:
                    - increment occurrences by 1
                - increment `start_index` by 1
                - increment `stop_index` by 1

        - print `'Number of times <substring> occurs is: <occurrences>'`
    
    example:
    - find_substring('azcbobobegghakl', 'bob')    # Number of times bob occurs is: 2
    - find_substring('bob', 'bob')                # Number of times bob occurs is: 1
    - find_substring('', '')                      # Number of times  occurs is: 0
    - find_substring('azcbobobegghakl', 'alice')  # Number of times alice occurs is: 0
    - find_substring('hi', 'hmmmm')               # Number of times hmmmm occurs is: 0
"""
"""
Obervations:
* loop while `stop_index` is >= length of `string` 
(Comparison operator must be <= (less than or equal to) otherwise we run into an infinite loop)

The rest worked like a charm.
"""


def find_substring(string, substring):
    occurrences = 0
    should_search = (True if len(string) > 0
                     and len(substring) > 0
                     and len(substring) <= len(string)
                     else False)

    if should_search:
        start_index = 0
        stop_index = len(substring)

        while stop_index <= len(string):
            if string[start_index:stop_index] == substring:
                occurrences += 1
            start_index += 1
            stop_index += 1

    print(f'Number of times {substring} occurs is: {occurrences}')


# Examples:
find_substring('azcbobobegghakl', 'bob')
find_substring('bob', 'bob')
find_substring('', '')
find_substring('azcbobobegghakl', 'alice')
find_substring('hi', 'hmmmm')
