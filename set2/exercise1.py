"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# Creates a list with some words in it. 
some_words = ["what", "does", "this", "line", "do", "?"]

#Loops each item from the list some_words and prints them 
for word in some_words:
    print(word)
#Same thing as above
for x in some_words:
    print(x)
#Prints the list some_words
print(some_words)

#If statement to check if the list length is bigger than 3and prints the following statement
if len(some_words) > 3:
    print("some_words contains more than 3 words")

#UsefulFunction prints out information regarding the current operating system the function uname() was run on.
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())


usefulFunction()
