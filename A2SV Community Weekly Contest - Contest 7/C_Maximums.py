# https://codeforces.com/gym/576550/problem/C

n = int(input())
b = list(map(int, input().split()))

a = [b[0]]
max_ = b[0]
for i in range(1, n):
    max_ = max(max_, a[i-1])
    a.append(b[i] + max_)

print(*a)
