#시장 선거 포스터
#좌표 압축
#220708 poolc study, try, 
import sys
input = sys.stdin.readline

N = int(input())
L = []
plane = []
for _ in range(N):
    l, r = map(int, input().split())
    plane.append(l)
    plane.append(r)
    L.append([l,r])

setPlane = set(plane)
plane = list(setPlane)
plane.sort()

dictPlane = {}
for i in range(len(plane)):
    val = plane[i]
    dictPlane[val] = i

answer = [-1 for _ in range(len(plane))]
for i in range(N):
    l,r = L[i]
    dl, dr = dictPlane[l], dictPlane[r]
    
    for k in range(dl,dr+1):
        answer[k] = i
print(answer)  
visited={}
for i in range(len(answer)):
    visited[answer[i]]=1

print(len(visited))
    




