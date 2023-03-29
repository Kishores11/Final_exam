def temp():
    a = int(input("Enter the temperature:"))
    print("\n1.Enter 'C' to convert from Celsius to Fahrenheit \n2.Enter 'F' to convert from Celsius to Fahrenheit")
    ch = input("Enter your choice:")
    if ch == 'C':
        result = (a*1.8) - 32
        ans = round(result,2)
        return f"{a} Celsius is {ans} Fahrenheit"
    elif ch == 'F':
        result = (a*1.8) + 32
        ans = round(result,2)
        return f"{a} Fahrenheit is {ans} Celsius"
    
message = temp()
print(message)

