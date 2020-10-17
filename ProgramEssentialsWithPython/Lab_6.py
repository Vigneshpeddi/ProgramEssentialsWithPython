
#Week 8 Day 2 Lab #6 Vignesh Peddi

#Functions
def add(): #we are creating a function for addition
    if answer == 1: #the if statement will execute if the answer = 1
        num1 = float(input("What is the first number you would like to add: ")) #we are asking the user for the first number
        num2 = float(input("What is the second number you would like to add: ")) #we are asking the user for the second number
        sum = num1 + num2 #we are calculating the sum
        return sum #we are returning the sum
def subtract():  #we are creating a function for subtraction
    if answer == 2: #the if statement will execute if the answer = 2
        num1 = float(input("What is the first number you would like to subtract: "))#we are asking the user for the first number
        num2 = float(input("What is the second number you would like to subtract: "))#we are asking the user for the second number
        difference = num1 - num2 #we are calculating the difference
        return difference #we are returning the difference
   
def multiply():  #we are creating a function for multiplication
    if answer == 3: #the if statement will execute if the answer = 3
        num1 = float(input("What is the first number you would like to multiply: "))#we are asking the user for the first number
        num2 = float(input("What is the second number you would like to multiply: "))#we are asking the user for the second number
        product = num1 * num2 #we are calculating the product
        print("The product is",product) #we are printing the product
    
def divide():  #we are creating a function for division
    if answer == 4: #the if statement will execute if the answer = 4
        num1 = float(input("What is the first number you would like to divide: "))#we are asking the user for the first number
        num2 = float(input("What is the second number you would like to divide: "))#we are asking the user for the second number
        quotient = num1 / num2 #we are calculating the quotient
        return quotient #we are returning the quotient
def menu(): #we are creating the function for the menu options
    print("My Basic Calculator \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Exit") #we are printing the menu


#Base Program Code

exit = "n" #we are assigning the string 'n' to the variable exit
while exit == "n": #we are creatng a loop that will only execute if exit = 'n'
    menu() #we are calling the fuction menu
    answer = int(input("Which Option (Type the number of the option you want): ")) #we are asking the user for what option they want
    
    if answer == 5: #the if statement willonly execute if answer = 5
        exit = "y" #we are setting the variable exit to 'y
    elif answer == 1:   #the if statement willonly execute if answer = 1
        addition = add(); #we are assigning the function add() to the variable addition
        print("The sum is {:.0f}" .format(addition)) #we are printing the variable addition
    elif answer == 2:  #the if statement willonly execute if answer = 2
        sub = subtract();  #we are assigning the function subtract() to the variable sub
        print("The difference is",sub) #we are printing the variable sub
    elif answer == 3:  #the if statement willonly execute if answer = 3
        multiply() #we are calling the function multiply
    elif answer == 4:  #the if statement willonly execute if answer = 4
        div = divide(); #we are assigning the function divide() to the variable div
        print("The quotient is",div) #we are printing the variable div
