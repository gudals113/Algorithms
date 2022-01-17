#숫자 카드, 이분탐색

N = int(input())
card = list(map(int, input().split()))
M = int(input())
question = list(map(int, input().split()))
answer = [0 for _ in range(M)]
card = sorted(card)

for i in range(M):
    
    q=question[i]
    s, t = 0, N-1
    while True:
        m=(s+t)//2
        c=card[m]
        
        if s>=t and c!=q:
            break
        
        if c==q:
            answer[i]=1
            break
        elif c>q:
            s, t = s, m-1
            
        elif c<q:
            s, t = m+1, t
for i in range(M):
    print(answer[i], end=' ')