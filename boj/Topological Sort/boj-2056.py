#작업
#위상정렬
#220727 sol

#선행 작업의 번호가 반드시 작으므로 queue 혹은 방문 처리할 필요 없이 풀 수 있다.
N = int(input())

time = [ 0 for _ in range(N+1)]
toG = [[]for _ in range(N+1)]
for i in range(1,N+1):
    l = list(map(int, input().split()))
    
    time[i] = l[0]
    count = l[1]
    
    for c in range(count):
        pre = l[c+2]
        toG[pre].append(i)

start = [0 for _ in range(N+1)]
answer = 0

for idx in range(1,N+1):
    cost = start[idx] + time[idx]
    if len(toG[idx]) == 0 :
        answer = max(answer, cost)
        
    for next in toG[idx]:
        start[next] = max(start[next], cost)
                
print(answer)