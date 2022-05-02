def solution(board, moves):
    answer = 0
    stack=[]
    N = len(board)
    
    for move in moves:
        for i in range(N):
            if board[i][move-1] != 0 :
                doll = board[i][move-1]
                board[i][move-1]=0
                
                if len(stack)==0 or stack[-1]!=doll:
                    stack.append(doll)
                
                elif stack[-1]== doll:
                    stack.pop()
                    answer+=2
                    
                break
                

    return answer

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	,[1,5,3,5,1,2,1,4])