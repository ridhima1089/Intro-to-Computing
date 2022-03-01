print("Solution1")
print(" ")
# define a recursive function
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 1:
        print("Move disk 1 from rod",from_rod,"to rod",to_rod)
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
         
#ask user for input
n = int(input("Enter the number of disks"))

#call the function 
TowerOfHanoi(n, 'A', 'C', 'B')

########################################################

print("Solution2")
print(" ")
#input rows
n = int(input("Enter the number of rows in Pascal's Triangle: "))

#using recursions
print("\nUsing recursions:\n")
def pascal(n, originaln=n):
    if n == 0:
        return
    
    pascal(n-1,originaln)

    #printing the spaces
    print('  '*(originaln-n), end='')

    #first number is always 1
    entry = 1
    for i in range(1, n+1):

        print(entry, end ='   ')

        #using Binomial Coefficient
        entry = entry * (n - i) // i
    print()
pascal(n)

#using loops
print("\nUsing loops:\n")
for line in range(1, n+1):

    #everything else same as recursion
    print('  '*(n - line), end='')

    x = 1
    for i in range(1, line+1):

        print(x, end='   ')

        x = x * (line - i) // i
    print()
print("")

#####################################################################################



############################################################
print("Solution4")
print(" ")
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Ridhima", "21105007")
print("Object created")

#printing the assigned values
print("The name of the student is {student1.name} and SID is {student1.sid}.")

#deleting object
del student1
print("")

##############################################################
print("Solution5")
print(" ")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __del__(self):
        print(f"Employee {self.name} record deleted")

#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part a, updating salary
employee1.salary = 70000
print(f"a. The updated salary of the employee {employee1.name} is {employee1.salary}")

#part b, deleting a record
print("b. ", end='')
del employee3

print(" ")

#################################################
print("Solution6")
print(" ") 
input_friend1 = str(input("Enter the word from friend 1:")).lower()
input_friend2 = str(input("Enter the word from friend 2:")).lower()

list_word = []

def split_dict(word):
    letters = []
    for x in word:
        letters.append(x)
    string_dict = {}
    for letter in letters:
        if letter in string_dict:
            string_dict[letter] += 1
        else:
            string_dict[letter] = 1
    global list_word
    list_word.append(string_dict)
    


split_dict(word = input_friend1)
split_dict(word = input_friend2)


#store each element of list_word to a separate variable
dict1 = list_word[0]
dict2 = list_word[1]

for i in dict1:
    if i in dict2: 
        #letter matched. 
        #now match the value
        if dict1[i] == dict2[i]:
            #value matched
            print(" :)")
            print("")
        else: 
            print(" :( ")
            print("")
    else: 
        print(" :( ")
        print("")
            
#ask shopkeeper for input to check result of for loop;and also check if the word is meaningful
print("")

shopkeeper1 = str(input("Press N if any of the above result was :( , otherwise press Y  ---- ")).lower()


print("")
print("")
if shopkeeper1 == 'y':
    shopkeeper = str(input("Does the word 2 make sense? Y/n ---- ")).lower()
    if shopkeeper == "y":
        print("Friendship is true")
        print("")
    else:
        print("Fake friendship! Don't worry, this is for fun!")
else: 
    print("Fake friendship! Don't worry, this is for fun!")
