
N= int(input())
room=[[0 for _ in range(N)] for _ in range(N)] #채워진 상태

# empty=[ [0 for _ in range(4)] for _ in range(N**2)] #empty[student][0/1/2/3] = 위 /왼/ 오/ 아래 내 주위 비어있는 곳

wanted=[[] for _ in range(N**2)] # 내가 원하는 친구들
assigned=[[-1,-1] * (N**2)] #배정받았는지 체크하기
ace=[1,1] #현재 가장 좋은 자리

#위, 왼, 오, 아래 순서
dx=[0,-1,1,0]
dy=[1,0,0,-1]


for i in range(N**2):
    student, f1,f2,f3,f4 = map(int, input().split())
    wanted[student-1]=[f1-1,f2-1,f3-1,f4-1]
    
    for j in range(4): #원하는 친구 4명 모두 돌려보자
        freind = wanted[student-1][j]
        location_friend=assigned[freind]
        
        tmp=[[0 for _ in range(N)] for _ in range(N)]
        if location_friend==[-1,-1]:
            continue
        
        for k in range(4): 
            nx=location_friend[0]+dx[k] 
            ny=location_friend[1]+dy[k] #친구 배치된 곳 주위 4방향 우선순위대로 보자
            if room[nx][ny]==0 and 0<=nx<N and 0<=ny<N : #아직 배치되어있지 않고 격자를 벗어나지 않으면 배치는 가능
                    if tmp[nx][ny]==0:
                        tmp[nx][ny]=1
                else:
                    tmp[nx][ny]=tmp[nx][ny]*10 #1개만 있으면 1점 2개 10점 3개 100점 4개 1000점
                
    
    for x in range(N):
        for y in range(N):
            if tmp[x][y]==1000 :
                assigned[student-1]=[x,y]
                room[x][y]=1
                continue # for 문 벗어나기
            elif tmp[x][y]==100 :
    
        