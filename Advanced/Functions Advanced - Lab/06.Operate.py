def operate(sign, *args):
    if(sign == "+"):
        result = sum(args)
        return result

    elif(sign == "-"):
        firstNumber = args[0]

        for i in args[1:]:
            firstNumber -= i
        return firstNumber

    elif(sign == "*"):
        firstNumber = args[0]

        for i in args[1:]:
            firstNumber *= i
        return firstNumber

    elif(sign == "/"):
        firstNumber = args[0]

        for i in args[1:]:
            firstNumber /= i
        return firstNumber

        
print(operate("/", 20, 4, 5))