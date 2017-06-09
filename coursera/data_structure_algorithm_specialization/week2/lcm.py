# Uses python2

def gcd_fast(a, b):
    if b>a:
        temp=b
        b=a
        a=temp
    c=-1
    while(c!=0):
        c=a%b
        a=b
        b=c
    return(a)

def lcm_fast(a, b):
    return(a*b/gcd_fast(a,b))
a,b=map(int,raw_input().split())
print(lcm_fast(a, b))
