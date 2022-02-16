#종이의 개수, 분할 정복
def cut_paper(corner_x,corner_y, length):
    corner = paper[corner_x][corner_y]
    
    if length == 1 :
        sol_dic[corner] += 1
        return
    
    for i in range(length):
        for j in range(length):
            x , y = corner_x + i , corner_y + j
            if corner != paper[x][y] :
                for l in range(3):
                    for k in range(3):
                        cut_paper(corner_x + l*length//3, corner_y + k*length//3 , length//3)
                return 
                
    sol_dic[corner] += 1
    return 

N=int(input())
paper = []
for i in range(N):
    line = list( map( int, input().split() ) )
    paper.append(line)
#paper[x][y] x : 세로, y : 가로

sol_dic = {0:0, -1:0, 1:0}
cut_paper(0,0,N)

for i in range(3):
    print(sol_dic[-1+i])
