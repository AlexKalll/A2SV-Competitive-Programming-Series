# https://codeforces.com/gym/576550/problem/B

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans = 0
i = 0
while m > 0 and i < n:
    if a[i] < 0:
        ans += abs(a[i])
        m -= 1
        i += 1
    else:
        break

print(ans)