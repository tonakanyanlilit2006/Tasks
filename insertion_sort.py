# Tasks
def ins_sort(x):
    for i in range (1,len (x)):
        key=x[i]
        j=i-1
        while j>=0 and x[j]>key:
            x[j+1]=x[j]
            j-=1
        x[j+1]=key
    return x

x=[7,11,2,5,9]

print(ins_sort(x))