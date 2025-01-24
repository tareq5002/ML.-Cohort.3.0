#Arithmatic opreation

a= 10
b= 5
c= 9

sum= a+b+c
d= a-b
e= a*b*c
f= a/b

print(sum,d,e,f)

##flor divison

g=9
h=4
i=g//h
print(i)

##modulus operator

j= g%h
print(j)

##Logical operator

x= 10
y= 55
z= 20

if x>y and x>z:
    print("x is the largest")

elif y>x and y>z:
    print("y is the largest")

else:
    print("z is the largest")


##task 1 using user input determine the value of the largest number

x= int(input("Enter the value of x:"))
y= int(input("Enter the value of y:"))
z= int(input("Enter the value of z:"))

if x>y and x>z:
    print("x is the largest")

elif y>x and y>z:
    print("y is the largest")

else:
    print("z  is the largest")

 ## task 2 Using user input determine the lowest and average cgpa between 3 friends

cgpa1= float(input("Enter the value of cgpa1:"))
cgpa2= float(input("Enter the value of cgpa2:"))
cgpa3= float(input("Enter the value of cgpa3:"))

average= (cgpa1+cgpa2+cgpa3) / 3

print(average)

if cgpa1<cgpa2 and cgpa1<cgpa3:
    print("cgpa1 is the lowest cgpa")

elif cgpa2<cgpa1 and cgpa2<cgpa3:
    print("cgpa2 is the lowest cgpa")

else:
    print("cgpa3 is the lowest cgpa")


##Done all the tasks.