## ____________string_____________
st = "keshav"
print (st)
print(type(st))
# IN Single coted single line m hi do statement likhte varna error ajayega
 
st= 'upflairs'

print(st[starting : stopping : jump])

print(st)
print(st[3])
print(st[-4])
print(st[0:3])
print(st[:3])  #starting =0
print(st[3:])   # stoping = end

st= 'upflairs'

print(st.upper()) # function

st= 'UPFLAIRS'
print(st.lower())
print(st.capitalize())
print(st.title())

st='PRADUMAN'
print(len(st)) #no of character
print(st.count('A'))
print(st.find('P')) #index of P

st='PRADUMAN SINGH ' 
print(st.split( ',')) 
print(st)
print(st.replace('SINGH','king'))

print(st.replace('SINGH',''))
print(st.replace('S',''))

     #datatype_________________ BOOLEAN__________
     
var1 = True
var2 = False 
print(var1,var2)
print(type(var1),type(var2))    


## datatype _______________LIST________
  
  #list = collection of different data type   only  in a PYTHON it is a dynamic aaray.
  
ls=[10,20,30,40,50.25,41,2.3,'keshav',True]
print(ls)
print(type(ls))
ls=[10 ,20,30,40,50,60,70]
#   0   1  2  3  4  5  6
#   -7  -6 -5 -4 -3 -2 -1
print(ls[3])
#print(ls[4:])

#insert,deletion,
student_name = ['mohit','keshav','tushar']
print(student_name)
student_name.append('vinay')  # append function is use for adding item in the last position...

print(student_name)
student_name.pop() # it remove by default from last
print(student_name)

student_name.pop(0)
print(student_name) 

student_name = ['mohit','keshav','tushar'] 
student_name[1] = 'keshav  singh'  # to update tha record by indexing
print(student_name) 
student_name.insert(0,'vinay') # insert is use to add a item by indexing.
stdent_name.append()
print(student_name)


ls=[10,20,30,40,50,60,True,[40,20,30,'upflairs']]
print(ls[7])
ls[7][3]='flipkart'
print(ls)



#_____________________________TUPLE_____________ (it is imutable means can't change)

#tpl=(52,41,63,52,52,85.2,41,20.01,'upflairs')

print(tpl)
print(type(tpl))
tpl.count()
tpl.index()
# access = yes
# remove = NO
# insert = no
# update = no 
   
#tpl=10,20,30
print(tpl)

#_____________________________SET________________________________________ indexing not allow

## duplicate not allow in output
## doesnt maintain the order 
## imutable 
# access = NO
# remove = YES
# insert = YES
# update = no 

st={42,20,30,42,55,405}
print(st)
print(type(st)) 
st.remove(20) # show error when item is not given
st.discard(45)  # it does not show error when item is not present

st.add(35)

print(st)

