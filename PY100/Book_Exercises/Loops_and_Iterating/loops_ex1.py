# The following code causes an infinite loop (a loop that never stops iterating). Why?

counter = 0

while counter < 5:
    print(counter)

# the expression counter < 5 will always be truthy as counter is not changed in the loop body.
