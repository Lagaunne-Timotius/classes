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


def fibonacci_partial_sum_fast(f, t): 
    x=get_fibonacci_huge_fast(t+2, 10)
    y=get_fibonacci_huge_fast(f+1, 10)
    return((x-y)%10)
    

x, y = map(int, raw_input().split())
print(fibonacci_partial_sum_fast(x, y))