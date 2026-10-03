broken=int(input())
x=0
n=0
def y(x,n,broken):
    step=14
    while x<100 :
        x+=step
        n+=1
        step-=1
        if x>=broken:
           x-=step
           return(y2(x,n,broken))
def y2(x,n,broken):
    while x< broken:
        x+=1
        n+=1
    return n
print(y(x,n,broken))
                    
                    
                  
                


    
    
    

