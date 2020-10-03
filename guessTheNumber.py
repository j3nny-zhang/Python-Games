import random
def main():
    randomNumber = random.randint(1,10)

    print(randomNumber)

    userInput = input("Please enter an integer between 1 and 10:\n")
    userInput = int(userInput)

    print("You entered: " + str(userInput))
   

    while randomNumber != userInput:
        if randomNumber > userInput:
            print("Higher!")
            userInput = input("Please enter an integer between 1 and 10:\n")
            userInput = int(userInput)
        else:
            print("Lower!")
            userInput = input("Please enter an integer between 1 and 10:\n")
            userInput = int(userInput)
    print("You guessed correctly!")
        
   
main()
