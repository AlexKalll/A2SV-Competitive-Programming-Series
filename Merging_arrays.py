n, m = map(int, input().split())

first_array = list(map(int, input().split()))
second_array = list(map(int, input().split()))

third_array = []
first = 0
second = 0

for _ in range(n + m):
    if first < n and (second == m or first_array[first] <= second_array[second]):
        third_array.append(first_array[first])
        first += 1
    else:
        third_array.append(second_array[second])
        second += 1

final = ' '.join(map(str, third_array)) #
print(final)

#or simply i can use unpacking by using astrix *   as follows
# print(*third_array)  
