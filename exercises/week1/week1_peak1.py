def peak(A, N):
    for i in range(N):
        if (i==0 or A[i-1] <= A[i]) and (i==N-1 or A[i] >= A[i+1]):
            return i 

N = int(input())
A = [int(x) for x in input().split(" ")]

print(peak(A, N))
    
