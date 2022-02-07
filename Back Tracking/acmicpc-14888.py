# 연산자 끼워넣기
N= int(input())
nums = list( map(int, input().split()) )
opers = list(map(int, input().split()))#덧뺄곱나
# numsCheck=[0 for i in range(N)]
opersCheck=[op for op in (opers)]

# result_nums=[]
result_opers=[]

# tmp_nums=[]
tmp_opers=[]


# def numsDFS():
#     if len(result_nums) == N :
#         tmp_nums.append(result_nums[:])
#         return
    
#     for i in range(N):
#         if numsCheck[i]==0:
#             numsCheck[i]=1
#             result_nums.append(nums[i])
#             numsDFS()
#             numsCheck[i]=0
#             result_nums.pop()

# numsDFS()

def operDFS():
    if opersCheck == [0,0,0,0]:
        tmp_opers.append(result_opers[:])
        return
    
    for i in range(4):
        if opersCheck[i] !=0 :
            result_opers.append(i)
            opersCheck[i] -=1
            operDFS()
            result_opers.pop()
            opersCheck[i] +=1

operDFS()

ans1, ans2 = -float("INF"), float("INF")
for j in range(len(tmp_opers)):
    
    oper_list = tmp_opers[j]
    num_list = [i for i in nums]
 
    tmp = num_list[0]
    for i in range(len(oper_list)):
        if oper_list[i] == 0:
            tmp= tmp+ num_list[i+1]
        
        elif oper_list[i]==1:
            tmp= tmp-num_list[i+1]
        
        elif oper_list[i]==2:
            tmp = tmp * num_list[i+1]
            
        elif oper_list[i]==3:
            if tmp <0 or num_list[i+1]<0:
                tmp = abs(tmp) // abs(num_list[i+1])
                tmp = tmp *-1
            else:
                tmp = tmp // num_list[i+1]
            
    ans1 = max(ans1, tmp)
    ans2 = min(ans2, tmp)
    
print(ans1)
print(ans2)