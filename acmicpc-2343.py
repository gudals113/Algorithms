#백준 2343번 기타 레슨 (binary search)
N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)
answer = end
while end >= start:
    mid = (start+end)//2

    count = M
    long = 0

    for lesson in arr:

        long += lesson

        if long > mid:
            long = lesson
            count -= 1

    # print(start, end, mid, count)
    if count > 0:
        end = mid - 1
        
    else:
        start = mid + 1

print(start)

