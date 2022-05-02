#톱니바퀴 ( 삼성, 구현)
chain=[]
for _ in range(4):
    chain.append(input())
    

def turn(n, w):
    global chain
    if w == 1:
        newchain = chain[n][7]+chain[n][0:7]
        chain[n] = newchain[:]
    
    else :
        newchain = chain[n][1:8]+chain[n][0]
        chain[n] = newchain[:]
    


K = int(input())

for _ in range(K):
    num, way = map(int, input().split())
    
    now = chain[num-1]
    now_left , now_right = now[6], now[2] 
    
    turn(num-1,way)
    
    #오른쪽에 있는 것들
    if way == 1:
        nway = -1
    elif way ==-1:
        nway = 1    
        
    for i in range(num, 4) :
        right = chain[i]
        
        if now_right != right[6] :
            now_right = right[2]    
            turn(i,nway)
            
            if nway == -1:
                nway = 1
            else:
                nway = -1
            
        else:
            break        
        
    #왼쪽
    if way == 1:
        nway = -1
    else:
        nway = 1
    for i in range(num-2, -1,-1):
        left = chain[i]
        
        if now_left != left[2] :
            now_left = left[6]
            turn(i,nway)
            if nway == -1:
                nway = 1
            else:
                nway = -1
        else:
            break
    

sol=0
for i in range(4):
    if chain[i][0] == '1' :
        sol += 2**i
print(sol)
