def solution(key, lock):
    INF = float('inf')
    N,M = len(lock),len(key)
    count = 0
    
    # 맞춰야 하는 홈의 개수    
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                count+=1

    def rotate(i):
        if i== 0 : newKey = key[:]
        
        elif i==1:
            
            newKey = [[0 for _ in range(M)]for _ in range(M)]
            for x in range(M):
                for y in range(M):
                    newKey[y][M-1-x] = key[x][y]

        elif i==2:
            newKey = [[0 for _ in range(M)]for _ in range(M)]
            for x in range(M):
                for y in range(M):
                    newKey[M-1-x][M-1-y] = key[x][y]
        elif i==3:
            newKey = [[0 for _ in range(M)]for _ in range(M)]
            for x in range(M):
                for y in range(M):
                    newKey[M-1-y][x] = key[x][y]        
        return newKey
    
    
    # [0,0],[0,N-1], [N-1,0], [N-1,N-1]
    def find(eachKey, fix):
            #key의 왼쪽 위 고정.
        for kx in range(M):
            for ky in range(M):
                tmp = 0
                if fix == 0:
                    for lx in range(N):
                        for ly in range(N):
                            if 0 <= kx+lx < M and 0<=ky+ly<M:
                                if eachKey[kx+lx][ky+ly] == 1 and  lock[lx][ly]==0:
                                    tmp+=1
                                elif eachKey[kx+lx][ky+ly] == 1 and  lock[lx][ly]==1:
                                    tmp=INF
                    if tmp == count:
                        return True 
                    
                elif fix == 1:
            # key 왼쪽 아래 고정.

                    for lx in range(N):
                        for ly in range(N):
                            if 0<=kx-lx<M and 0<=ky+ly<M:
                                if eachKey[kx-lx][ky+ly] ==1 and lock[N-1-lx][ly]==0:
                                    tmp +=1
                                elif eachKey[kx-lx][ky+ly] == 1 and  lock[N-1-lx][ly]==1:
                                    tmp=INF
                elif fix == 2:
            # key 오른쪽 위 고정.
      
                    for lx in range(N):
                        for ly in range(N):
                            if 0<=kx+lx<M and 0<=ky-ly<M:
                                if eachKey[kx+lx][ky-ly] == 1 and lock[lx][N-1-ly]==0:
                                    tmp +=1
                                    
                                elif eachKey[kx+lx][ky-ly]== 1 and  lock[lx][N-1-ly]==1:
                                    tmp=INF
                                    
                elif fix == 3:
                    for lx in range(N):
                        for ly in range(N):
                            if 0<=kx-lx<M and 0<=ky-ly<M:
                                if eachKey[kx-lx][ky-ly] == 1 and lock[N-1-lx][N-1-ly]==0:
                                    tmp +=1
                                    
                                elif eachKey[kx-lx][ky-ly] == 1 and  lock[N-1-lx][N-1-ly]==1:
                                    tmp=INF

 
                if tmp == count :
                        return True
                    
        return False
    
    for i in range(4):
        eachKey = rotate(i)
        for fix in range(4):
            if find(eachKey, fix):
                return True

    return False

rst = solution([[1,1,1]for _ in range(3)], [ [1,1,1] for _ in range(3)])
print(rst)
