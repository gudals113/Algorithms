#11559.py
#뿌요뿌요 , 구현, sol220630
from collections import deque
import copy


G=[['.'for _ in range(6)]for _ in range(12)]
for x in range(12):
    l = input()
    for y in range(6):
        G[x][y]=l[y]
    
chain = 0    
while True:
    boom=0    
    visited=[ [0 for _ in range(6)]for _ in range(12)]
    for x in range(12):
        for y in range(6):
 
            if not visited[x][y]:
                    
                visited[x][y]=1
                color = G[x][y]
                
                if color=='.':
                    continue
                
                else:
                    
                    newG = copy.deepcopy(G)
                    newG[x][y]='.'
                    count = 1
                    q=deque([[x,y]])
                    
                    while q:
                        i,j = q.popleft()
                        for ni,nj in ([i+1,j],[i-1,j],[i,j+1],[i,j-1]):
                            if 0<=ni<12 and 0<=nj<6 and not visited[ni][nj] and newG[ni][nj]==color:
                                count+=1
                                visited[ni][nj]=1
                                newG[ni][nj]='.'
                                q.append([ni,nj])
                                
                    if count>=4:
                        boom=1
                        G=copy.deepcopy(newG)
          
    if boom==0:
        break                    
    else:

        chain+=1
        for x in range(10,-1,-1):
            for y in range(5,-1,-1):
                
                color = G[x][y]

                if color != '.' and G[x+1][y]=='.':
                    
                    idx = 0
                    while x+idx<11:
                        if G[x+idx+1][y]=='.':
                            idx+=1
                        else:
                            break
                    
                    G[x+idx][y] = color
                    G[x][y] = '.'
            
   
            
            
print(chain)
# for i in range(12):
#     print(*G[i])
         
                            
  
                
                

