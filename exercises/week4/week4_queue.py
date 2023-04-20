def Queue():
    n = int(input())
    op = []
    stack = []
    for i in range(n):
        op.append(input())    
    for i in op:
        if i == 'D':
            print(stack.pop(0))           
        else:   
            stack.append(int(i.replace('E ','')))
Queue()