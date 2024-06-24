#D.E. Shaw:Given an  integer array maximum product of any three numbers in the array. For example, for A=[1,3,4,5], you should 
# return 60, while for B=[-2,-4,5,3] you should return 40

def Max_product(A):
    A.sort()
    return max((A[0]*A[1]*A[-1]),A[-1]*A[-2]*A[-3])

A=list(map(int,input().split()))
print(Max_product(A))