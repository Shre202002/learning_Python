#lambda functions 
# addition of 2 numbers 
# sum1 = lambda num1, num2 : num1+num2
# print(f"The sum of two number is {sum1(34,69)}")

# list=[6,5,'raj',6.0,'s']
# print(list[1:3])

# #lex_auth_012693750719488000124

def get_count(num_list):
    count=0

    # Write your logic here
    
    for i in range(len(num_list)):
        if(num_list[i] == num_list[i-1]):
            count += 1
        
    
    return count

#provide different values in list and test your program
num_list=[1,1,1,5,100,-20,-20,6,0,0]

print(get_count(num_list))