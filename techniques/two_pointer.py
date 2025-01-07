
# Two Pointer Technique

def twoPointer(arr):
    if len(arr) == 0:
        return 0
    
    writePointer = 1
    
    for readPointer in range(1, len(arr)):
        if arr[readPointer] != arr[readPointer - 1]:
            arr[writePointer] = arr[readPointer]
            writePointer += 1
    
    return writePointer
        
        
twoPointer([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
        
# python techniques/two_pointer.py
    
    