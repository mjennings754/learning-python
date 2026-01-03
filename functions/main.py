"""
Functions
The first step to code reuse is the function: a named piece of code, separate
from all others. A function can take any number and type of input
parameters and return any number and type of output results.
"""

def item_details(required1, required2, *args):
    print(required1, required2)
    print("Other information:")
    print(args)

item_details('460491', 'Supima Cotton T-shirt', '26SS', 'SU', 19.90, "69 NAVY", "200010293891802")
