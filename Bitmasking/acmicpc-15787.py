#기차가 어둠을 헤치고 은하수를 (구현, 비트마스킹)
N,M = map( int, input().split() )
visited = [0 for _ in range( 1 <<20 )]

train = [0 for _ in range(N)]
#train[N][000 0000 ]
for i in range(M):
    command= list( map(int, input().split()) )
    
    if command[0]==1:
        t = command[1]
        p = command[2]
        train[t-1] = train[t-1] | 1<<(p-1)
    
    elif command[0]==2:
        t = command[1]
        p = command[2]
        train[t-1] = train[t-1] & ~(1<<(p-1))
    
    elif command[0]==3:
        t = command[1]
        train[t-1] = train[t-1] & ~(1<<19)
        train[t-1] = train[t-1] << 1 
        
    elif command[0]==4:
        t = command[1]
        train[t-1] = train[t-1] >>1

sol=0
for i in range(N):
    bitmask = train[i-1]
    if visited[bitmask] == 0:
        sol+=1
        visited[bitmask] =1
print(sol)