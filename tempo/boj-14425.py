#문자열 집합
from collections import defaultdict

N,M = map(int,input().split())
dict=defaultdict(int)
for _ in range(N):
    dict[input()]+=1
sol=0
for _ in range(M):
    if input() in dict:
        sol+=1
print(sol)