# def area(r):
#     a=3.14*r*r
#     c=2*3.14*r*r
#     print("area of a circle is",a)
#     print("area of a curcumference is",c)
# b,a=int(input("ensvag :"))
# # b=area(r)
# print(b)    
# import math 
# x=input("enter fun ")
# n=int(input("num"))
# x**n==n*(x**n-1)
# print(x**n)
# from re import X


# x=input("enter fun ")
# n=int(input("num"))
# if(x==x):
#     x=n*x**n-1
#     print(x)
# else:
#     print("invalid")
# from itertools import zip_longest

# class Polynomial:
#     def __init__(self, coefficients):
#         self.coefficients = coefficients
        
#     @property
#     def order(self):
#         return len(self.coefficients) - 1
    
#     def derivative(self):
#         return Polynomial([i*j for i,j in enumerate(self.coefficients)][1:])
    
#     def __add__(self, other):
#         return Polynomial([i + j for i, j in zip_longest(self.coefficients, other.coefficients, fillvalue=0)])
    
#     def __repr__(self):
#         return f"Polynomial({list(self.coefficients)})"
        
#     def __str__(self):
#         return " + ".join(reversed([f"{j}x^{i}" for i, j in enumerate(self.coefficients)]))
    
#     def __call__(self, x):
#         return sum(j*(x**i) for i, j in enumerate(self.coefficients))
# def circle(r):
#     a=3.14*r*r
#     print("Area of a circle:",a)
#     c=2*3.14*r
#     print("Area of curcumference:",c)
# r=int(input("Enter the No:"))
# c=circle(r)
# print(c)    
def integration(r,n):
    a=n
    print(a,**n-1)
    

n=int(input("enter your n value : "))
integration(r,n)
    
    
    
