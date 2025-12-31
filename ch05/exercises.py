"""
5.1 Capitalize the word starting with m:
song = When an eel grabs your arm,
... And it causes great harm,
... That's - a moray!
"""
word = "Moray"
song = f"When an eel grabs your arm, And it causes great harm, That's - a {word}!"
print(song)

"""
5.2 Print each list question with its correctly matching answer, in the form:
Q: question
A: answer
"""
"""
>>> questions = [
...
"We don't serve strings around here. Are you a string?"
...
"What is said on Father's Day in the forest?"
,
...
"What makes the sound 'Sis! Boom! Bah!'?"
,
... ]
>>> answers = [
...
...
...
"An exploding sheep.
"
,
"No, I'm a frayed knot.
"'Pop!' goes the weasel."]
"""
questions = ["We don't serve strings around here. Are you a string?", "What is said on Father's Day in the forest?", "What makes the sound 'Sis! Boom! Bah!'?" ]
answers = ["An exploding sheep.", "No, I'm a frayed knot.", "Pop!' goes the weasel."]
for question in questions:
    print("Q:", question)
for answer in answers:
    print("A:", answer)

# Need to figure out

"""
5.3 Write the following poem by using old-style formatting. Substitute the
strings 'roast beef'
'ham', 'head', and 'clam' into this string:
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.
"""
poem = """
My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.
"""
args = ('roast beef', 'ham', 'head', 'clam')
print(poem % args)


"""
5.4 Write a form letter by using new-style formatting. Save the following
string as letter (you’ll use it in the next exercise):
"""

letter = """
Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job}
_
{title}
"""
print(
    letter.format(salutation="Ambassador",
                  name="Nikola",
                  product="Pudding",
                  verbed="Exploded",
                  room="Hotel room",
                  animals="Crocodiles",
                  amount="$1.99",
                  percent="1",
                  spokesman="Ronald Mcdonald",
                  job="SpecOps at Greenfield Pudding",
                  title="Hello")
)
"""
5.6 After public polls to name things, a pattern emerged: an English
submarine (Boaty McBoatface), an Australian racehorse (Horsey
McHorseface), and a Swedish train (Trainy McTrainface). Use % formatting
to print the winning name at the state fair for a prize duck, gourd, and spitz.
"""
names = ["duck", "gourd", "spitz"]
for name in names:
    cap_name = name.capitalize()
    print("%sy Mc%sface" % (cap_name, cap_name))

