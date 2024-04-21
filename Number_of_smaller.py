n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

ans = []
no_smalls = 0

for i in range(len(arr2)):
    while no_smalls < len(arr1) and arr1[no_smalls] < arr2[i]:
        no_smalls += 1
    ans.append(no_smalls)

print(*ans)
