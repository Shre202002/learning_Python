a = True
b = False
c = False

# and have More Presedane tha OR

if not a or b: #(FALSE || False)
# True ! -> False || False -----> False     
    print(1)
    
    
elif not a or not b and c: #(False || True---> True  && False ---> False )
#   True!->(false) || False ! ---> True ---> TRUE && False ---> FALSE 
    print(2)
    
    
    
elif not a or b or  not b and   a : #( false || False || True---> True && True ---> True )
#   True!-> (flase)||(false)|| False!---> (True) ----> TRUE   && (True)---------> True
    print(3)
    
    
    
else:
    print(4)
    
    
