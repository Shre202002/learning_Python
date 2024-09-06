# PYTHON PROGRAM FOR SNAKE WATER AND GUN GAME 

import random

'''
 -1-> water
 0 ->  snake
 1 -> gun
 
'''
def result(c,y):
        
    if(c==y):
        return "Game is draw "
    else:
        if(c == 0 and y == 1):
            return "You Win "
        
        elif(c == 0 and y == -1):
            return " Computer Win "
        
        elif(c == -1 and y == 0):
            return " You Win"
        
        elif(c == -1 and y == 1):
            return " Computer Win "
    
        elif(c == 1 and y == 0):
            return " Computer Win"
        
        elif(c ==-1 and y == -1):
            return " You Win "
    
    
c_choice =random.choice([-1,0,1])
you = input("Enter your choice: ")
convert_dict= {'g': 1, 's':0, 'w':-1}
result_dict = {1:"Snake", 0: "Snake", -1: "Water"}
y_choice = convert_dict[you]

print(f"you had chosen: {result_dict[y_choice]}\nComputer had chosen :{result_dict[c_choice]}")

print(result(c_choice, y_choice))



