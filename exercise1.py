print("""Enter two integer numbers,
       if their product will be less or equal to 1000;
       program will returned their product else their sum.""")
num1 = int(input("num1:"))
num2 = int(input("num2:"))
product = num1 * num2
if (num1*num2) <= 1000:
    print(product)
else: 
    print(num1 + num2)