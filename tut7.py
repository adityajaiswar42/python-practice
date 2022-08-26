# hey=(12.34,'aditya',True)
# hello=(25.75,'vyankat',False)
# world=hey+hello
# print(world)
# from ast import Num


def fact(x):
    if x==1:
        return 1
    else:
        return(x*fact(x-1))
num=int(input("enter num"))
print("fact is ",fact(num))


# hey[1]='rohit'
# print(type(hey))
# list=['aditya','24','true']
# list[1]='vyankat'
# print(list)
