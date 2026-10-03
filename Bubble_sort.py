a=[43,6,38,9,1,15,3,4,22]
def bubble(a):
    for i in range(len(a)):
        for j in range (len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
print(bubble(a))