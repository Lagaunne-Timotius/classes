# Uses python2
## Pisano period
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



n,m=map(int,raw_input().split())
print(get_fibonacci_huge_fast(n, m))
