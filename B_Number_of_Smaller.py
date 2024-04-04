n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = []
l = 0

for i in range(len(arr2)):
    while l < len(arr1) and arr1[l] < arr2[i]:
        l += 1
    ans.append(l)

print(*ans)
    
# res = ' '.join(map(str, ans))
# print(res)      #This is because the join method is only used in the string 