# 선물 전달

N = int(input())

poor = {}
for i in range(N):
    poor[i]=1
answer = 0    
def DFS(idx):
    global answer
    
    if idx==N:
        answer+=1
        return
    
    
    poorList = list(poor)

    for p in poorList:
        if idx!=p :
            del poor[p]       
            DFS(idx+1)
            poor[p]=1

# DFS(0)
# print(answer)

# 전체 경우의 수 - 1이 자기 선물 받는 경우의수 - 2이 자기 선물.. -N 자기 선물
# + 1,2 자기 선물 받는 경우의 수 + 1,2,3 자기 선물, 2,3
# 12/23/34/45/ 123/ 234...흠..

#dp?


