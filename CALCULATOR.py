print("----CALCULATOR----")
num1=float(input("Enter your First Number:"))
operator=input("OPERATOR:")
num2=float(input("Enter your Second Number:"))
if operator=="+":
    print("RESULT:",num1+num2)
elif operator=="-":
    print("RESULT:",num1-num2)
elif operator=="*":
    print("RESULT:",num1*num1)
elif operator=="/":
    print("RESULT:",num1/num2)
else:
    print("INVALID OPERATOR!")

    


