## Lists and Tupples code

data = [24, 30, 36, 42]

data.append(50)
data.remove(42)

print(data)

data = (24, 30, 36, 42)

new_data = list(data)

new_data.append(45)
new_data.remove(42)

print(new_data)


##TASKS code

x = [1, 2, 3, 4, 5]

x.append(6)
x.remove(2)

total = sum(x)
print(x)
print(total)

##task 2

cities = ('USA', 'Australia', 'Denmark', 'Iceland', 'Finland')

print(cities[2])

new_cities = list(cities)

new_cities.append('Canada')

print(new_cities)

moddified_cities = tuple(new_cities)

print(moddified_cities)


## Third task

marks = {
    "Maths": 90,
    "English": 85,
    "Physics": 92,
    "Chimestry": 95
}

marks["Higher math" ] = 95

marks["Maths"] = 95


print(marks)


total_marks = sum(marks.values())

number_of_subjects = len(marks)

average = total_marks / number_of_subjects

print(average)

