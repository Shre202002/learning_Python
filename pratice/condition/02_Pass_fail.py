# Input 3 subject marks and check weather student is pass or fail 

m={
    # 'a':10,
    # 'b':20,
    # 'c':30,
    
}



b = input("Subject name: ")
a = int(input("Enter marks: "))
m.update({b:a})

b = input("Subject name: ")
a = int(input("Enter marks: "))
m.update({b:a})

b = input("Subject name: ")
a = int(input("Enter marks: "))
m.update({b:a})


Fm = {key: value for key, value in m.items() if value < 33}

print(f"{index}: Subject = {key}, marks = {value}")

p = (sum(m.values())/300)*100




print("Your Percentage SCORE IS: ",p)

if(p<33):
    print("You Are Failed In Examination \n Better Luck Next time ")
elif(p>=33 and p<=40):
    print("You are Just passes \n You need Improvement ")
elif(p>=41 and p<=60 ):
    print("You are Ok in Studies \n But You Need Improvement")
else:
    print("You Scored Well In Examination ")


