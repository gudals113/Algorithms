R=[0]+list(map(int, input().split()))
B=[0]+list(map(int, input().split()))
k,N=map(int, input().split())

reddp=[[0 for _ in range(k+1)] for _ in range(N+1)] 
bluedp=[[0 for _ in range(k+1)] for _ in range(N+1)] 

reddp[1][0]=R[1]
bluedp[1][0]=B[1]

for i in range(2, N+1):
    for j in range(k+1):

        if j>=i:
            reddp[i][j]=-10000
            bluedp[i][j]=-10000 
        
        else:

            if j==0:
                reddp[i][j]=reddp[i-1][j]+ R[i]
                bluedp[i][j]=bluedp[i-1][j]+ B[i]

            else:
                reddp[i][j]=max(bluedp[i-1][j-1], reddp[i-1][j]) + R[i]
                bluedp[i][j]=max(reddp[i-1][j-1], bluedp[i-1][j]) + B[i]

print(reddp, '여깅?',bluedp)
# def round(i,k,color):
#     if color==0:

#         if i>1:
#             if k>=1:
#                 sol = max(round(i-1, k-1, 1), round(i-1, k, 0)) + R[i-1] 
#                 reddp
            
#         elif i==1 :
#             return R[0]
