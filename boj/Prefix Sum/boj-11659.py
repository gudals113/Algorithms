#구간 합 구하기 4
import sys 
input = sys.stdin.readline
N,M=map(int,input().split())
A = [0]+list(map(int,input().split()))
prefix = [ 0 for _ in range(N+1)] # prefix[i] = 0번부터 i번까지 합
for i in range(1,N+1):
    prefix[i] = prefix[i-1]+A[i]

for _ in range(M):
    i,j = map(int,input().split())
    sol =  prefix[j]-prefix[i-1]
    print(sol)
    