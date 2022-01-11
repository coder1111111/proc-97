import random
chances = 0
countnumber =int(input("put a whole number 1-20, try to guess the random number in the fewest tries press enter to submit only press once:"))
randomnumber=random.randint(1,20)

while chances < 5:

        if countnumber == randomnumber:
                print("ding ding ding! WE HAVE A WINNER!")
                break
        if countnumber > randomnumber:
                print("number to big")
                countnumber =int(input("put a whole number 1-20, try to guess the random number in the fewest tries press enter to submit only press once:"))
                chances=chances+1
        if countnumber< randomnumber:
                print("number too small") 
                countnumber =int(input("put a whole number 1-20, try to guess the random number in the fewest tries press enter to submit only press once:"))   
                chances=chances+1
if chances == 5:
        print("you lost") 