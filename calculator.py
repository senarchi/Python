first= input("Enter 1st number: ")
operator=input ("Enter operator (+,-,*,/,%): ")
second=input ("Enter second number: ")

first=int(first)
second=int(second)

if operator == "+":
    print(first+second)
elif operator == "-":
    print(first-second)
elif operator == "*":
    print(first*second)    
elif operator =="/":
    print(first/second)
elif operator =="%":
    print(first%second)    
else:
    print("Invalid Input")            
