#쿼드트리, 분할정복
N = int(input())
video = [[0 for _ in range(N)] for _ in range(N)]
sol=[]

for i in range(N):
    line = input()
    for j in range(N):
        video[i][j] = int (line[j])

def cut_video(x_corner,y_corner,length) :
    corner = video[x_corner][y_corner]
    if length==1:
        return corner
    
    for i in range(length):
        for j in range(length):
            if video[x_corner + i ][y_corner + j ] != corner :
                lt=cut_video(x_corner,y_corner, length//2)
                rt=cut_video(x_corner, y_corner+length//2, length//2)
                lb=cut_video(x_corner+length//2, y_corner, length//2)
                rb=cut_video(x_corner+length//2, y_corner+length//2, length//2)
    
                corner = [lt,rt,lb,rb]
                return corner        
    return corner
    
def get_print(result):
    global sol
    
    if type(result) == list:
        sol.append('(')
        for i in range(4):
            get_print(result[i])    
        sol.append(')')
        
    else:
        sol.append(str(result))
        

     
SOL_LIST = cut_video(0,0,N)
get_print(SOL_LIST)
# print(SOL_LIST)
# print(sol)
print(''.join(sol))