print("****Expense Tracker****")
print("Your Capital for the Month/Week")
req=float(input("Maximum Amount to be Spent-->"))
g=float(input("Total Money Spend on Grocieres-->"))
t=float(input("Total Money Spend on Travel-->"))
r=float(input("Total Money Spend on Rent-->"))
i=float(input("Total Money Spend on Internet-->"))
edu=float(input("Total Money Spend on Education-->"))
e=float(input("Total Money Spend on Electricity-->"))
o=float(input("Total Money Spend on Other Items-->"))
add=(g+t+r+i+edu+e+o)
print("Total Money Spent-->",add)
if add>=req:
    print("Your Expense is Greater than Your Desired Amount,Save More!")
else:
    print("Great Work!")
    ms=req-add
    print("Great!,You Saved-->",ms)

