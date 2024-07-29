###______________________LOOP_______________######
  
  
#for var in range(starting point, stopping point ,jump ):

 #1 for loop
#example


for i in range(100): # 0-99
    print('welcome at upflair',i)    
   
   
company = "upflairs"
student_name = ['manshi','abhishek','mohit','sachin'] 
student_marks =(85,41,63,96,14,25)  
dt ={'a':10,'b':20,'c':30,'d':40} 
# key , value both

for char in student_name :
    print(char)
 
number = [14,52,63,96,85,74,8,15,25,36,147,966,42,15,36,4] 
  position == return 
count=0
for item in number:
     if item == 85 :
         print(count)
     count =count +1    
    
for item in number: 
        if item <=50:
          print(item) 
  
  
  
 #2 # WHILE LOOP  run when the condition is true
 
 
i = 0 
while i<=100:
    print("welcome at upflairs ! " ,i)
    i=i+1 
 
 ###  BREAK key word is use to break the loop at particular condition ignore other all remaning itration
   #### CONTINUE key word ignore current itration.
 

for i in range(11):
    print(i) 
    if i== 5:
        break
      continue 
    print(i) 
    
count = 0
for i in range (10) :
    continue
    count+=1
    break
    continue
print(count)  

 #3  ###________________FUNCTION______________________________func is a block of code that perform any certain task for multiple time..definition one time calling n time
 
    # 1. pre-defined : the func which is not defined by user is called predefined ex; append(),len()
    
    #2. user-defined:
    
## function
age = [10,20,30,40,50,60,70,80,90]
age2 = [1,2,3]
definition part

def my_len(ls):
    count = 0
    for i in ls:
        count+=1
    return count 
    
    
#calling part
print(my_len(ls=age)) # user defined function
print(my_len(age2))
print(len(age)) # predefined function


# for star pattern

for i in range(0,6) :
   for j in range(0,i+1) :
    print('* ', end="")
     print()

# Integer Pattern Program

i = 0
while i<6 :
    for j in range(0,i+1) :
       print(j+1, '', end="")
    print()
    i += 1 


# Program to find max & min item in a list

ls = [45, -6, 67, -15, 61, 25, 43, 85]

max = ls[0]
min = ls[0]
for i in ls :
    if i<=min :
        min = i
    if i>=max :
        max = i
    
print('max item:', max, 'present at index:', ls.index(max))
print('min item:', min, 'present at index:', ls.index(min))
    
  
  
    
    
 
    
  
  
    
    
 
    
