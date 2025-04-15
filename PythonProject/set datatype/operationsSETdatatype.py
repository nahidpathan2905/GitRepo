s={"abc",10,32.6,201,201}
print(s)  #doesnt maintain order
print(len(s))  #duplicate not allowed
print("---------add element----")
s.add(43)
s.add("xyz")
print(s)
print("----------add multiple element----")
s.update([-1,3])  #use []for multiple element
print(s)
print("------remove elements")
s.remove(10)
#s.remove(-10) #throws error if element doesnt exist
s.discard(-5)  #no error even element doesnt exist
print(s)
s.pop()  #remove random element
print(s)
#copy
set=s.copy()
print(set)
#sorting
s1={4,9,8,1}
s2=sorted(s1)
print(s2)
#clear set
s1.clear()
print(len(s1))
#delete set
del s2
print(s2)