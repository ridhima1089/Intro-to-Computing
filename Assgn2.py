print('Solution 1')
### giving value to input_string.
given_string='Python is a case sensitive language'
# printing the length of given string
print('Length of given string = ',len(given_string))
#printing the input_string in reverse order.
print('Reversing the given string = ',given_string[::-1])
#slicing and printing the input_string. 
sliced_string=given_string[10:26]
print('Using slice function-',sliced_string)
#replacing and printing new string
new_string= given_string.replace('a case sensitive','object oriented')
print(new_string)
#printing index of "a" from given_string
print(given_string.index('a'))
#Removing the white spaces.
print(given_string.replace(' ',''))

print('Solution 2')

print('string formatting')
name='Ridhima'
sid= 21105007
department='ECE'
CGPA=9.9
print('Hey, %s Here!'%name)
print('My SID is %d '%sid)
print('I am from %s department and my CGPA is %f'%(department,CGPA))

print('Solution 3')

a=56
b=10
print(' a&b :', a & b)
print(' a|b :', a | b)
print(' a^b :', a ^ b)
###Left shift  both a and b with 2 bits.
print('a<<2 : ', a<<2)
print('b<<2 : ', b<<2)
###Right shift a with 2 bits and b with 4 bits.
print('a>>2 : ', a>>2)
print('b>>2 : ', b>>2)

print('Solution 4')

###taking input of 3 numbers from the user.

a=input('Enter num1: ')
b=input('Enter num2: ')
c=input('Enter num3: ')

### finding the highest no.
if a>b and a>c:
    print('Highest number: ',a)
if b>a and b>c:
    print('Highest number: ',b)
else:
   print('Highest number: ',c)

print('Solution 5')

###Taking input string from the user.
input_string=input('Enter the string: ')
if 'name' in input_string:
    print('Yes')
else:
    print('No')

print('Solution 6')

###Taking input of 3 lengths from the user
a = int(input("Enter 1st length : ")) 
b = int(input("Enter 2nd length : "))
c = int(input("Enter 3rd length : "))

if a+b > c and a+c > b and b+c > a:
    print("Yes")
else:
    print("No")
