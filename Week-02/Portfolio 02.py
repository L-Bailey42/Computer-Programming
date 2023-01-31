#Task 1
name = input ("Enter your name: ")
print("Hello",name)


#Task 2
c_temp = float(input("\nEnter a temperature in Celsius: "))
f_temp = (c_temp*(9/5)) + 32
print("Celsius: ",c_temp,"\nEquivalent Farenheit: ",f_temp)


#Task 3
student_num = int(input("\nEnter number of students: "))
group_size = int(input("Enter size of group: "))

group_num = student_num // group_size
extra_students = student_num % group_size
print("There wil be",group_num,"full group(s), and",extra_students,"extra students in a smaller group.")


#Task 4
student_num = int(input("\nEnter number of students: "))
sweet_total = int(input("Enter number of sweets: "))

sweet_num = sweet_num // student_num
extra_sweets = sweet_num % student_num
print("There wil be",sweet_num,"sweets per student and",extra_sweets,"sweets left over."
