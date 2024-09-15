import random

def game():
    score = random.randint(1, 100)
    # print(f"Your score is {score}")

    with open(r"D:\learning_Python\pratice\File_IO\second\highscrre.txt") as f:
        highscore = f.read()
        
        if (highscore != ""):
            highscore = int(highscore)
        else:
           highscore = 0
    print(f"your Score is {score}")
    if(score>highscore):
        with open(r"D:\learning_Python\pratice\File_IO\second\highscrre.txt","w") as f:
            f.write(str(score))

game()
