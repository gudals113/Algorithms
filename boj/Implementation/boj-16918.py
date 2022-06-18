#봄버맨 구현 sol 220603
R,C,N = map(int,input().split())
G=[['.' for _ in range(C)]for _ in range(R)]
for i in range(R):
    line = input()
    for j in range(C):
        if line[j]=='O':
            
            G[i][j] = '0'
        else:
            G[i][j] = '.'
        
        
for time in range(2,N+1):
    if time%2==0 :
        for x in range(R):
            for y in range(C):
                if G[x][y]=='.':
                    G[x][y] = str(time)
                    
    else:
        for x in range(R):
            for y in range(C):
                if G[x][y] == str(time-3):
                    G[x][y]='.'
                    for nx ,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
                        if 0<=nx<R and 0<=ny<C and G[nx][ny]!=str(time-3):
                            G[nx][ny] = '.'

# print('answer')
for i in range(R):
    tmp = ''
    for j in range(C):
        if G[i][j] == '.':
            tmp+='.'
        
        else:
            tmp+='O'
            
    print(tmp)
    

    