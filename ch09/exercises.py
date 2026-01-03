"""
9.1 Define a function called good() that returns the following list:
['Harry','Ron','Hermione'].
"""

def good():
    return ['Harry','Ron','Hermione']

print(good())

"""
9.2 Define a generator function called get_odds() that returns the odd
numbers from range(10). Use a for loop to find and print the third value
returned.
"""

def get_odds():
    for number in range(1, 10, 2):
        yield number

count = 1
for number in get_odds():
    if count == 3:
        print("The number is", number)
        break
    count += 1

"""
9.3 Define a decorator called test that prints 'start' when a function is
called, and 'end' when it finishes.
"""

def test(func):
    def new_func(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_func
@test
def greeting():
    print("Hello")

greeting()

"""
9.4 Define an exception called OopsException. Raise this exception to see
what happens. Then, write the code to catch this exception and print
'Caught an oops'.
"""

class OopsException(Exception):
    pass

#raise OopsException()

try:
    raise OopsException
except OopsException:
    print("Caught an oops")