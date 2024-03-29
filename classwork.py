# ### Problem 1:
# Write some Python code that has three variables called ```greeting```, ```my_name```, and ```my_age```. Intialize each of the 3 variables with an appropriate value, then print out the example below using the 3 variables and two different approaches for formatting Strings.
#
# 1) Using concatenation and the ```+``` and 2) Using an ```f-string```. Sample output:
#
# ```
# YOUR_GREETING_VARIABLE YOUR_NAME_VARIABLE!!! I hear that you are YOUR_MY_AGE_VARIABLE today!
# ```
#
#todo validate the welcome1

# greeting= "Hello Homie"
# my_name = "Jarvis"
# my_age = "29"
# welcome1 =(${greeting} + ${my_name} + '!!  I hear that you are' + ${my_age} + 'today!')
# # you are trying to do JS string templating
# welcome2 = f'{greeting} {my_name} !!!  I hear that you are  {my_age} today!'
# print(welcome1)
# print(welcome2)



# ### Problem 2:
# Write some Python code that asks the user for a secret password. Create a loop that quits with the user's quit word. If the user doesn't enter that word, ask them to guess again.
#
secret_word = input("Enter a secret word ")
# the quit word should be define by the user not hard coded
while (secret_word.lower() != 'blue'):
    secret_word = input("Enter a secret word ")

#
# ### Problem 3:
# Write some Python code using ```f-strings``` that prints 0 to 50 three times in a row (vertically).
# ```
# 1 1 1
# 2 2 2
# 3 3 3
# 4 4 4
# 5 5 5
# .
# .
# .
# ```


x = range(0,50+1,1)
for n in x:
    print(f'{n}  {n}  {n}')




# ### Problem 4:
# Write some Python code that create a random number and stores it in a variable. Ask the user to guess the random number. Keep letting the user guess until they get it right, then quit.
#

import random
rand_num = random.randint(1,5)
rand_guess = " "
while rand_num != rand_guess:
    rand_guess = int(input("enter a guess 1-5 "))
     # this is redundant
    if rand_num != rand_guess:
        print('try again')
else:
    print('you got it')






# ### Challenge
# Write some Python code to ask the user to create a number for the computer to guess between 1 - 10000. Write the code so that the computer guesses random numbers between 1 - 10000 and will keep guessing until the computer guesses the number correctly. Once the computer guesses the random number, alert the user with an alert box that displays how many guesses it took to guess the random number.