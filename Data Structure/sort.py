L = [1,2,3,4,5,6,7,8,9,10]
N = len(L)

# 선택 정렬 
def selection_sort(L):
    for i in range(N):  #해당 위치 i에 들어갈 원소를 선택
        minVal_idx = i      
        for j in range(i+1,N):
            if L[j] < L[minVal_idx] :
                minVal_idx = j
        
        L[i], L[minVal_idx] = L[minVal_idx], L[i]

# 삽입 정렬
def insertion_sort(L):
    for i in range(1,N):
        val = L[i]
        leftVal_idx = i-1

        while leftVal_idx >=0 and L[leftVal_idx] > val :
            L[leftVal_idx+1] = L[leftVal_idx] 
            leftVal_idx-=1
        
        L[leftVal_idx+1] = val

#거품 정렬
def bubble_sort(L):
    end = N-1
    
    while end>0:
        # isSwapped=False
        lastSwapped=0
        for i in range(end):
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                lastSwapped = i    
        # if not isSwapped : break
        end = lastSwapped
        
# 퀵 정렬
# def quick_sort(L):
#     if len(L) <= 1:
#         return L
    
#     pivot = L[len(L)//2]
#     lessList , eqaulList, greatList = [], [], []
#     for num in L :
#         if num < pivot :
#             lessList.append(num)
            
#         elif num > pivot :
#             greatList.append(num)
            
#         else:
#             eqaulList.append(num)
            
#     return quick_sort(lessList) + eqaulList + quick_sort(greatList)

# L = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(L,s,e):
    if s >= e :
        return
    
    pivot = s
    l,r = s+1, e
    print(L)
    while l<=r :
        #pivot 보다 큰 값을 왼쪽에서부터 찾는다.
        while l<=e and L[l] <= L[pivot] :
            l+=1
            
        #pivot 보다 작은 값을 오른쪽에서부터 찾는다.
        while r>=s+1 and L[r] >= L[pivot] :
            r-=1
    
        print(pivot, l,r)
        
        #l,r 이 엇갈린 경우 피벗 이동, l위치에 pivot
        if l>r :
            L[r] , L[pivot] = L[pivot], L[r] 
        else:
            L[l] , L[r] = L[r], L[l]
        
    quick_sort(L, s, r-1)
    quick_sort(L, r+1, e)https://www.daleseo.com/sort-merge/

quick_sort([0,1,2,3,4,5,6,7],0,7)

def merge_sort(L):
    def sort(l, r):
        if r-l<2 :
            return
        m = (l+r)//2
        sort(l,m)
        sort(m+1,r)
        merge(l,m,r)

    def merge(left,mid,right):
        tmp = []
        l, r = left, mid
        
        while l < mid and r < right :
            if L[l] < L[r]:
                tmp.append(L[l])
                l+=1
                
            else:
                tmp.append(L[r])
                r+=1
                
        #l, r 배열 중 아직 병합 안된 것들 처리
        while l < mid :
            tmp.append(L[l])
            l+=1
        while r < right:
            tmp.append(L[r])
            r+=1
            
        for i in range(left, right):
            L[i] = tmp[i-left]

    return sort(0, len(L))


