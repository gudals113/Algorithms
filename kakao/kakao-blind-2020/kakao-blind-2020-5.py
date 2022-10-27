# kakao-blind-2020-5.py
def solution(N, build_frame):
    answer = []
    N +=1
    Gbo = [ [0 for _ in range(N)] for _ in range(N) ]
    Ggi = [ [0 for _ in range(N)] for _ in range(N)]
    # N+=1
    for inst in build_frame:   
        x,y,a,b = inst

        # 기둥 설치
        if a==0 and b==1 :
            
            # 바닥
            if y ==0 : pass
            # 보의 끝
            elif (Gbo[N-1-y][x] == 1) or (x-1>=0 and Gbo[N-1-y][x-1]==1) : pass
            # 기둥 위
            elif y-1>=0 and Ggi[N-1-(y-1)][x] == 1 : pass
            # 다음 스테이지
            else: continue
            
            Ggi[N-y-1][x] = 1
        
        # 보 설치
        elif a==1 and b==1 :            
            # 기둥 위
            if y-1>=0 and (Ggi[N-1-(y-1)][x] == 1 or (x+1 < N and Ggi[N-1-(y-1)][x+1]==1 ) ): 
                pass
            
            # 양쪽 보와 연결
            elif ( x-1>=0 and Gbo[N-y-1][x-1]==1 )  and ( x+1 < N and Gbo[N-y-1][x+1]==1 ) : pass
            
            else:continue
            
            Gbo[N-y-1][x] = 1

    
        # 기둥 삭제
        elif a==0 and b==0 :
            # 내 위에 기둥
            if y+1<N and Ggi[N-1-(y+1)][x] == 1: 
                if not Gbo[N-1-(y+1)][x] == 1 or not ((x-1)>=0 and Gbo[N-1-(y+1)][x] == 1) :
                    continue
                
            # 내 위에 보 인 경우
            elif y+1<N and Gbo[N-1-(y+1)][x] == 1:
                # 반대쪽 끝에 기둥 있으면 삭제 가능.
                if (x+1 < N and Ggi[N-1-y][x+1]==1 ):pass
                # 양쪽 끝 보
                elif x-1>=0 and x+1<N and Gbo[N-1-(y+1)][x-1]==1 and Gbo[N-1-(y+1)][x+1] == 1:pass
                    
                else: continue
                
            # 왼쪽에서 이어지는 보가 있고
            elif y+1<N and x-1>=0 and Gbo[N-1-(y+1)][x-1]==1:
                # 왼쪽 끝에 기둥이 있다면 삭제 가능
                if Ggi[N-1-y][x-1]==1 : pass
                # 왼쪽 끝끝이랑 내위에 보 있으면 삭제 가능
                elif x-2>=0 and Gbo[N-1-(y+1)][x-2]==1 and Gbo[N-1-(y+1)][x] == 1 : pass
                else: continue

            Ggi[N-y-1][x]=0
        
        #보 삭제
        elif a==1 and b==0 :
            
            # 오른쪽 옆에 보가 있고
            if  x+1<N and  Gbo[N-1-y][x+1] == 1 :
                # 그 보 아래에 기둥이 없으면
                if  not (y-1>=0 and Ggi[N-1-(y-1)][x+1] == 1 and x+2<N and Ggi[N-1-(y-1)][x+2]==1 ):
                    continue
            
            #왼쪽에 보가 있다
            elif x-1>=0 and Gbo[N-1-y][x-1] == 1 :
                if not(  y-1>=0 and Ggi[N-1-(y-1)][x-1] == 1 and Ggi[N-1-(y-1)][x]==1  ):
                    continue
                
            # 내 위에 기둥
            elif Ggi[N-1-y][x]==1 :
                if y-1>=0 and y-1>=0 and Ggi[N-1-(y-1)][x]==1 :
                    pass
                
                elif x-1>=0 and Gbo[N-1-y][x-1]==1 :
                    pass

                else: continue
                        
            elif x+1<N and Ggi[N-1-y][x+1]==1 :
                if y-1>=0 and Ggi[N-1-(y-1)][x+1]==1 :
                    pass
                elif x+1<N and Gbo[N-1-y][x+1] == 1:
                    pass
                else: continue
            
            Gbo[N-1-y][x] = 0

    for x in range(N):
        for y in range(N):
            if Ggi[x][y]==1 :
                answer.append([y,N-1-x,0])
            if Gbo[x][y]==1 :
                answer.append([y,N-1-x,1])

    answer.sort(key= lambda x :(x[0],x[1],x[2]))
    
    return answer
solution(5	,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]])