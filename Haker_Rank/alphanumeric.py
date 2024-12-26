s = '125'
n,u,c=0,0,0
for i in s:
     if '0' <= i <= '9':
          n=n+1
     if 'a' <= i <= 'z':
          c= c+1
     if 'A' <=i <= "Z":
          u+=1
print('True' if n or c or u else 'False')  
print('True' if c or u else 'False')   
print('True' if n else 'False')   
print('True' if c else 'False') 
print('True' if u else 'False')  
