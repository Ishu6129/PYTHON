import numpy 
import time as t
'''

dtype : Defining type of data     default:int32

        if dtype='uint8'  and we enter more thaan 255 than it again start with zero
        if dtype='uint8'  and we enter -1 than it will consider as 255
        
        if dtype='int8'  and we enter -129 than it will consider as 127
        if dtype='int8'  and we enter 128 than it will consider as -128
        if dtype='int8'  and we enter -126 than it will consider as 126
        if dtype='int8'  and we enter 126 than it will consider as -126
        
ndmin : accept only defined dimension or more than that else convert to defined dimension

'''
#1
# input : 1 2 3 4
# output : [4. 3. 2. 1.] 
'''
n=list(map(int,input().split()))
s=t.time()
print(np.flip(np.array(n,dtype="float")))
print(t.time()-s)
'''
#2
# input : 1 2 3 4 5 6 7 8 9
# output : [[1 2 3]
#           [4 5 6]
#           [7 8 9]] 
'''
n=list(map(int,input().split()))
s=t.time()
ar=np.array(n,ndmin=2).reshape((3,3))      # uses .shape to show its shape => (3,3)
print(ar)
print(t.time()-s)

# or 

s=t.time()
ar=np.array(n,ndmin=2)
ar.shape=3,3
print(ar)
print(t.time()-s)

'''
#3
'''
r,c=list(map(int,input("Enter r and c ").split()))
s=t.time()
print(np.eye(r,c)) # can also mention dtype in function
print(t.time()-s)
'''
'''
# for ones matrix

r,c=list(map(int,input("Enter r and c ").split()))
out1=np.ones((r,c))
out2=np.full((r,c),2)
print(out1,out2,sep="\n")

# Addition and subtraction

r,c=list(map(int,input("Enter r and c ").split()))
m1=np.full((r,c),7)
m2=np.full((r,c),2)
print("Addition")
print(np.add(m1,m2))
print("Subtraction")
print(np.subtract(m1,m2))
'''
#4
'''
r,c=list(map(int,input("Enter r and c ").split()))
m1=[]
m2=[]
for i in range(r):
    m1.append(list(map(int,input().split()))) # --  np.array(list(map(int,input().split()))).reshape(r,c)

for i in range(r):
    m2.append(list(map(int,input().split())))
a=np.array(m1)
b=np.array(m2)
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.floor_divide(a,b))
print(np.mod(a,b))
print(np.power(a,b))
'''
#5
'''
r,c=list(map(int,input("Enter r and c ").split()))
m1=[]
for i in range(r):
    m1.append(list(map(int,input().split())))
a=np.array(m1)
print(np.transpose(a))
print(list(a.flatten()))
'''
'''
a=numpy.array([1,2,0,-2,0])
print(a.astype(bool))
#or
print(a!=0)
'''
'''
a=numpy.array([1,2,3])
a[:]=0
print(a)
'''
