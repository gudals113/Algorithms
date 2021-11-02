#백준 2110번 공유기 설치 (binary search)
N, M = map(int, input().split())
arr=[]
for _ in range(N):
    arr.append(int(input()))
arr=sorted(arr)

start = 1
end = arr[-1]-arr[0]


while end>=start :
    count = 1
    mid = (start+end)//2

    current = arr[0]
    for i in range(1,N):

        if arr[i] - current >= mid :
            current = arr[i]
            count += 1

    # print(start, end)
    if count >= M :
        answer = mid
        start = mid +1

    else :
        end = mid - 1

print(answer)