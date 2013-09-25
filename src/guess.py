#! /usr/bin/python
''' Khara fist app 
    multiple line comment'''
import random
guessesTaken = 0 
print('Hello! What is your name? ')
myName = raw_input()

number = random.randint(1,10)
print('Well, ' + myName + ',I am thinking of number between 1, 10')
while guessesTaken < 6:
    print ('Take a guess')
    guess = input()
    guess = int(guess)
    guessesTaken +=1
    if guess < number:
        print ("Your guess is too low")
    if guess > number:
        print ("Your guess is too high")
    if guess == number:
        break
        
if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good job, " + myName + "! You guesssed my numner in " + guessesTaken + ' gueses!')
if guess != number:
    print ("Nope the numbr is was thiking was: " + str(number))
    

        
        
        
    


