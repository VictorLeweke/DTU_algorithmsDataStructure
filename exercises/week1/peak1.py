# Input
# Line 1: The number N of integers in the array (1 < N).
# Line 2: The integers in the array separated by a space.

#Output 
# Line 1: The index (0-indexed) of the found peakpoint in the array.

n = int(input())
A = list(map(int, input().split()))


def peak1(A,n):
    if A[0] >= A[1]:
        return 0 
    for i in range(1,n-2):
        if A[i-1] <= A[i] and A[i] >= A[i+1]:
            return i
    if A[n-2] <= A[n-1]:
        return n-1

print(peak1(A,n))

