def swap(parent_idx, child_idx, heap, satellite):
    if 0 < parent_idx < child_idx < len(heap):
        if heap[parent_idx] < heap[child_idx]:
            temp = heap[parent_idx]
            heap[parent_idx] = heap[child_idx]
            heap[child_idx] = temp

            temp = satellite[parent_idx]
            satellite[parent_idx] = satellite[child_idx]
            satellite[child_idx] = temp

            return True
    return False

def bubble_up(idx, heap, satellite):
    parent_idx = idx//2
    if swap(parent_idx, idx, heap, satellite):
        bubble_up(parent_idx, heap, satellite)

def bubble_down(idx, heap, satellite):
    # This is what I did in the lecture:
    
    # child_idx = idx*2
    # if len(heap) > child_idx + 1:
    #     child_idx = child_idx + int(heap[child_idx] < heap[child_idx + 1])

    # This is a more intuitive way to do it:
    
    # if both children exist, choose the larger one
    if len(heap) > idx*2 + 1 and heap[idx*2] < heap[idx*2 + 1]:
        # line 30 works because "heap[idx*2] < heap[idx*2 + 1]" is only executed if
        # "len(heap) > idx*2 + 1" is true, i.e. if both children exist.
        # This is because of the "and": if the first condition is false, then
        # the second condition is not evaluated, as it is not necessary.
        child_idx = idx*2 + 1
    
    # if only the left child exists, choose that
    else:
        child_idx = idx*2

    if swap(idx, child_idx, heap, satellite):
        bubble_down(child_idx, heap, satellite)

def extract_max(heap, satellite):
    if len(heap) == 1:
        return None
    if len(heap) == 2:
        return heap.pop(), satellite.pop()
    else:
        key = heap[1]
        sat = satellite[1]
        heap[1] = heap.pop()
        satellite[1] = satellite.pop()
        bubble_down(1, heap, satellite)
        return key, sat

def insert(key, sat, heap, satellite):
    heap.append(key)
    satellite.append(sat)
    bubble_up(len(heap)-1, heap, satellite)

N = int(input())

heap_array = [None]
sat_array = [None]

for i in range(N):
    command = input().split(" ")
    if command[0] == "I":
        key = int(command[1])
        sat = int(command[1])
        insert(key, sat, heap_array, sat_array)
    elif command[0] == "E":
        heap, sat = extract_max(heap_array, sat_array)
        print(sat)
    elif command[0] == "P":
        for i in sat_array[1:]:
            if i == len(heap_array):
                print(i)
            else:
                print(i, end=" ")