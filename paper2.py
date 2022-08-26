def circle(r):
    circumference=2*3.14*r
    area=3.14*r*r

    return circumference,area

s=int(input("enter radius: "))
z=circle(s)
print("ur area is: ",z)
