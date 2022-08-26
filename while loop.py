# i=int(input("i ki value daal: "))
i=1

j=0
n=int(input("num daal: "))
# n=7
while(i<=n):
    while(j<=(i-1)):
        print(i,end=" ")
        j=j+1
    print('\r')
    j=0 
    i=i+1
print("loop break")    