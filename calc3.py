num1 = float(input("Enter the no.1 : "))
num2 = float(input("Enter the no.2 : "))
operator = input("Enter the Operation : ")
if operator =='+':
    print(num1+num2)
elif operator =='_':
    print(num1-num2)
elif operator =='*':
        print(num1*num2)
elif operator =='/':
    print(num1/num2)
elif operator =='%':
    print(num1/num2)
else:
    print('Invalid Operator')

