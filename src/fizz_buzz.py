# fizz_buzz() function using TDD:

# testing
# my thoughts
# first make sure everything is set up and the "skeleton" files are linked
# create a setUp function
# check for a false positive by entering different values into a test and the function and run tests
# write 1 test at a time
# write pseudocode for test and only think about how to solve that one task by simplifying it
# then think about expected and actual within assertEqual
# make sure the actual argument calls the function fizz_buzz()
# once 1 test is written, write a section of code for the main function, then continue that for all of the tests
# we have to do multiple tests but we have only one main function
# once the program works and passes the tests, refactor the solution


def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    if number == int(number) or float(number):
        return str(number)
    

# 1: divisible by 3
# if 3 entered, return "fizz" str
# get formula for divisible by 3
# number % 3 == 0

# 2: divisible by 5
# if 5 entered, return "buzz" str
# formula for divisible by 5
# number % 5 == 0

# 3: divisible by 3 AND 5
# if number is divisible by 3 AND 5 (e.g. 30, 5*6 or 3*10)
# return "fizzbuzz"

# 4: when int or float 7 entered, convert it to a str
# use str() method to convert all numbers entered

# things I've learned:
####### when you have conditions, it goes through each line of code from top to bottom until it reaches a condition, then stops there. If the first "if" statement's conditions are met then the program will stop there, and not move to other conditions in lines that come next. It'll stop anywhere where conditions are met.
# so you may need to re-order your conditions, just by reading through each condition and thinking about if some conditions should be put before or after another condition
# as if number % 3 == 0 and number % 5 == 0: return "FizzBuzz" covers both numbers divisible by 3 and 5, that should come first in the conditions so it checks that before checking just divisible by 3 on its own or divisible by 5 on its own
# - should check if the number is in the 3x AND 5x table first before checking if it's in 3x or 5x table
# the number should be converted to a string, 7 was an example given but it should be for all numbers entered
