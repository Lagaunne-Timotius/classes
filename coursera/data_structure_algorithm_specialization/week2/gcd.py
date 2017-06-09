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

a,b=map(int,raw_input().split())
print(gcd_fast(a, b))