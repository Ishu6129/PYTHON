n=int(input())
s="1"
if n==1:
    print("1")
elif n>1:
    print("1")
    for j in range(n-1):
        c=""
        a=len(s)
        while 0<a:
            t=0
            p=s[0]
            for i in range(len(s)):
                if s[i]==s[0]:
                    t=t+1
                    m=i
                    a=a-1
                else:
                    s=s[m+1:]
                    break
            c=c+str(t)+p
        print(*c)
        s=c
