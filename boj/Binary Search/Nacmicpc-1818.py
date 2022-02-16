# 책정리 ( binary serach, LIS)
# lower_bound
# LIS 이분 탐색
N = int(input())

books = list(map(int, input().split()))
dp=[]


def binary_search(s,e, book) :
    while s<e:
        mid = (s+e)//2
        
        if dp[mid] < book :
            s = mid +1
            
        else:
            e = mid 
    dp[e]=book
    

for book in books :
    if len(dp)==0 or dp[-1] < book :
        dp.append(book)
    else:
        binary_search(0, len(dp)-1, book)
    
print(N-len(dp))


# books = [2, 1, 4, 5, 3]
# dp = []

# book=2 :  dp = [2]
# book=1 :  dp = [1]
# book=4 :  dp = [1, 4]
# book=5 :  dp = [1,4,5]
# book=3 :  dp = [1,3,5]

