def peak(A, N):
    i = 0
    j = N-1

    while True:
        m = int((i+j)/2)
        if m > i and A[m-1] > A[m]:
            j = m-1
        elif m < j and A[m+1] > A[m]:
            i = m + 1
        else:
            return m

N = int(input())
A = [int(x) for x in input().split(" ")]

print(peak(A, N))
    
