#Week 5 Day 2 Lab 4B Vignesh Peddi

#This program follows the flowhcart from Lab 4B

num = 0 #we are starting the item counter at 0

total_price = 0 #we are starting the total price at 0

tax_total = 0 #we are starting the tax total at 0

subtotal = 0 #we are starting the subtotal at 0

answer = "Y" #we are defining the answer as "Y" to make the user already be in the loop

while answer == "Y": #answer must be "y" to enter loop
    price = float(input("What is the price: $")) #we are asking the user for the price

    will_tax = input("Is this item taxed [Y/n]: ") #we are asking the user if the item will be taxed

    if will_tax == "Y": #if the item is taxed, the if statement will be performed

        taxed_item =  (.07 * price) #if the item is taxed, then the program will calculate the tax of the item

    else: #if the item is not taxed the else statement will execute

        taxed_item = 0 #if the item is not taxed, then the tax of the item will be set to 0

    subtotal += price #we are calculating the subtotal by adding the existing subtotal to the new item price every time someone enters the loop

    tax_total += taxed_item #we are calculating the tax total by adding the existing tax total to the new tax amount every time someone enters the loop

    total_price = subtotal + tax_total #we are calculating the total price by adding the subtotal and the tax total

    num += 1 #we are counting the number of items by adding 1 to num everytime someone enters the loop

    answer = input("Would you like to do that again [Y/n]: ") #we are asking the user if they want to enter the loop agin, if they enter Y they will, if not they will exit the loop

print("Items: {0:.2f}" .format(num)) #we are outputing the number of times the person has entered the loop

print("Subtotal: ${0:.2f}" .format(subtotal)) #we are outputing the subtotal

print("Tax Total: ${0:.2f}" .format(tax_total)) #we are outputing the tax total

print("Final Cost: ${0:.2f}" .format(total_price)) #we are outputing the total price

money_tendered = float(input("How much money are you giving the clerk: ")) #we are asking the user for how much money they are paying the clerk

change = money_tendered - total_price #we are calculating the change the user will receive

print("Amount Due: ${0:.2f}" .format(total_price)) #we are outputing the amount due or total price

print("Amount Paid: ${0:.2f}" .format(money_tendered)) #we are outputing the money tendered or amount paid

print("Change: ${0:.2f}" .format(change)) #we are outputing the change the user will receive
 



