## some for loop examples

languages = 'Python'

for i in  languages:
    print(i)

languages = ['Swift', 'Python', 'Go']

for i in languages:
    print(i)

    print(".........")


i = 0, 3
for i in range(0, 4):
    print(i)

languages = ['Swift', 'Python', 'Go']

for lang in languages:
    if lang == 'Go':
        break
    continue
    print(lang)
   
# outer loop 
i = ['Electric', 'Fast']
j = ['Tesla', 'Porsche', 'Mercedes']

for x in i:
    if i == 'Fast':
        continue
    for y in j:

        if j == 'Mercedes':
            break
        print(x,y)
        print()

for x in range(6):
  print(x)
else:
  print("Finally finished!")

for x in range(7):

    if x == 4:
        break
    print(x)

else:
    print("Fianlly Finsahed")

##Using while loop

i = 0

while i<3:
    print("Hello World")

    i += 1
