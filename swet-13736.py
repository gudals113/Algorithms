T = int(input())
for test_case in range(1, T + 1):
    A,B,K = map(int,input().split())

    for i in range(K) : 
        if A==0 or B== 0 :
            break
        
        elif A <= B :
            B = B-A
            A = 2*A
            
        else:
            A = A-B
            B = 2*B
        
        # print(A,B)
    sol = min(A,B)
    print(sol)
            
        

    