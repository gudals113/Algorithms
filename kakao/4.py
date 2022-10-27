from itertools import combinations
def solution(n, info):
    
    scoreList = [i for i in range(11)]
    answer = [0 for _ in range(11)]
    answerScore = -1
    candidate=[]
    for i in range(n,0,-1):
        cList = list(combinations(scoreList,i))
        
        for c in cList:
            check = [0 for _ in range(11)]
            for score in c:
                check[10-score]=1
                
            left = n
            lion, apeach = 0,0
            visited = [0 for _ in range(11)]
            for score in range(11):
                if check[10-score]==0 :
                    if info[10-score]>0:
                        apeach+=score
                    continue

                apcCnt = info[10-score]
                
                if apcCnt==0 and left>0:
                    left-=1
                    lion+=score
                    visited[10-score] = 1
                
                elif apcCnt>0 and left>apcCnt:
                    left-=(apcCnt+1)
                    lion+=score
                    visited[10-score] = apcCnt+1
                    
                elif apcCnt>0 and left<=apcCnt:
                    apeach+=score

            if lion>apeach:
                if lion>answerScore:
                    answerScore = lion
                    candidate = [[visited, left]]

                
                elif lion==answerScore:
                    candidate.append([visited, left])
        
    global answerList
    answerList = [0 for _ in range(11)]
    
    def DFS(vList, left):    
        global answerList
        
        if left == 0:
            for i in range(10,-1,-1):
                if answerList[i] < vList[i]:
                    answerList = vList[:]
                    break
                elif answerList[i] > vList[i]:
                    break
            
            return
        
        newV = vList[:]
        for i in range(10,-1,-1):
            newV[i]+=1
            DFS(newV, left-1)
            newV[i]-=1
            
    if answerScore == -1:
        answer =[-1]
        
    else:
        for vList, left in candidate:
            DFS(vList,left)
        answer = answerList

    return answer        
            