list1=[10,11,12,13,14,15,16]
for rollNo in list1:
    if rollNo==13:
        continue
    print(rollNo)
print("-------------------")
Emp_salary=[5000,6000,8000,2000,4000,3200,1500]
for salary in Emp_salary:
    if salary<2000:
        continue
    print("Paid:",salary)