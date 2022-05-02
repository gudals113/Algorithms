start=[]
G=[[0 for _ in range(9)]for _ in range(9)]
for i in range(9):
    line = list(input())
    for j in range(9):
        G[i][j]= int(line[j])
        if int(line[j])==0:
            start.append([i,j])

def DFS(idx):
    
    if idx == len(start):
        for i in range(9):
            print(''.join(map(str,G[i])))
        
        return 1
    
    x,y = start[idx]
    
    if G[x][y] == 0:

        # 가로
        candidate=[0 for _ in range(10)] 
        for i in range(9):
            if G[x][i]!=0:
                candidate[G[x][i]] = 1
                
            if G[i][y]!=0:
                candidate[G[i][y]] = 1
                
            
        nx ,ny = x//3, y//3
        nx, ny = nx*3, ny*3

        for i in range(3):
            for j in range(3):
                if G[nx+i][ny+j] !=0:
                    candidate[G[nx+i][ny+j]] = 1
                
            
        
        for i in range(1,10):
            if candidate[i] == 0:
                
                G[x][y]=i
                if DFS(idx+1) ==1:
                    return 1
                G[x][y]=0
    return 0

        
DFS(0)
