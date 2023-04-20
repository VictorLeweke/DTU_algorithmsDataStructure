def MaximalSubarray():
    n = int(input())
    l = list(map(int, input().split()))
    max_sum = l[0]
    current_sum = 0
    for i in l: 
        current_sum = current_sum + i
        if current_sum <= i:
            current_sum = i
        if max_sum < current_sum:
            max_sum = current_sum
    print(max_sum)
MaximalSubarray()