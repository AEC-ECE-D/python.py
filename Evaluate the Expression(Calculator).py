from sys import exit
def is_number(item):
    try:
        int(item)
        return True
    except ValueError:
        return False
def set_up_list():
    astring = input()
    astring = astring.replace(" ", "")
    for item in astring:
        if item not in ["0", "1", "2", "3" , "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ".", "(", ")"]:
            print ("Unsupported Character: " + item)
            exit()
    a_list = []
    for item in astring:
        a_list.append(item)
    count = 0
    while count < len(a_list) - 1:
        if is_number(a_list[count]) and a_list[count + 1] == "(":
            print ("Program does not accept parentheses directly after number, must have operator in between.")
            exit()
        if is_number(a_list[count]) and is_number(a_list[count + 1]):
            a_list[count] += a_list[count + 1]
            del a_list[count + 1]
        elif is_number(a_list[count]) and a_list[count + 1] == ".":
            try:
                x = a_list[count+2]
            except IndexError:
                print ("Your formatting is off somehow.")
                exit()
            if is_number(a_list[count + 2]):
                a_list[count] += a_list[count + 1] + a_list[count + 2]
                del a_list[count + 2]
                del a_list[count + 1]
        else:
            count += 1
    return a_list
def perform_operation(n1, operand, n2):
    if operand == "+":
        return str(int(n1) + int(n2))
    elif operand == "-":
        return str(int(n1) - int(n2))
    elif operand == "*":
        return str(int(n1) * int(n2))
    elif operand == "/":
        try:
            n = str(int(n1) / int(n2))
            return n
        except ZeroDivisionError:
            print ("You tried to divide by 0.")
            print ("Just for that I am going to terminate myself")
            exit()
expression = set_up_list()
emergency_count = 0
P = ["(", ")"]
while len(expression) != 1:
    count = 0
    while count < len(expression) - 1:
        if expression[count] == "(":
            if expression[count + 2] == ")":
                del expression[count + 2]
                del expression[count]
        count += 1
    count = 0
    while count < len(expression) - 1:
        if expression[count] in ["*", "/"] and not (expression[count+1] in P or expression[count-1] in P):
            expression[count - 1] = perform_operation(expression[count - 1], expression[count], expression[count + 1])
            del expression[count + 1]
            del expression[count]
        count += 1
    count = 0
    while count < len(expression) - 1:
        if expression[count] in ["+", "-"] and not (expression[count+1] in P or expression[count-1] in P):
            expression[count - 1] = perform_operation(expression[count - 1], expression[count], expression[count + 1])
            del expression[count + 1]
            del expression[count]
        count += 1
    emergency_count += 1
    if emergency_count >= 1000:
        print ("Operation was too long or was bugged")
        exit()
print (int(expression[0]))
