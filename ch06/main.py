# repeat with while
count = 1
while count <= 5:
    print(count)
    count += 1

# Cancel with break

while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == 'q':
        break
    print(stuff.capitalize())

# Skip ahead with continue
while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is", number*number)
    
# Iterate with for and in

word = 'thud'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1

# Cancel with break

word = 'thud'
for letter in word:
    if letter == 'u':
        break
    print(letter)

# Generate number sequences with range()

for x in range(0,3):
    print(x)

print(list(range(0, 3)))

# Here's how to make a range from 2 down to 0:
for x in range(2, -1, -1):
    print(x)

