t = int(input())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    i, ans = 0, 0
    same_sign_max = 0
    while i < n:
        left = i
        right = i
        while right < n - 1 and (arr[right]*arr[right + 1]) > 0:
            right += 1
        same_sign_max = max(arr[left : right + 1])
        ans += same_sign_max
        i = right + 1
    print(ans)
