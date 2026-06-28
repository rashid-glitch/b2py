#Type Checking
#--------------

a="table"
b=23
c=4.2
d=False
print(type(a) ,type(b), type(c), type(d))

#Swapping
#---------------

"""
=10
b=20
print("Before swapping")
print("a=", a)
print("b=", b)
temp=a
a=b
b=temp
print("After swapping")
print("a=", a)
print("b=", b)
"""
a=10
b=20
print("before swapping")
print(f"a= {a}, b={b}")
a, b =b, a
print("After swapping")
print(f"a= {a}, b={b}")

#Swapping
#------------

principal= 5000
rate=8
time =3
si= (principal*rate*time)/100
print("Simple interest=", si)

#String Reverse and upper, lower
#-----------

fullName="Rashid Ray"
print(fullName.upper())
print(fullName.lower())
print(fullName[::-1])

#String split, check vowels
#-------------

fullName="Rashid Ray"
i=0
for char in fullName:
  if char in "aeiouAEIOU":
    i+=1
print(i)
print(fullName.split())
