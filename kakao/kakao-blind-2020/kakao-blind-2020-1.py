# kakao-blind-2020-1.py
# 
def solution(s):
    answer = float('inf')
    N = len(s)
    
    for slice in range(1,N+1):
        tmp = ''
        
        before = s[:slice]
        count = 1

        for start in range(slice,N,slice):
            # if start+slice > N :now = s[start:N]
            # else: now = s[start:start+slice]
            now = s[start:start+slice]              
            if now == before:
                count+=1
            else:
                if count>1 :
                    tmp+= str(count) + before
                elif count == 1:
                    tmp += before
                before = now
                count = 1    
        
        if count>1:
            tmp+=str(count)+ before
        else:
            tmp+=before
        
        answer = min(answer, len(tmp) )

    print(answer)
    return answer

solution('a')
# solution("abcab")