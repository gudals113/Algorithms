#스도쿠
sdoku = []
start = []
for i in range(9):
    line = list(map(int, input().split()))
    for j in range(9):
        if line[j]==0 :
            start.append([i,j])
    
    sdoku.append( line )

def DFS(idx):
    global ans
    if idx == len(start) :
        for i in range(9):
            print(' '.join(map(str, sdoku[i])))
        return 1
        
    x,y=start[idx]
    check_r,check_c,check_s = [0 for _ in range(10)],[0 for _ in range(10)],[0 for _ in range(10)]    
    
    section_x = (x//3) *3
    section_y = (y//3) *3
    
    #있는 거 부터 체크
    for i in range(9):
        row = sdoku[x][i]
        if row !=0:
            check_r[row] = 1
            
    for i in range(9):
        col = sdoku[i][y]
        if col !=0:
            check_c[col]=1
    
    for i in range(3):
        for j in range(3):
            sqr = sdoku[section_x+i][section_y+j]
            if sqr !=0 :
                check_s[sqr]=1
       
    
    
    for i in range(1,10):
      
        if check_r[i] ==0 and check_c[i]==0 and check_s[i]==0:
            sdoku[x][y]=i
            if DFS(idx+1) ==1:
                return 1
            sdoku[x][y]=0
    
        if i == 9:
            return 0
    
    return 0

DFS(0)

