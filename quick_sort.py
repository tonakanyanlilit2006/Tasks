a = [4, 7, 33, 5, 21, 28, 45,37,67,16]
def quick_sort(a):

    if len(a) <= 1:
        return a

    m=[]
    left = []
    right = []
    p = a[len(a) // 2]
    for i in a:

        if i < p:
            left.append(i)
        elif i==p:
            m.append(i)
        else:
            right.append(i)
    return (quick_sort(left) + m + quick_sort(right))
print(quick_sort(a))