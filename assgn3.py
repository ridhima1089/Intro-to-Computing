### Question 1
#################################

print('Solution 1')

#Taking input from user

input_string=input('enter a string :')
if ' ' in input_string :
    list1=input_string.split() 
else :
    list1=list(input_string)
count={}       # specifing empty dictionary to count the no. of occurance
for i in list1 :         
    if i not in count :
        count[i]=1
    else :         
        count[i]=count[i]+1
#### printing the occurance of the  each word or character
for i in count :
    print(i,count[i])

print('\n')

##Question 2
##########################################
print("Solution 2")

#Taking inputs from user
day=int(input('Enter a valid date between 1 to 31- ')) 
month= int(input('Enter a valid month between 1 to 12- '))
year=int(input('Enter a valid year between 1800-2025- '))
###Removing all invalid cases
if day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025 or (month in [4,6,9,11] and day>30) or (month==2 and year%4!=0 and day>28) or (month==2 and year%4==0 and day>29):
         print('Enter a valid inputs')
###following are the valid cases
else:
    if month==2:  ## Dealing with leap and non-leap year in month==2
        if year%4==0:
            if day <29:
                day=day+1
                print('Next Date is',day,'/',month,'/',year)
            else:
                print('Next date is 01/03/',year)
        else:
            if day<28:
                day=day+1
                print('Next Date is',day,'/',month,'/',year)
            else:
                print('Next date is 01/03/',year)
    elif month in [4,6,9,11]:  ## month  having 30 days
        if day<30:
           day=day+1
           print('Next Date is',day,'/',month,'/',year) 
        else:
            print('Next date is 01/',month+1,year)
    else:
        if day<31:             ## dealing with month having 31 day and month of december
            day=day+1
            print('Next Date is',day,'/',month,'/',year)
        else:
            if month==12:
                print('Next date is 01/01/',year+1)
            else:
                print('Next date is 01/',month+1,year)
                
    print('\n')



## QUESTION 3
##############################################
print('Solution 3')
list=[3,9,10]
list1=[]      ## create the empty list
for i in list:
    tup=(i,i*i)
    list1.append(tup) ### using append function to add tuples to list
print(list1)
print('\n')

## QUESTION 4
###################################################
print("Solution 4")
grade_point=int(input('Enter the grade point [integer between (4,10)]: '))
if grade_point<4 or grade_point>10 :
    print('invalid input')
else :        ## Specifiing dictionaries each for grade and performance having grade_point as theirs keys:
    grade={4:'D',5:'C',6:'C+',7:'B',8:'B+',9:'A',10:'A+'}
    performance={4:'Poor',5:'Below Average',6:'Average',7:'Good',8:'Very Good',9:'Excellent',10:'Outstanding'}
      ## printing the required for a input given 
    print('Your grade is',grade[grade_point],'and',performance[grade_point],'performance')
print('\n')

## Question 5
######################################
print("\nThe solution of Question 5 is:\n")
string = "ABCDEFGHIJK"
j = 0
while len(string) - j*2 >= 1:
    print(" "*j + string[0 : len(string) - j*2])
    j += 1
    print('\n')



## Question 6
##########################################

print("Solution6")
condition=True

#Defining dictionary to store the values
Dictionary={}
prompt="y"
while condition:                                        ### using 'while' loop to ask for details of student
    if prompt.lower()=="y":
        SID=int(input("Please Enter SID of Student- "))
        name=input("Please enter the name of the Student- ")
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N- ")
        condition = True

    else:
        condition = False
#Part a
print("Part a")
for key,value in Dictionary.items():
    print(f"{key} is {value}")
print("")

#Part b
print("Part b")
Val_sort_dict= sorted(Dictionary.values())
print(f"value sorted dictionary is {Val_sort_dict}")
print("")

#Part c
print("Part c")
Key_sort_dict= sorted(Dictionary.keys())
print(f"Keys sorted dictionary is {Key_sort_dict}")
print("")

#Part d
print("Part D")
SID_tbf=int(input("Please enter the student's SID whose detail you need- "))
if SID_tbf in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[SID_tbf]}")
else:
    print("The SID is not present in the given Data")
print("")



## QUESTION 7
##############################################
print('Solution 7')

### Taking input From the user

n=int(input('Enter the number till you want to See fibonacci series: '))
def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    
    return   fib(n-2)+fib(n-1)
for i in range(1,n+1):
    print(fib(i),' ',end='')


## QUESTION 8
#######################################
print(" ")    
print("Solution 8") 

Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

##Part a
print('Part a')
##a new set of all elements that are in Set1 and Set2 but not both.
set_new=Set1^Set2
print(set_new)

## Part b
print('Part b')
### a new set of all elements that are in only one of the three sets Set1, Set2 and Set3.

Set4=Set1^Set2^Set3
print(Set4)

##Part c
print('Part c')
### a new set of elements that are exactly two of the sets Set1, Set2 and Set3.

set5=Set1 & Set2
set6=Set2 & Set3
set7=Set1 & Set3
set8=set5^set6^set7
print(set8)

##Part d
print('Part d')
##a new set of all integers in the range 1 to 10 that are not in Set1.
list1=[]    # creating an empty list
for i in range(1,11) :
    if i not in Set1:
        list1.append(i)
set9=set(list1)     # converting list into set 
print(set9)

# Part e
print('Part e')

list2=[]          # creating an empty list 
for i in range(1,11) :
    if (i not in Set1) and (i not in Set2) and (i not in Set3):
        list2.append(i)
set10=set(list2)         # converting list into set 
print(set10)
