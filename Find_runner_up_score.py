if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for s in arr:
        if s != max(arr):
         print(s)
         break
   
