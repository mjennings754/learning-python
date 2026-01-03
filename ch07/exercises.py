"""
7.1 Create a list called years
_
list, starting with the year of your birth, and
each year thereafter until the year of your fifth birthday. For example, if you
were born in 1980, the list would be years
_
list = [1980, 1981, 1982,
1983, 1984, 1985]. If you’re less than five years old and reading this
book, I don’t know what to tell you.
"""
years_list = ['1999', '2000', '2001', '2002', '2003', '2004']

"""
7.2 In which year in years_list was your third birthday? Remember, you
were 0 years of age for your first year.
"""
print(years_list[3])

"""
7.3 In which year in years_list were you the oldest?
"""
print(years_list[-1])

"""
7.4 Make a list called things with these three strings as elements:
"mozzarella"
"cinderella"
"salmonella"
"""
things = ["mozzarella", "cinderella", "salmonella"]

"""
7.5 Capitalize the element in things that refers to a person and then print
the list. Did it change the element in the list?
"""
print(things[1].capitalize())

"""
7.6 Make the cheesy element of things all uppercase and then print the list.
"""
print(things[0].upper())

"""
7.7 Delete the disease element from things, collect your Nobel Prize, and
print the list.
"""
things.pop()
print("Collecting Nobel Prize...")
print(things)

"""
7.8 Create a list called surprise with the elements "Groucho"
,
and "Harpo"
.
"Chico"
,
"""
surprise = ["Groucho", "Harpo", "Chico"]

"""
7.9 Lowercase the last element of the surprise list, reverse it, and then
capitalize it.
"""
print(surprise[-1].lower())
print(surprise[-1][::-1])
print(surprise[-1].upper())

"""
7.10 Use a list comprehension to make a list called even of the even
numbers in range(10).
"""

even = [number for number in range(10) if number % 2 == 0]
print(even)