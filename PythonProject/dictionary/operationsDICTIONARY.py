dict={1:"a",2:"b","c":20}
print(dict)
print(dict[2])
print(dict["c"])
#example
student={
    "name":"nahid",
    "age":27,
    "grade":"A"
}
#accesing values
print(student["name"])
print(student.get("age"))
#adding new pair kry:value
student["course"]="math"
print(student)
#updating existing value
student["age"]=28
print(student)
#removing ewlement
student.pop("grade")
print(student)
#removing last inserted item
student.popitem()
print(student)
#cheking if key exist
print("course" in student)
print("name" in student)
#accessing key,values and items
print(student.keys())
print(student.values())
print(student.items())
#iterating through dictionary
for key,value in student.items():
    print(f"{key}:{value}")