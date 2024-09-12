def bubble_sort(sez):
    n = len(sez)
    for i in range(n):
        swifted = False 
        for j in range(n-i-1):
            if sez[j] > sez[j+1]:
                sez[j], sez[j+1] = sez[j+1], sez[j]
                swifted = True
        if swifted == False:
            break
    return sez 

def selection_sort(sez):
    n = len(sez)
    for i in range(n-1):
        min_idx = i 
        for j in range(i+1,n-1):
            if sez[j] < sez[min_idx]:
                min_idx = j 
        sez[min_idx], sez[i] = sez[i], sez[min_idx]
    return sez

def quick_sort(sez):
    if len(sez) <= 1:
        return sez 
    pivot = sez[0]
    left = [x for x in sez if x < pivot]
    middle = [x for x in sez if x == pivot]
    right = [x for x in sez if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

seznam = [20,-2,5,10,30,100,5,9,10]

print(bubble_sort(seznam))
print(selection_sort(seznam))
print(quick_sort(seznam))