# https://codeforces.com/gym/576550/problem/A

t = int(input())
for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    l = 0
    r = n-1
    ans = []

    while l < r:
            ans.append(b[l])
            ans.append(b[r])
            l += 1
            r -= 1

    if n % 2 == 1:
        ans.append(b[l])  # or ans.append(b[n//2 + 1]) or ans.append(b[r])

    print(*ans)