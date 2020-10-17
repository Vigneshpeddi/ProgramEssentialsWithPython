#Week 3 Day 2 Vignesh Peddi Lab 3B

#This program follows the flowchart from Lab 3B

#STEP 1 OF FLOWCHART: START

#STEP 2 OF FLOWCHART: PROCESS -num, total_price-
num = 0
total_price = 0

#STEP 3 OF FLOWCHART: INPUT -continue-
continue_resp = input("Would you like to continue[Y/n]? ")

#STEP 4 OF FLOWCHART: DECISON -while loop-
while continue_resp == "Y":
    #STEP 5 OF FLOWCHART: PROCESS -num-
    num = num + 1

    #STEP 6 OF FLOWCHART: INPUT -price-
    price = float(input("What is the price? "))
    
    #STEP 7 OF FLOWCHART: PROCESS -total_price-
    total_price = total_price + price
    
    #STEP 8 OF FLOWCHART: INPUT -continue-
    continue_resp = input("Would you like to continue[Y/n]? ")

#STEP 9 OF FLOWCHART: INPUT -money-
money = float(input("How much money are you going to pay the cashier? "))

#STEP 10 OF FLOWCHART: PROCESS -change-
change = money - total_price

#STEP 11 OF FLOWCHART: OUTPUT -change, total_price-
print("The total price is: ${:.2f} ".format(total_price))
print("If you pay the cashier ${0:.2f} and your total price is ${1:.2f}, then you have a change of ${2:.2f}" .format(money, total_price, change))


