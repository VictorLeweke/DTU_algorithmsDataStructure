# Input
# Line 1: The number N of integers in the array (1 < N).
# Line 2: The integers in the array separated by a space.

#Output 
# Line 1: The index (0-indexed) of the found peakpoint in the array.

n = int(input())
A = list(map(int, input().split()))


def findMax(A,n):
    max = 0
    for i in range(0,n):
        if (A[i] > A[max]):
            max = i
    return max



print(findMax(A,n))