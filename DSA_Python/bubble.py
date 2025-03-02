def bubble_sort(l):
    for i in range(1,len(l)):
        for j in range(len(l)-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
def modified_buble_sort(l):
    flag=False
    for i in range(1,len(l)):
        flag=False
        for j in range(len(l)-i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                flag=True
        if not flag:
            break
l=[89,24,12,54,21,9]
modified_buble_sort(l)
print(l)