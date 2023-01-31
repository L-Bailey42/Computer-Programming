#Task 1
print(10 < 100)
print(100 != 100)
print(50 >= 50)


#Task 2
age = int(input("\nEnter your age: "))
print(age < 18)
print(age < 21)
print(age < 31)


#Task 3
print("\n")
print("a" < "b")
print("b" < "a")
print("John" < "Terry")


#Task 4
print("\n")
print("john" < "Terry")


#Task 5
print("\n")
print(5 < 10.2)
#print(5 < "Monty")
#print(5 < "5")


#Task 6
age = 30
print("\n")
print(age >= 18 and age <= 65)
print(age < 18 or age > 65)
print(not age > 18)


#Task 7
age = 30
print("\n")
print((age >= 18 and age <= 65) and (not age == 30))


#Task 8
weight = 83
height = 194
print("\n")
print(100 < weight and weight < 200)
print(height > 131 and height < 160)


#Task 9
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
print("\n")
print("Eric" in names)
print("Mark" not in names)

print("\n")
message = "Hello there, my name is John"
print("nam" in message)


#Task 10
age = int(input("\nEnter your age: "))
if 18 <= age <= 30:
    print("You are still young!")


#Task 11
age = int(input("\nEnter your age: "))
if 18 <= age <= 30:
    print("You are still young!")
elif 30 < age <= 40:
    print("You are not quite as young...")


#Task 12
name = input("\nEnter your name: ")
if len(name) == 0:
    print("Your name is",name)
else:
    print("Name not entered")


#Task 13
age = int(input("\nEnter your age: "))
print("You are an adult" if age >= 18 else "You are not an adult, yet!")
