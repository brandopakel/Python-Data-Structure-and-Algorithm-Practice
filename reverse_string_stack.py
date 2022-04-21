# reversing a string methods in python
a_string = "a string"
a_string[::-1]

# 2
print(''.join(reversed('a string')))

# using a stack to reverse a string

def reverse_string(a_string):
    stack = []
    string = ""
    for c in a_string:
        stack.append(c)
    for c in a_string:
        string += stack.pop()
    return string

print(reverse_string("a string"))