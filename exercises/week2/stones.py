def MergeSort(l,start,end):
    if start < end:
        m = int((start+end) / 2)
        MergeSort(l, start, m)
        MergeSort(l, m+1, end)
        Merge(l, start, m, end)
    return l
        
def Merge(l, start, m, r):
    n1 = m - start + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = l[start + i]
 
    for j in range(0, n2):
        R[j] = l[m + 1 + j]
 
    # Merge the temp arrays back into l[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = start     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            l[k] = L[i]
            i += 1
        else:
            l[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        l[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        l[k] = R[j]
        j += 1
        k += 1

def Stones():
    n,w = map(int, input().split())
    l = list(map(int, input().split()))
    if sum(l)<=w:
        return n
    else:
        l = MergeSort(l,0,n-1)
        s=0
        nb=0
        while l and (s+l[nb])<=w:
            s+=l[nb]
            nb+=1        
        return nb


print(Stones())