# Uses python2

def get_pisano_period(n, m):
    periodic=[0,1]
    i=0
    j=1
    while(periodic[i]!=1 or periodic[j]!=0):
        periodic.append((periodic[i]+periodic[j])%m)
        i=i+1
        j=j+1
    
    return(periodic)

    
def get_fibonacci_huge_fast(n, m):
    periodic=get_pisano_period(n, m)
    #print(periodic)
    return(periodic[n%(len(periodic)-1)])


def fibonacci_sum_fast(n):   
    x=get_fibonacci_huge_fast(n+2, 10)
    return((x-1)%10)
    

n = int(raw_input())
print(fibonacci_sum_fast(n))
