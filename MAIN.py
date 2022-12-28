print("................CHOOSE MODULE TO USE.............")
print("1.Student Modules")
print("2.Course Modules")
print("3.Batch Modules")
print("4.Department Modules")
print("5.Examination Modules")
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
