a="Hello World"

print(a[3])    #acces elemnt of the string

print(len(a))  # length of the string


#check

txt= "The best thing in life is free!"
print("free" in txt)
print("Free" in txt)


#Slicing of the text

a= "Hasibur Rahman"
print(a[2:7])
print(a[0:15])


#upper and lower case 

a= "Hasibur Rahman"
print(a.upper())
print(a.lower())

#String Concatenation/adddition of a string

a="Hasibur"
b="Rahman"
c="Tareq"
d= a+" "+b+" "+c
print(d)

#string  format using a placeholder

age= 24
txt=f"My name is Rohit, I am {age}"
print(txt)