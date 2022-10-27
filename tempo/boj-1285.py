#동전 뒤집기
from collections import deque

# hint 220916
# 1행 -> 2열 -> 1행  = 2열
# 즉, 다시 뒤집은 경우는 생각 안해도 되는구나.


N = int(input())
s = ''
for _ in range(N):
    l = input()
    for i in range(N):
        s+=l[i]
answer = s.count('T')
def change(s, cnt, type, line):    
    s = list(s)
    if type == 0:
        start = line*N
        for i in range(start, start+N):
            if s[i]=='T' : 
                s[i]='H'
                cnt-=1
            else : 
                s[i]= 'T'
                cnt+=1
    else:
        start = line
        for i in range(start,N**2,N):
            if s[i]=='T' : 
                s[i]='H'
                cnt-=1
            else: 
                s[i]='T'     
                cnt+=1
               
    return ''.join(s), cnt







