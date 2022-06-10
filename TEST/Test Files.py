from lib2to3 import pygram
from platform import python_revision


number = 0
def loops_7():
    """Make a pyramid.

    Return this:
    [
        [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
        [' ', '*', '*', '*', '*', '*', '*', '*', ' '],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    ]
    or in more simple terms:
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
    (this is what will print when you test from inside this file)
    This is a hard problem. Use lots of experimentation and draw
    lots of diagrams!
    """
    newcolumns = 5
    newrows = 9
    middle = int((newrows/2))
    lower = middle
    upper = middle
    newlist = []
    minilist = []
    for i in range(1, newcolumns + 1):
        for j in range(lower):
            minilist.append(" ")
        for k in range(upper - lower + 1):
            minilist.append("*")
        for l in range(newrows - upper - 1):
            minilist.append(" ")
        newlist.append(minilist)
        lower = lower - 1
        upper = upper + 1
        minilist = []
    return newlist

def loops_8():
    pyramid = [
            [" ", " ", " ", " ", "*", " ", " ", " ", " "],
            [" ", " ", " ", "*", "*", "*", " ", " ", " "],
            [" ", " ", "*", "*", "*", "*", "*", " ", " "],
            [" ", "*", "*", "*", "*", "*", "*", "*", " "],
            ["*", "*", "*", "*", "*", "*", "*", "*", "*"],
        ]
    return pyramid
def little_printer(some_kind_of_list, exercise_name):
    """Help to see what's going on.

    This is a helper function that prints your
    results to check that they are tidy.
    Note: You don't have to do anything with it.
    """
    if some_kind_of_list is not None:
        print("\n" + exercise_name)
        if type(some_kind_of_list[0]) is list:
            for row in some_kind_of_list:
                for column in row:
                    print(column, end="")
                print()
        else:
            for column in some_kind_of_list:
                print(column, end="")
            print()
    else:
        print(exercise_name, "maybe you haven't got to this one yet?")

if number == 0:
   print (loops_7())
   print (loops_8())
   if loops_7() == loops_8():
       print("This is Correct")


