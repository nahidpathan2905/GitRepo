s1="NAHID"
print(s1)
print(s1.lower())
print(len(s1))
s2=("velocity")
print(s2.upper())
print (s2.rfind('i'))
s3="abcdabcd"
s4="ABCDABCD"
print (s3.rfind('b'))   #last occurrence
print(s3.find('b'))   #first occurrance
print(s3.index('b')) #alternate way of first occurrence
print(s3[2:5])
print(len(s3))
print(s3==s4)  #compare data & case(case sensitive)
print(s3.__eq__(s4))   #alternate
print(s4.lower()==s3) #compare only data
s5="my name is nahid"
print("nahid" in s5)
print(s5.__contains__("my"))  #alternate way
print(s5.startswith("my"))
print(s5.endswith("abc"))