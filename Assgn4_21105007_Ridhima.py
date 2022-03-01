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
print("Question 3")
print(" ")
a=int(input('enter first no. :'))  ##Getting input from user 
b=int(input('enter secod no. :'))
if b==0 :
    print('Denominator cant be 0 , error')
else :
    result=divmod(a,b)    ## calling divmod function
    print(result)
    print('\nPart a)')
    print(callable(divmod))   ## using callable function to check callability

    print('\nPart b)')
    if result[0] == 0 :   ## checking weather the values are non-zeros 
        if result[1] == 0 :
            print('both values are zero ')
    else :
       if result[1] == 0 :
            print('one value is zero')
       else :
            print('both values are non zero')    
    
    print('\nPart c)')
    lis=[result[0],result[1],4,5,6]   ##adding (4,5,6) to values and finding out values greater than 4 
    print(lis)
    set1=set()
    for i in lis :
        if i > 4 :
            print(i,end=' ')
            set1.add(i)   ## making set of the values
    print()


    print('\nPart d)')
    print(set1)

    print('\nPart e)')
    fr_set=frozenset(set1)  ## making set immutable
    print('the immutable set is :',fr_set)

    print('\nPart f)')
    b=max(set1)
    print('max value :',b)    ### calculating max value and its hash value
    print('Hash value :',hash(b))

print('')



############################################################
print("Solution4")
print(" ")

##creating a class
class Student:   ###Creating class with constuctor and destructor
    def __init__(self,name,roll_number):
        self.name=name           
        self.roll_number=roll_number

    def __del__(self) :
        print('Record of ',self.name,' destroyed')


s1=Student('Ridhima',21105007) ## creating a class and feeding data into it
print(s1.name)
print(s1.roll_number)
del s1      ## deleting the object s1
print('')

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
##Using anagram 
def anagram(s):  ## Defining the anagram function 
    if s=='' :
        return [s]
    else :
        word=[]
        for i in anagram(s[1:]) :
            for p in range(len(i)+1) :
                word.append(i[:p]+s[0]+i[p:])
        return word
### Talking input from the users 
word1=input('Give a word to test friendship :')
word_1=word1.lower()
word2=input('Give a meaningful word containing same letter of the word given by your friend :')
word_2=word2.lower()
## checking if the word contains same letter as the first word i.e its in its anagram or not
if word_2 in anagram(word_1) :  
    c=input('does the word entered by 2nd friend seems meaningfull ? (y/n) :')
    if c == 'y' :   ### checking the meaningfulness of word 
        print('Test passed thus  friendship is true')
    else :
        print('Test failed thus friendship is false ')
else :
    print('word does not have the same letter thus  test failed friendship is false ')
