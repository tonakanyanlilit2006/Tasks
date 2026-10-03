a = [4, 7, 33, 5, 21, 28, 45,37,67,16]
def quick_sort(a):

    if len(a) <= 1:
        return a

    p = a[len(a) // 2]

    left = []
    right = []

    for x in a[:-1]:

        if x <= p:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [p] + quick_sort(right)
print(quick_sort(a))