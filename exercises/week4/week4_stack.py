def Stack():
    n = int(input())
    op = []
    stack = []
    for i in range(n):
        op.append(input())    
    for i in op:
        if i == 'PO':
            print(stack.pop())           
        else:   
            stack.append(int(i.replace('PU ','')))
Stack()