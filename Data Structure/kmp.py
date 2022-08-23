# kmp.py

# kmp? understand
# 패턴을 옮길 때마다, 앞에서부터 일치하는 부분까지 차례로 찾아 나간다( 이것도 최적화 가능할 듯)
# 만약 7개 일치하면 pi[7-1]를 참고한다. pi[6]=3, 접두사3개 접미사 3개 같다 -> '일치한' pat 길이 - 3 만큼 이동. = 7-3 = 4
# 그럼 이미 3개는 일치한 상황이다.
# S : i->i+4, pat: j-> 3(3개이미 일치하므로 다음 idx부터 비교) 
S ='aba cab aac abacabbc'
pat ='aba cab aac'

pi = [0,0,1,0,1,2,3,1,0] #이거 구하는 방법도 최적화 가능

# 예제 https://www.acmicpc.net/problem/1701
# pi?
# 처음부터 시작해야지(접두사)
# i=0,j=1 -> if pat[i]==pat[j] : i+=1, j+=1, pi[j]=1
# i=1, j=2 -> if pat[i]==pat[j] : i+=1, j+=1, pi[j] = pi[j-1]+1 = 2
# i=2, j=3 - > if pat[i]!=pat[j] : 


pl = len(pat)
sl = len(S)

#
def failure(W):
    
    j=0
    i=1
    while True:
        if W[i]!=W[j]:
            i
        
        
        
    
failure('abaab')