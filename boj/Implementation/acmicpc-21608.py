
N= int(input())
room=[[0 for _ in range(N)] for _ in range(N)] #채워진 상태

# empty=[ [0 for _ in range(4)] for _ in range(N**2)] #empty[student][0/1/2/3] = 위 /왼/ 오/ 아래 내 주위 비어있는 곳

wanted=[[] for _ in range(1+ N**2)] # 내가 원하는 친구들
assigned=[[-1,-1] for _ in range (1+ N**2)] #배정받았는지 체크하기
#위, 왼, 오, 아래 순서
dx=[0,-1,1,0]
dy=[1,0,0,-1]

def check_blank(x,y): # x , y 주위의 4칸에 빈칸이 몇개나 있는가?
    count=0
    for i in range(4):
        nx= x+dx[i]
        ny= y+dy[i]
        if 0<=nx< N and 0<=ny<N and room[ nx ][ ny ] ==0:
            count+=1
    
    return count

sol=0
score=[0,1,10,100,1000]

for i in range(N**2):
    student, f1,f2,f3,f4 = map(int, input().split())
    wanted[student]=[f1,f2,f3,f4]
    
    #각 학생 배치를 위해 배열 넣어두기
    tmp=[ [], [], [], [] ]
    for j in range(4): #원하는 친구 4명 모두 돌려보자
        freind = wanted[student][j]
        location_friend=assigned[freind]
        
        if location_friend==[-1,-1]: #친구가 아직 배치되어 있지 않다면 
            # print("배치해야될사람/ 그 친구",student, freind)
            continue
        
        for k in range(4): 
            nx=location_friend[0]+dx[k] 
            ny=location_friend[1]+dy[k] #친구 배치된 곳 주위 4방향 우선순위대로 보자
            if 0<=nx<N and 0<=ny<N and room[nx][ny]==0: #아직 배치되어있지 않고 격자를 벗어나지 않으면 배치는 가능
                    blank=check_blank(nx,ny)
                    plan = [nx,ny, blank]
                    if plan not in tmp[0]:
                        tmp[0].append(plan)
                    else:
                        if plan not in tmp[1]:
                            tmp[1].append(plan)
                        else:
                            if plan not in tmp[2]:
                                tmp[2].append(plan)
                            else:
                                tmp[3].append(plan)

    select=[-1,-1]
    for l in range(3,-1,-1):
        if tmp[l]!=[] :
            tmp[l].sort(key=lambda x: (-x[2], x[0], x[1]))
            select=tmp[l][0]
            # sol+= score[l] # 수정
            break
    
    if select==[-1,-1]:
        ans=0
        ans1=[]
        for x in range(N):
            for y in range(N):
                if room[x][y]==0:
                    blank=check_blank(x,y)
                    
                    if ans < blank :
                        ans=blank
                        select=[x,y]
                    
                    if blank==0:
                        ans1.append([x,y])
                        
                    
        if ans==0:
            select=ans1[0]
                
    # print("student",student, "select:", select,"tmp:", tmp )    
    assigned[student]= select
    room[ select[0] ][ select[1] ]= student


for i in range(1, 1+N**2):
    how=0
    x,y = assigned[i][0], assigned[i][1] # 학생의 위치
    
    for j in range(4):
        nx ,ny = x+dx[j], y+dy[j]
        if 0<=nx<N and 0<=ny<N :
            who = room[nx][ny] # 내 주위에는 누가 있을까

            if who in wanted[i] :
                how +=1
                
    sol+=score[how]
        

print(sol)