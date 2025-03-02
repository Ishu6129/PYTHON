#1

def NaturalNumberUpto(n):
    if n>0:
        NaturalNumberUpto(n-1)
        print(n,end=" ")
NaturalNumberUpto(10)

#2
print()

def NaturalNumberReverse(n):
    if n>0:
        print(n,end=" ")
        NaturalNumberReverse(n - 1)
NaturalNumberReverse(10)

#3
print()

def FirstNOdd(n):
    if n>0:
        FirstNOdd(n-1)
        print(2*n-1,end=" ")
FirstNOdd(10)

#4
print()

def FirstNEven(n):
    if n>0:
        FirstNEven(n-1)
        print(2*n,end=" ")
FirstNEven(10)

#5
print()

def FirstNOddRevese(n):
    if n>0:
        print(2*n-1,end=" ")
        FirstNOddRevese(n-1)
FirstNOddRevese(10)

#6
print()

def FirstNEvenReverse(n):
    if n>0:
        print(2*n,end=" ")
        FirstNEvenReverse(n-1)
FirstNEvenReverse(10)

#7
print()

def SumOfN(n):
    if n==1:
        return 1
    return n+SumOfN(n-1)
print(SumOfN(5))

#8

def SumOfNOdd(n):
    if n==1:
        return 1
    return 2*n-1 + SumOfNOdd(n-1)
print(SumOfNOdd(5))

#9

def SumOfNEven(n):
    if n==1:
        return 2
    return 2*n + SumOfNEven(n-1)
print(SumOfNEven(5))

#10

def Factorial(n):
    if n==1:
        return 1
    return n*Factorial(n-1)
print(Factorial(5))

#11

def SumOfFirstNSquare(n):
    if n==1:
        return 1
    return n*n+SumOfFirstNSquare(n-1)
print(SumOfFirstNSquare(5))

#12
def fib(n):
    if n<=1:
        return n
    else:
        a=fib(n-1)
        b=fib(n-2)
        return a+b
print(fib(0))