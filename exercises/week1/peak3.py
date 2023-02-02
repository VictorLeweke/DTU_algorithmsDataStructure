# Input
# Line 1: The number N of integers in the array (1 < N).
# Line 2: The integers in the array separated by a space.

#Output 
# Line 1: The index (0-indexed) of the found peakpoint in the array.

import math

n = int(input())
A = list(map(int, input().split()))
i, j = [0,n-1]

def peak3(A,i,j):
    m = math.ceil((i+j)/2)
    if i==j:
        return j
    if j-i==1:
        return min([i,j])
    elif A[m] >= A[m-1] and A[m] >= A[m+1]:
        return m
    elif A[m-1] > A[m]:
        return peak3(A,i,m-1) 
    elif A[m] < A[m+1]:
        return peak3(A,m+1,j)



print(peak3(A,i,j))
"""
m 8

peak3(A,9,15)
m 12"""