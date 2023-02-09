import math

n = int(input())
A = list(map(int, input().split()))
M = []

# convert the array A into a matrix
for i in range(n): 
    row=[] 
    for j in range(n):
        row.append(A[i*n+j]) 
    M.append(row)

# function to check if neighbors are not out of bounds
def inrange(index, size):
    if 0 < index < size-1:
        return True
    else:
        return False

def peak2D1(M,n):
    for i in range(n):
        for j in range(n):

            # Check if index is in the "middle" of the 
            if inrange(i,n) and inrange(j,n):
                if M[i][j] >= M[i-1][j] and M[i][j] >= M[i][j-1] and M[i][j] >= M[i+1][j] and M[i][j] >= M[i][j+1]:
                    return [i,j]

            # check for top and bottom edges
            if inrange(i,n) and not inrange(j,n):
                if j == 0:
                    if M[i][j] >= M[i-1][j] and M[i][j] >= M[i+1][j] and M[i][j] >= M[i][j+1]:
                        return [i,j]
                else:
                    if M[i][j] >= M[i-1][j] and M[i][j] >= M[i][j-1] and M[i][j] >= M[i+1][j]:
                        return [i,j]

            # check for left and right edges
            if not inrange(i,n) and inrange(j,n):
                if i == 0:
                    if M[i][j] >= M[i][j-1] and M[i][j] >= M[i+1][j] and M[i][j] >= M[i][j+1]:
                        return [i,j]
                else:
                    if M[i][j] >= M[i-1][j] and M[i][j] >= M[i][j-1] and M[i][j] >= M[i][j+1]:
                        return [i,j]

            # check for all 4 corners
            if not inrange(i,n) and not inrange(j,n):
                if [i,j] == [0,0]:
                    if M[i][j] >= M[i+1][j] and M[i][j] >= M[i][j+1]:
                        return [i,j]
                elif [i,j] == [n-1,0]:
                    if M[i][j] >= M[i-1][j] and M[i][j] >= M[i][j+1]:
                        return [i,j]
                elif [i,j] == [0,n-1]:
                    if M[i][j] >= M[i+1][j] and M[i][j] >= M[i][j-1]:
                        return [i,j]
                else:
                    if M[i][j] >= M[i-1][j] and M[i][j] >= M[i][j-1]:
                        return [i,j]

print(M)
print(peak2D1(M,n))