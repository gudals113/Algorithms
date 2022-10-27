def solution(n, info):
    global answer, score
    
    answer = [0 for _ in range(11)]
    #get 어피치 점수
    def getScore():
        apeach, lion = 0,0
        for i in range(11):
            if visited[i] > info[i]:
                lion+= 10-i 
            elif info[i]>0:
                apeach+= 10-i
                
        return lion, apeach
        
        
    def check():  
        leftScore=0
        for i in range(11):
            if info[i]==0 and visited[0]==0:
                leftScore += 10-i
        return leftScore
    
    visited = [0 for _ in range(11)]
    score = -1
    def DFS(left,midLion, midAppeach):    
        global answer, score
    
        if left == 0:
            if midAppeach>= midLion:
                return
            
            if midLion > score:
                score = midLion
                answer = visited[:]
            
            elif midLion==score:
                for i in range(11):
                    if answer[i]<visited[i]:
                        answer = visited[:]
                        break
                    elif answer[i]>visited[i]:
                        break                
            return                
        
        for s in range(10,0,-1):
            visited[s]+=1
            lion, apeach = getScore()
            DFS(left-1,lion,apeach)
            visited[s]-=1

    firstLion, firstAppeach= getScore()
    DFS(n,firstLion,firstAppeach)
    
    if score ==-1:
        answer = [-1]
    return answer

solution(5,	[2,1,1,1,0,0,0,0,0,0,0]	)
solution()