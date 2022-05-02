N, L = map(int,input().split())
G=[]
for _ in range(N):
    G.append( list(map(int,input().split())))

#가로
# visited= [ [0 for _ in range(N)]for _ in range(N)]

sol=0
for i in range(N):
    line = G[i]    
    before = line[0]
    before_length = 1
    
    j=1 
    while True:
        if j == N:
            sol+=1
            break
        
        now = line[j]
        
        if now==before:
            before_length+=1
            j+=1
        
        elif now == before+1:
            
            if before_length >= L :
                
                before = now
                before_length=1
                j+=1
            
            else:
                break
        
        elif now == before-1:
            before_length=0
            
            if j+L <= N:
                
                for k in range(L):
                    if now == line[j+k] :
                        before_length+=1

                if before_length==L:
                    before = now
                    before_length=0
                    j+=L
                
                else:
                    break
                    
            else:
                break
            
        else:
            break

# print(sol)

for i in range(N):
    before = G[0][i]
    before_length=1
    j=1
    
    while True:
        if j == N:
            sol+=1
            break
        
        now = G[j][i]
        
        if now == before:
            before_length+=1
            j+=1
        
        elif now == before+1:
            if before_length>=L:
                
                before = now
                before_length=1
                j+=1
                
            else:
                break
            
        elif now == before-1:
            before_length=0
            if j + L <= N :
                for k in range(L):
                    if now == G[j+k][i] :
                        before_length+=1
                if before_length==L:
                    before = now
                    before_length=0
                    j+=L
                
                else:
                    break
                    
            else:
                break
        
        else:
            break
        
print(sol)