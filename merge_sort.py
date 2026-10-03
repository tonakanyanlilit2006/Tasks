a=[4,7,21,33,5,28,45]

def marge_sort(a):
    if len(a)<=1:
        return a
    mid =len(a) //2
    left =marge_sort(a[:mid])
    right =marge_sort(a[mid:])
    return merge(left,right)
def merge(left,right):
    out, i, j=[],0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            out.append(left[i])
            i+=1
        else:
            out.append(right[j])
            j+=1
    out+=left[i:]
    out+=right[j:]
    return out
print(marge_sort(a))
    