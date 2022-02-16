# IOI
N=int(input())
length = int(input())
string = input().split('I')
sol=0
tmp=0
for i in range(len(string)) :
    
    if string[i] == 'O' and i!=len(string)-1:
        
        tmp+=1
    
    
    
    elif i==len(string)-1 or string[i] !='O':
        count = tmp-N+1
        if count > 0:
            sol+=count
        tmp=0
        
print(sol)

