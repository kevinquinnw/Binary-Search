import random 

pos = -1 

def find(list, n):
    l = 0
    u = len(list) - 1 

    while l <= u: 
        mid = (l + u) // 2 

        if list[mid] == n:
            globals()['pos'] = mid
            return True 
        else:
            if list[mid] < n: 
                l = mid + 1 
            else:
                u = mid - 1
    
    return False

list = list(range(1, 101))
random.shuffle(list)

n = 56

if find(list, n):
    print("Found at ", pos + 1)
else: 
    print("Not Found")