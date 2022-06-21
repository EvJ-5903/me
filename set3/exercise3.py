"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random
from turtle import up


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    check = False
    check2 = False
    while check == False:
      flag = False
      try:
          lowerbound = int(input("Enter a lower bound: "))
      except:
          print("No, I said I wanted a number")
          flag = True
      finally:
          if (flag == False):
                while check2 == False:
                  flag = False
                  try:
                    upperbound = int(input("Enter an upper bound: "))
                  except:
                    print("No, I said I wanted a number")
                    flag = True
                  finally:
                    if (flag == False):
                      if (upperbound < lowerbound):
                        print ("Upper Bound cannot be lower than Lower Bound")
                      elif(upperbound == lowerbound):
                        print("Bounds cannot be the same")
                      elif(upperbound - lowerbound == 1):
                        print("You can't guess anything in these bounds")
                      else:
                        print(f"Great! The Bounds are between {lowerbound} & {upperbound}")
                        check2 = True
                        check = True
                        break
    actualNumber = random.randint(lowerbound, upperbound)
    guessed = False
    while not guessed:
      flag1 = False
      try:
        guessedNumber = int(input("Guess a number: "))
        print(f"You guessed {guessedNumber},")
      except:
        print("Not a Number!!")
        flag1 = True
      finally:
        if(flag1 == False):
          if guessedNumber == actualNumber:
            print(f"You got it!! It was {actualNumber}")
            guessed = True
          elif (guessedNumber < actualNumber and guessedNumber < lowerbound and (guessedNumber != lowerbound or upperbound)) or (guessedNumber > actualNumber and guessedNumber > upperbound and (guessedNumber != lowerbound or upperbound)):
            print("Did you know that is outside the bounds? Try again")
          elif (guessedNumber < actualNumber):
            print("Too small, try again :'(")
          else:
            print("Too big, try again :'(")
    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
