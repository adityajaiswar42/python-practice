list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)
tup1=(1.5,'a',True)
print(tup1)
a=int(input("enter ur no: "))
fact=1
for i in range(1,6):
    fact=fact*i
print(fact)
def fact(n):
    if(n==1):
        return 1
    else:
        hello=fact(n-1)    
        result=n*hello
        return result
c=fact(4)
print(c)
# from tkinter import N


num=1
n=5
while(n>=1):
    num=num*n 
    n=n-1
    # return num
    print(n)
print("by by")    
