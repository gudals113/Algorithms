# 소수 경로
# 소수 판별, BFS
# sol 220824

from collections import defaultdict, deque
INF = float('inf')
dp=[1 for _ in range(10000)]
dp[0]=0
dp[1]=0
for num in range(10000):
    if dp[num]==1:
        for i in range(2,10000):
            if num*i>=10000:
                break
            dp[i*num]=0
                
def BFS(start):
    answer = INF
    q= deque([[0, start]])
    while q:
        count, num = q.popleft()
        if num== end:
            answer = count
            break
        
        numList = [num[s] for s in range(4)]
        for place in range(4):
            now = num[place]
            for i in range(10):
                if i !=int(now):
                    newNumList= numList[:]
                    newNumList[place] = str(i)
                    newNum=''.join(newNumList)
                    
                    if int(newNum)>999 and dp[int(newNum)] == 1:
                        if visited[newNum]==0:
                            visited[newNum]=1
                            q.append([count+1, newNum])
                            
    return answer

T = int(input())
for stage in range(T):
    start, end = input().split()
    visited=defaultdict(int) #횟수 표시 해야 하나?? 1234 -> 4234 
    visited[start]=1
    rst = BFS(start)
    if rst == INF:
        rst= 'Impossible '
    print(rst)