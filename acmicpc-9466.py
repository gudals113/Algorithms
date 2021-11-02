#백준 9466 텀 프로젝트 (DFS)

import sys
def input():
    return sys.stdin.readline()

T=int(input())
for _ in range(T):
    ans=0
    N= int(input())
    students=[-1]+list(map(int, input().split()))
    visit=[-1 for _ in range(N+1)]
    
    for i in range(1,N+1):
        current=i
        stack=[]
        if visit[i]<0:

            while True: 
                next = students[current]
                visit[current]=i

                if next==current:
                    visit[next]=i
                    ans+=1
                    break

                if next == i :
                    visit[next]=i
                    ans+=(len(stack)+1)
                    break

                if visit[next]==i:
                    popped=-1
                    while True:
                        popped = stack.pop()
                        ans+=1
                        if popped==next:
                            ans+=1
                            break
                    break
                
                if visit[next]>0:
                    break

                # print(i, current,ans)
                stack.append(current)
                current=next
            # print(i, current, ans, "here")
    print(N-ans)