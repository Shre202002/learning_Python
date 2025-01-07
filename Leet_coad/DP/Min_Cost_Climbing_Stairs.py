arr =[1,1,2,3,7,1,4]
i,c = 1,0
while i < len(arr):
    if arr[i] >= arr[i-1]:
        c = c + arr[i]
        i = i +1
        print(f'this is +1 {c}')
        
    else:
        c = c + arr[i+1]
        i = i+2 
        print(f'this is +2 {c}')
print(c)