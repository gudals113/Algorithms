# 최대 연속 부분수열의 합

# 1. O(N log N)
def divide_conquer(arr):
    N = len(arr)

    def find(lo, hi):
        # 1.
        if lo == hi:
            return arr[lo]

        mid = (lo + hi) // 2
	# 2.
        left = find(lo, mid)
        right = find(mid+1, hi)

        # 3.
        tmp = 0
        left_part = MIN
        for i in range(mid, lo-1, -1):
            tmp += arr[i]
            left_part = max(left_part, tmp)

        tmp = 0
        right_part = MIN
        for i in range(mid+1, hi+1):
            tmp += arr[i]
            right_part = max(right_part, tmp)

        # 4.
        return max(left, right, left_part + right_part)

    # 5.
    return find(0, N-1)