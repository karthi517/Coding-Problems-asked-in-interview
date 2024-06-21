#Amazon: Given two arrays, write a function to get the intersection of the two. For example, if A=[1,2,3,4,5],and B=[0,1,3,7] then
# 
#  you should return [1,3]

A=list(map(int,input().split()))
B=list(map(int,input().split()))

A=set(A)
B=set(B)

if(len(A)<len(B)):
    C=[i for i in A if i in B ]
else:
    C=[i for i in B if i in A]
print(*C)