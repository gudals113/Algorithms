# DSLR
# BFS
# hint 220804
# 문자열 변환하는 것이 생각보다 시간이 많이 발생한다.

from collections import deque

inst = ['D','S','L','R']
def cal(intNum, idx):

    if idx == 0:
        intRst = (intNum*2)%10000
    
    elif idx == 1:
        if intNum == 0 :
            intRst = 9999
        else:
            intRst = intNum-1
    
    elif idx == 2:
        mok = intNum//1000
        intRst = mok+ (intNum*10) % 10000
        
    elif idx == 3:
        mok = intNum//10
        intRst = mok + (intNum%10)*1000
        
    return intRst


T = int(input())
for _ in range(T):
    start,end  = map(int, input().split())
    visited = [0 for _ in range(10000)]
    visited[start]=1
    
    q= deque()
    q.append([start,''])
    while q:
        intNum, tmp = q.popleft()
        
        if intNum == end :
            break
        
        for i in range(4):
            nextIntNum = cal(intNum, i)
            if not visited[nextIntNum]:
                visited[nextIntNum]=1
                q.append([nextIntNum, tmp+inst[i]])

    print(tmp)