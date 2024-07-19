def  add (num1 ,num2):
     return num1 + num2

def  substract(num1 ,num2):
    return num1 - num2

def  multiply (num1 ,num2):
    return num1 * num2

def division ( num1 , num2):
     return num1 / num2
 

print("Select operaton.")
print("1 -Add")
print("2 -Substraction")
print("3-Multiplication")
print("4-Division")


#Take input from the user 
Choice = int(input("Enter your choice (1,2,3,4): "))

num1 =int(input("Enter first number: "))
num2 =int(input("Enter second number:"))

if (Choice ==1):
    
    print  ("The addition of given two numbers is" ,num1+num2)
    
elif( Choice ==2):
    
    print  ("The substraction of given two numbers is",num1-num2 )
    
elif (Choice ==3):
    
    print ("The multiplication of given two numbers is",num1*num2)
    
elif ( Choice ==4):   
    
    print ("The division of given two numbers is", num1/num2)
    
else :
    print ("Invalid operation ")
    

    
