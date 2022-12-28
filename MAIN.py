print("................CHOOSE MODULE TO USE.............")
print("1.Student Modules")
print("1.Course Modules")
print("1.Batch Modules")
print("1.Department Modules")
print("1.Examination Modules")
a=int(input("enter module number to use"))
if a==1:
     import STUDENT
elif a==2:
    import COURSE
elif a==3:
    import BATCH
elif a==4:
    import DEPARTMENT
elif a==5:
    import EXAMINATION
else:
    print("Invalid choice, please try again")
