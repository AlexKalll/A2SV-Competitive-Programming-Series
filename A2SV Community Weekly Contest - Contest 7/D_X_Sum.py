# https://codeforces.com/gym/576550/problem/D

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    max_ = 0
    
    for row in range(n):
        for col in range(m):
            cur_ = 0
            
            i, j = row, col
            while i >= 0 and i < n and j >= 0 and j < m:
                cur_ += a[i][j]
                i -= 1
                j -= 1
            
            i, j = row, col
            while i >= 0 and i < n and j >= 0 and j < m:
                cur_ += a[i][j]
                i += 1
                j -= 1
            
            i, j = row, col
            while i >= 0 and i < n and j >= 0 and j < m:
                cur_ += a[i][j]
                i -= 1
                j += 1
            
            i, j = row, col
            while i >= 0 and i < n and j >= 0 and j < m:
                cur_ += a[i][j]
                i += 1
                j += 1
            
            cur_ -= a[row][col] * 3 
            max_ = max(max_, cur_)
    
    print(max_)
