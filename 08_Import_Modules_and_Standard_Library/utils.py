def find_index(arr,target):
    for i,value in enumerate(arr):
        if value == target:
            return i
    return -1

arr = [x for x in range(1,501)]