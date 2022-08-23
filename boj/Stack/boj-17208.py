# boj-17208.py
# 오큰수
# stack
# 220725 sol
N = int(input())
L = list( map(int, input().split()))
stack = []
answer = [-1 for _ in range(N)]
for i in range(N):
    num = L[i]
    
    while True:
        if len(stack)==0 or L[stack[-1]] >=num :
            break
        idx = stack.pop()
        answer[idx] = L[i]
            
    stack.append(i)

print(*answer)