# # boj-7453.py 합이 0인 네 정수
# # 시험 끝나고 다시 풀어보기
# #defaultdict 사용하지 않기

#meet in the middel
import sys
input = sys.stdin.readline
N = int(input())
A,B,C,D = [],[],[],[]
for i in range(N):
    a,b,c,d= map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
    
ABDict = {}
answer = 0
CDDIct = {}

for i in range(N):
    for j in range(N):
        tmpAB = A[i]+B[j]
        if tmpAB in ABDict:
            ABDict[tmpAB] +=1
        else:
            ABDict[tmpAB]=1
            
for i in range(N):
    for j in range(N):
        tmpCD = (C[i]+D[j])*-1
        if tmpCD in ABDict:
            answer += ABDict[tmpCD]
        

print(answer)