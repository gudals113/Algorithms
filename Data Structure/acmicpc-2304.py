#백준 2304번 창고 다각형 (stack)
N= int(input())
column = []
for _ in range(N):
    arr= list(map(int, input().split()))
    column.append(arr)
column.sort()

latest = -1
ans = 0

for i in range(N):
    cur_height = column[i][1]
    
    if latest==-1:
        latest = i

    if column[latest][1] < cur_height:
        

        temp = (column[i][0] - column[latest][0]) * (column[latest][1])
        ans += temp

        latest = i

# i love you



latest = -1
for i in range(N-1, -1, -1):

    cur_height = column[i][1]
    
    if latest==-1:
        latest = i

    if column[latest][1] < cur_height:
        

        temp = ( column[latest][0] - column[i][0]  ) * (column[latest][1])
        ans += temp

        latest = i

print(ans)
