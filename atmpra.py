Name = input("Enter your name :")
print("Hellow Dear",Name)
message =  '''
HOW CAN I HELP U SIR.

PLEASE SELECT ANY OPTION .
TYPE 1 >>> CHECK BANK AMOUNT.
TYPE 2 >>> DEPOSIT AMOUNT.
TYPE 3 >>> WITHDRWAL AMOUNT.

'''
print(message)
task = int(input("choose any option : "))
available_amount=10000

if task>=1 and task<=3 :
    print("WELCOME YOU IN BOB BANK")
    
    if task == 1 :
     print("THANKS FOR VISITING US ,YOUR available amount IS : ",available_amount,'INR')
     
    elif task == 2 :
        deposit_amount =int(input("ENTER YOUR DEPOSIT AMOUNT : "))
        print(deposit_amount) 
        
        if deposit_amount >=500:
            available_amount = available_amount + deposit_amount 
            print("You Have Successfully deposite your amount : ",deposit_amount)
            print("Your available amount is : ",available_amount) 
            print("Thanks for visiting us")  
            
        else:
             print("Plz deposite at least 500 rupees ! ") 
              
             
    else:
         withdrawl_amount=int(input("plz enter withdrawl_amount:"))
         
         if withdrawl_amount <= available_amount:
             available_amount -= withdrawl_amount
             print('You have successfully withdrawl your amount:',withdrawl_amount)
             print(" Your available amount is :",available_amount,'INR')
         else:
                print("You dont have sufficient amount in your account!")
                print("Your available amount is : ",available_amount,'INR')
else:
            print('plz choose coreect option ! ')     
            
            
            
            
        
        
        


