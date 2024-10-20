import random

num = random.randint(1,100)
a = -1
mov = 0

print(num)
while( a != num):
    a = int(input("Guess a number: "))

    if(a == num):
        print(f"Yes You had guess the correct number the number is {num} \nNumber of moves are {mov}")
    else:
        if (a > num ):

            if(a-num <=10):
                print(" You are Close to number")
                mov +=1
            else:
                print(" Chosen Smaller Number ")
            mov +=1
        else:
            if(num-a <= 10):
                print(" You are Close to number")
                mov +=1
            else:
                print(" Chosen Grater Number ")
            mov +=1
        
