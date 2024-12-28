# https://codeforces.com/gym/576550/problem/E

n = int(input())
strings = [input() for _ in range(n)]

strings.sort(key=len)

for i in range(1, n):
    if strings[i-1] not in strings[i]:
        print('NO')
        exit()

print('YES')
print(*strings, sep='\n')