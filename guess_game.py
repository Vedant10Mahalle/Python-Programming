import random
def guess_number():
    num=random.randint(1,100)
    attempt=0

    while True:
       
        
        guess=input("Guess a number:")

        guess=int(guess)
        if(guess<num)   :
            print("Too low")
        elif(guess>num):
            print("Too High")

        else:
            print("Correctly guessed")
            break
        attempt+=1    
guess_number()
    