
def table(t):   
 table = ""
 for i in range (1,11):
    table += f"{t} X {i} = {t*i} \n"
 with open(rf"D:\learning_Python\pratice\File_IO\Third\Tables\Table_of_{t}.txt","w") as f:
   f.write(table)

for n in range (2 , 21):
    table(n)

