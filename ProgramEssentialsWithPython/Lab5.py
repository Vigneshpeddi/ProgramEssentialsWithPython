#Week 7 Day 2 Lab 5 Vignesh Peddi
#This program follows the flowchart from lab 5

answer = "y" #we are setting the answer as y
while answer == "y": #when answer is y, the loop will begin
    ip_address = input("Please enter your ip address with no encryption: ")#we are prompting the user for their ip address
    ipsplit = ip_address.split(".", 4)#we are splitting the ip address into four octets 
    print("The ip address is {0}" .format(ip_address))#we are printing the ip address
    first_octet = int(ipsplit[0])#we are adding the value of the first part of the ip address to the variable first octet
    if first_octet <= 191 and first_octet >= 128: #the if statement will execute when the first octet is between 128 and 191
        print("This is a Class B Address") #we are printing the statement, "This is a Class B Address", if the if statement is true
    elif first_octet <= 223 and first_octet >= 192:#the elif statement will execute when the first octet is between 128 and 191
        print("This is a Class C Address")#we are printing the statement, "This is a Class C Address", if the elif statement is true
    elif first_octet <= 127 and first_octet >= 1:#the elif statement will execute when the first octet is between 1 and 127
        print("This is a Class A Address")#we are printing the statement, "This is a Class A Address", if the elif statement is true
    else: #the else statement will execute when the other if and elif statements are false
        print("That is an unrecognizable ip address!") #we are printing the statement, "That is an unrecognizable ip address!", if the other if and elif statements are false
    answer = input("Would you like to do that again[y/n]") #we are prompting the user if they want to do the loop again



     
