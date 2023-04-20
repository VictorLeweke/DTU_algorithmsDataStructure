def peak(A, N):
    current_max = 0
    for i in range(N):
        if A[i] > A[current_max]:
            current_max = i
    return current_max

N = int(input())
A = [int(x) for x in input().split(" ")]

print(peak(A, N))