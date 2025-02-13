def prime(x):
    a=[i for i in range(1,x+1) if x%i==0]
    if len(a)>2:
        return 'Not Prime'
    else:
        return 'Prime'