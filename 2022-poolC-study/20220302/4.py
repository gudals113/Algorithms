N,M, x,y, K = map(int,input().split())
G= []
for i in range(N):
    G.append( list(map(int, input().split())) )
A = list(map(int, input().split()))

#위 아래, 앞, 뒤, 왼 , 오
cube = [0,0,0,0,0,0]


for i in range(K):
    
    inst = A[i]
    
    if inst ==1:
        nx,ny = x, y+1
        
        if nx>=0 and nx<N and ny>=0 and ny<M:
            x,y, = nx, ny
            tmp = [cube[4], cube[5] , cube[2] ,cube[3] , cube[1], cube[0]]
            cube = tmp[:]
            
            print(cube[0])
            
            if G[nx][ny]==0:
                G[nx][ny]= cube[1]
            else :
                cube[1] = G[nx][ny]
                G[nx][ny]=0
            
    elif inst ==2:
        nx,ny = x, y-1
        
        if nx>=0 and nx<N and ny>=0 and ny<M:
            x,y, = nx, ny
            tmp = [cube[5], cube[4]  ,cube[2] ,cube[3] , cube[0], cube[1]]
            cube = tmp[:]
            print(cube[0])
            if G[nx][ny]==0:
                G[nx][ny]= cube[1]
            else :
                cube[1] = G[nx][ny]
                G[nx][ny]=0
        
    
    elif inst==3:
        nx,ny = x-1, y
        
        if nx>=0 and nx<N and ny>=0 and ny<M:
            x,y, = nx, ny
            tmp = [cube[2], cube[3] , cube[1], cube[0] , cube[4], cube[5]]
            cube = tmp[:]
            print(cube[0])
            if G[nx][ny]==0:
                G[nx][ny]= cube[1]
            else :
                cube[1] = G[nx][ny]
                G[nx][ny]=0
    
    elif inst==4:
        
        nx,ny = x+1, y
        
       
        if nx>=0 and nx<N and ny>=0 and ny<M:
            
            x,y, = nx, ny
            
            tmp = [cube[3], cube[2] , cube[0], cube[1] , cube[4], cube[5]]
            cube = tmp[:]
            print(cube[0])
            if G[nx][ny]==0:
                G[nx][ny]= cube[1]
            else :
                cube[1] = G[nx][ny]
                G[nx][ny]=0
   
    