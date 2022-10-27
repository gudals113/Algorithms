# kakao-blind-2020-5-2.py

def solution(N, build_frame):
    def check(a,gx,gy):
        #x,y의 기둥 혹은 보가 가능한지 검사
        
        if a==0:
            if gx==N-1 :
                return True
            
            elif Gbo[gx][gy]==1 :
                return True
            
            elif gy-1>=0 and Gbo[gx][gy-1]==1:
                return True

            elif gx+1<N and Ggi[gx+1][gy]==1:
                return True
            
            else:
                return False
        
        elif a==1:
            if gx+1 <N and Ggi[gx+1][gy]==1 :
                return True
            elif gx+1<N and gy+1<N and Ggi[gx+1][gy+1] == 1:
                return True
            elif gy-1>=0 and gy+1<N and Gbo[gx][gy-1]==1 and Gbo[gx][gy+1]==1:
                return True
            
            else :
                return False    

            
    answer = []
    N +=1
    Gbo = [ [0 for _ in range(N)] for _ in range(N) ]
    Ggi = [ [0 for _ in range(N)] for _ in range(N)]
    # N+=1
    for inst in build_frame:
        x,y,a,b = inst
        gx,gy = N-1-y, x
        
        #기둥 추가
        if a==0 and b==1:
            
            if check(0,gx,gy):
                Ggi[gx][gy] = 1
                

        
        #보 추가
        elif a==1 and b==1:
            if check(1,gx,gy):
                Gbo[gx][gy] = 1
     
                
        #기둥 삭제
        elif a==0 and b==0:
            Ggi[gx][gy]=0
            
            if gx-1>=0 and Ggi[gx-1][gy]==1 :
                if not check(0, gx-1,gy):
                    Ggi[gx][gy] = 1

            if gx-1>=0 and Gbo[gx-1][gy]==1:
                if not check(1,gx-1,gy) :
                    Ggi[gx][gy] = 1

            if gx-1>=0 and gy-1>=0 and Gbo[gx-1][gy-1]==1:
                if not check(1,gx-1,gy-1):

                    Ggi[gx][gy] = 1
                    
        
        
        #보 삭제
        else:
            Gbo[gx][gy]=0
            
            #바로 위 기둥
            if Ggi[gx][gy]==1:
                if not check(0, gx,gy):
                    Gbo[gx][gy]=1
            #오른쪽 위 기둥
            if gy+1<N and Ggi[gx][gy+1]==1:
                if not check(0, gx,gy+1):
                    Gbo[gx][gy]=1
            
            #왼쪽 보
            if gy-1>=0 and Gbo[gx][gy-1]==1:
                if not check(1, gx,gy-1):
                    Gbo[gx][gy]=1
            
            #오른쪽 보
            if gy+1<N and Gbo[gx][gy+1] == 1:

                if not check(1, gx,gy+1):
         
                    Gbo[gx][gy]=1
                    


    for x in range(N):
        for y in range(N):
            if Ggi[x][y]==1 :
                answer.append([y,N-1-x,0])
            if Gbo[x][y]==1 :
                answer.append([y,N-1-x,1])

    answer.sort(key= lambda x :(x[0],x[1],x[2]))
    return answer    

# solution(5	,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])
solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])