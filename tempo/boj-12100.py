
import copy


N = int(input())
G = [ list(map(int,input().split())) for _ in range(N)]

def move(i):
    if i ==0:
        for y in range(N):
            idx = 0
            newList = []
            for x in range(N):
                if G[x][y]!=0 :
                    
                    if idx==0:
                        idx = G[x][y]
                    
                    #같으면 이전에꺼 2곱하고 넣기
                    elif idx == G[x][y]:
                        newList.append(idx*2)
                        idx = 0
                    #다르면 이전에꺼 넣기
                    elif idx != G[x][y]:
                        newList.append(idx)
                        idx = G[x][y]
                
            #마지막 칸이 빈 칸이 아니었다면
            if idx!=0:
                newList.append(idx)
            
            #아래쪽에 빈칸 채워넣기
            zero = N - len(newList)
            for _ in range(zero):
                newList.append(0)

            #갱신
            for x in range(N):
                G[x][y]=newList[x]
        
     
            
    if i ==1:
    # global G
        for y in range(N):
            idx = 0
            newList = []
            for x in range(N-1,-1,-1):
                if G[x][y]!=0 :
                    
                    if idx==0:
                        idx = G[x][y]
                        
                    elif idx == G[x][y]:
                        newList.append(idx*2)
                        idx = 0
                        
                    elif idx != G[x][y]:
                        newList.append(idx)
                        idx = G[x][y]
                
                
            if idx!=0:
                newList.append(idx)
            
            zero = N - len(newList)
            for _ in range(zero):
                newList.append(0)

            for x in range(N):
                G[x][y]=newList[N-1-x]
        
      
        
    if i ==2:
    # global G
        for x in range(N):
            idx = 0
            newList = []
            for y in range(N):
                if G[x][y]!=0 :
                    
                    if idx==0:
                        idx = G[x][y]
                        
                    elif idx == G[x][y]:
                        newList.append(idx*2)
                        idx = 0
                    elif idx != G[x][y]:
                        newList.append(idx)
                        idx = G[x][y]
                
                
            if idx!=0:
                newList.append(idx)
            
            zero = N - len(newList)
            for _ in range(zero):
                newList.append(0)
            
            G[x]=newList[:]
        # print(G)
    
          
    if i ==3:
    # global G
        for x in range(N):
            idx = 0
            newList = []
            for y in range(N-1,-1,-1):
                if G[x][y]!=0 :
                    
                    if idx==0:
                        idx = G[x][y]
                    elif idx == G[x][y]:
                        newList.append(idx*2)
                        idx = 0
                    elif idx != G[x][y]:
                        newList.append(idx)
                        idx = G[x][y]
                    
            if idx!=0:
                newList.append(idx)
            
            zero = N - len(newList)
            for _ in range(zero):
                newList.append(0)
            
            G[x]=newList[::-1]
        
        

sol = 0
def DFS(count):
    global sol, G

    
    if count == 5:
 
        for i in range(N):
            for j in range(N):             
                if G[i][j]>sol:
                    sol = G[i][j]
        return True
    
    tmp = copy.deepcopy(G)
    for i in range(4):
        move(i)
        DFS(count+1)
        G = copy.deepcopy(tmp)
    
DFS(0)
print(sol)


# r= up(g)
# s= left(r)
# t = down(s)
# l = left(t)
# d = down(l)
# print(d)

