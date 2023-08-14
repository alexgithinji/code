#tuple = it is a collection which is ordered and unchangeable
    #  used to group together related data

student = ("alex",21,"male")
print(student.count("alex"))
print(student.index("male"))

for x in student:
   print(x)
   if "alex" in student:
       print("alex is available!")
