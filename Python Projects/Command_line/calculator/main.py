no1 = None
no2 = None
op = "1"
result = None
while op != '99':
    op = input("1.Add 2.Subtract 3.Divide 4.Multiply 99.Quit: ")
    op.upper()
    if op.upper() == "99" or op.upper() == 'QUIT':
        quit()
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))

    if op.upper() == "1" or op.upper() == "ADD":
        result = no1 + no2
        print(result)

    elif op.upper() == "2" or op.upper() == 'SUBTRACT':
        result = no1 - no2
        print(result)

    elif op.upper() == "3" or op.upper() == 'DIVIDE':
        result = no1 // no2
        print(result)

    elif op.upper() == "4" or op.upper() == 'MULTIPLY':
        result = no1 * no2
        print(result)
