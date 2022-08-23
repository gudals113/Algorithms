# boj-2170.py
# 선 긋기
# sol 220721
# sweeping
# sort 할 때, L.sort(key = lambda x : (x[0],x[1])) 으로 하면 시간초과 발생
import sys
input = sys.stdin.readline
N = int(input())
L=[]

for _ in range(N):
    L.append(list(map(int, input().split())))

L.sort(key = lambda x :x[0])
answer = 0
s,e = L[0]
for i in range(1,len(L)):
    x,y = L[i]
    
    if x<= e:
        e= max(e,y)
        
    else: # x>tmp[1]
        answer += e-s
        s,e = x,y
 
answer+=e-s
print(answer)