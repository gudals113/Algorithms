#백준 1654번 랜선 자르기 (binary search)
import sys   
sys.setrecursionlimit(10000) 

K, N = map(int, input().split())
cable=[]

global sol
sol=0

for _ in range(K):
    cable.append(int(input()))

def cutting(s,t):
    
    if t-s<=1:
        return s

    m=(s+t)//2
    
    sol=0
    for i in range(K):
        sol += cable[i]//m
    # print(sol,s,t,m)
    # print(sol)
    if sol < N :
        return cutting(s,m)
    else :
        return cutting(m,t)

print(cutting(0, (2**31)))
