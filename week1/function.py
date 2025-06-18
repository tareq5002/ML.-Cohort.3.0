def my_function():
    print("Hello world from a function")

my_function()


def my_function(fname, mname, lname):
    print(fname + " " + mname + " " + lname)

my_function("HASIBUR", "RAHMAN", "TAREQ")



## NID creating usning python code- name, address, father name, mother name, cell number

def create_nid(name, father_name, mother_name, permanent_address, cell_number, gender):

    print("\n........... NID INFORMATION.............")       ##\n using for new line
    print()
    print("Name              :", name)
    print("Father_Name       :", father_name)
    print("Mother_Name       :", mother_name)
    print("Permanent Address :", permanent_address)
    print("Cell Number       :", cell_number)
    print("Gender            :", gender)

# Correct function call with a missing comma fixed
create_nid(
    "HASIBUR RAHMAN TAREQ",
    "Late Nur Mohammad",
    "Selina Begum",
    "Satkhira, Khulna",
    "01315975200",   # ✅ Comma added here
    "Male"
)
