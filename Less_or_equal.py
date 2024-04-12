def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    nums.sort()
    
    if k == 0:
        ans = nums[0] - 1
    else:
        ans = nums[k - 1]
    
    count = 0
    for i in range(n):
        if nums[i] <= ans:
            count += 1
    if count != k or not (1 <= ans <= 1000000000):
        print("-1")
        return
    else:
        print(ans)
        return

if __name__ == "__main__":
    main()
