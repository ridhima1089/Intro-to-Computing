### ASSIGNMENT 1

### 1)Write a Python program to find average of three numbers entered by the user. ###

## "Taking input from user" ##
print("Answer Number 1")

Num1= float(input("Enter the Num1- "))
Num2= float(input("Enter the Num2- "))
Num3= float(input("Enter the Num3- "))

## Taking average using formula ##

avg= (Num1+Num2+Num3)/3

print("AVERAGE OF THREE NUMBER - ",avg)



### 2)Write a python program to compute a person's income tax laws...###

## Asking Gross Income and the number of dependents from the user ##
print("Answer Number 2")


gross_income=float(input("Enter the Gross income to the nearest penny-  "))
num_dependents=float(input("Enter the number of Dependents- "))

Taxable_income= gross_income - 10000 - (3000*num_dependents)
Tax=(Taxable_income*20)/100

if Tax<0 :
    print("Your tax is 0$")
else:
    print(Tax)

### 3)Write a python program to store different data type values into a list. ###
print("Answer Number 3")


print("Student-[Sid , Name , Gender , Department name , CGPA]")
Student=[21105007 ,'Ridhima','F','ECE',9.5]
print("Student- ",Student)

### 4)Write a python program to enter marks of 5 students into a list and display them in sorted manner.###
print("Answer Number 4")


Marks=[67,82,90,75,88]
print("Marks before sorting ")
print(Marks)
Marks.sort()
print("Marks after sorting ")
print(Marks)

### 5)(a)Write a Python program to print a specified list after removing 4th element.
print("Answer Number 5(a)")


color=['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print(color)



### 5)(b)Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
print("Answer Number 5(b)")
color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=["Purple"]
print(color)
