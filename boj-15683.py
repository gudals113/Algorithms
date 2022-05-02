N,M = map(int,input().split())
G=[]
cam = [[]for _ in range(6)]

for i in range(N):
    line = list(map(int,input().split()))
    for j in range(M):
        if 1<=line[j]<=5:
            cam[line[j]].append([i,j])
            
    G.append(line)
    

for x,y in cam[5]:
    