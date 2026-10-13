
a = [7,23,8,9,0,11,173,1001,2,1]
def heap(a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    
    if left < n and a[left] > a[i]:
        largest = left

    if right < n and a[right] > a[largest]:
        largest = right

    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        heap(a, n, largest)
        
def heap_sort(a):
    n = len(a)
    for i in range(n // 2 - 1, -1,-1):
        heap(a, n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heap(a, i, 0)
    return a
print(heap_sort(a))