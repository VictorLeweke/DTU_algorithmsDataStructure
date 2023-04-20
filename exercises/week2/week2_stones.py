#Read input
N,W = map(int, input().split())
w = list(map(int, input().split()))

def stones(N,W,w):    
  
    #Sort the weights of the stones
    w_sort = sorted(w)
    
    #Accumulating weight of the stones
    T = 0
    
    for i in range(N):
        
        #Can we pick up the  next stone
        if T+w_sort[i] > W:
            return i
        else:
            T+=w_sort[i]
    
    return N

print(stones(N,W,w))
