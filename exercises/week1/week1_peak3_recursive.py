def peak(A, i, j):
    m = int((i+j)/2)
    if m > i and A[m-1] > A[m]:
        return peak(A, i, m-1)
    elif m < j and A[m+1] > A[m]:
        return peak(A, m+1, j)
    else:
        return m

N = int(input())
A = [int(x) for x in input().split(" ")]

print(peak(A, 0, N-1))
    