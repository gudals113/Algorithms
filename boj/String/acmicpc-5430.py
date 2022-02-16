T= int(input())

def AC():
    p = input()
    N = int(input())
    arr = input()
    arr=arr[1:-1].split(',')

    way = 1
    f, b = 0,0
    for i in range(len(p)):
        if p[i] == 'R' :
            way *= -1
        
        else:
            # d= len(p[i])
            
            if way ==1:
                f+=1
            else :
                b-=1
                
    if (arr==[''] and f-b>0) or f-b > len(arr):
        print('error' )          
    else:
        
        if b==0:
            arr=arr[f:]
        else:
            arr=arr[f:b]
        
        
        if way==-1:
            arr.reverse()
        print(arr)
        str='[' + ','.join(arr)+']'
        print(str)
    return

for _ in range(T):
    AC()