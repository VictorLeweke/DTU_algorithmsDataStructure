def ChristmasPresents():
    A, L, O = map(int, input().split())
    found = False
    
    if A < L and A < O:
        print("Anna")
        found = True
    	
    if L < A:
        print("Laura")
        found = True
    
    if O < A or O < L:
        print("Oscar")
        found = True
    
    if not found:
    	print("NONE")

ChristmasPresents()
