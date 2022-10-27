def solution(key, lock):
    answer = False
    N,M  = len(lock), len(key)
    count = 0
    
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
        
    def find(eachKey, basex, basey): 
        tmp = 0 
        for kx in range(M):
            for ky in range(M):
                lx,ly = basex+kx, basey+ky
                # lx,ly = basex,basey
                # key가 왼쪽 위에 간 경우 생각하기
                if 0<=lx<N and 0<=ly<N:
                    if eachKey[kx][ky] == 1 and lock[lx][ly]==0:
                        tmp+=1
                        
                    elif eachKey[kx][ky] ==1 and lock[lx][ly]==1:
                        return -1
                    
                    elif eachKey[kx][ky] == 0 and lock[lx][ly] == 1:
                        pass
                    elif eachKey[kx][ky] ==0 and lock[lx][ly]==0:
                        return -1

        return tmp
    def findleft(eachKey, keyx,keyy):
        tmp = 0
        for lx in range(N):
            for ly in range(N):
                basex,basey = keyx+lx, keyy+ly
                if 0<=basex<M and 0<=basey<M:
                    if eachKey[basex][basey]==1 and lock[lx][ly] == 0 :
                        tmp+=1
                    elif eachKey[basex][basey]==1 and lock[lx][ly] == 1:
                        return 1
                    elif eachKey[basex][basey] == 0 and lock[lx][ly] == 0:
                        return -1
        return tmp

    for i in range(4):
        eachKey = rotate(i)
        print(eachKey)
        for basex in range(N):
            for basey in range(N):
                rst = find(eachKey, basex, basey)

                if rst == count :
                    answer =  True
        
        for keyx in range(M):
            for keyy in range(M):
                rst = findleft(eachKey, keyx,keyy)

                if rst == count :
                    answer = True
    return answer

rst = solution([[1,0,0,1],[1,1,0,1],[1,1,1,1],[1,0,0,0]], [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,0,0],[1,1,1,0,0]] )
print(rst)