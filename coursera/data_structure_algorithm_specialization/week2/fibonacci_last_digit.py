# Uses python2
def get_fibonacci_last_digit_fast(n):
    a=[]
    a.append(0)
    a.append(1)
    if n==0:
        return(a[n])
    if n==1:
        return(a[n])
    for i in range(n-1):
        a.append((a[i]+a[i+1])%10)
    return(a[n])
    

n = int(raw_input())
print(get_fibonacci_last_digit_fast(n))
