#Week 10 Day 2 Vignesh Peddi Final Exam MArch 14, 2019 SE 116C
#Functions
def amt_deductions(grosspayweekly, dependents):
    if dependents == 0:
        deductions = 0.1
    elif dependents == 1:
        deductions = 0.08
    elif dependents == 2:
        deductions = 0.06
    else:
        deductions = 0.03
    amountdeducted = grosspayweekly * deductions
    return amountdeducted
def net(grosspayweekly, amount_deducted):
    netpay = grosspayweekly - amount_deducted
    return netpay
#Base Program Code
answer = "y"
employee_count = 0
totalgrosspay = 0
totalnetpay = 0
totaldeductions = 0
while answer == "y" or answer == "Y":
    lastname = input("What is your last name: ")
    hourlyrate = float(input("What is your hourly rate: "))
    weeklyhours = float(input("How many hours do you work in a week: "))
    dependents = int(input("How many dependents do you have: "))
    grosspayweekly = hourlyrate * weeklyhours
    amount_deducted = amt_deductions(grosspayweekly, dependents)
    net_pay = net(grosspayweekly, amount_deducted)
    print(lastname,"Gross Pay: ${:3.2f} Net Pay: ${:3.2f} Amound Deducted: ${:3.2f}".format(grosspayweekly, net_pay, amount_deducted))
    employee_count += 1
    totalgrosspay += grosspayweekly
    totalnetpay += net_pay
    totaldeductions += amount_deducted
    answer = input("Would you like to enter more data[Y/n]: ")
print("Number of Employees: {:.0f} Total Gross Pay: ${:.2f} Total Net Pay: ${:.2f} Total Amount of Deductions: ${:.2f}".format(employee_count, totalgrosspay, totalnetpay, totaldeductions))



