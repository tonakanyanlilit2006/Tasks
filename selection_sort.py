a=[7,111,72,1,3,15,169]
def selection_sort(a):
    for i in range(len(a)-1):
        min_index=i
        for j in range(i+1,len(a)):
            if a[j]<a[min_index]:
                min_index=j 
        a[i],a[min_index]=a[min_index],a[i]
    return a
print(selection_sort(a))