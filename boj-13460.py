N, M = map(int, input().split())
G=[]
R, B=[], []
for i in range(N):
    line = input()
    for j in range(M):
        if line[j]=='B':
            B=[i,j]
            
        elif line[j]=='R':
            R = [i,j]
            
    G.append(line)



def DO_LEFT(r,b):
    global G
    rx, ry = r
    bx, by = b
    
    
    if ry > by :
        line = G[bx]
        targetBy=by
        for i in range(by, -1, -1):
            if line[i] == '#' or line[i]=='R' : #' R 일리는 없지만 표현 쉽게 하기 위해'
                break
            
            elif line[i]=='.' :
                targetBy = i
                
            elif line[i]=='0' :
                return False
            
        G[bx][by] = '.'
        G[bx][targetBy] = 'B'
        
        line = G[rx]
        targetRy=ry
        for i in range(ry, -1, -1):
            if line[i] == '#' or line[i]=='B': #'위에서와 다르게 B인 경우 존재한다'
                break
            
            elif line[i]=='.' :
                targetRy = i

            elif line[i]=='0' : 
                return True #성공한 경우!

        G[rx][ry] = '.'
        G[rx][targetRy] = 'R'
    
    