number = int(input("Insert a number"))
factor = 1
result  = number * factor

#while factor < 7:
    #print(number,":",result)
    #factor = factor + 1
    #number = number + 1
    #result = result * factor
while factor < number:

    factor = factor + 1
    result = result * factor
    if factor == number - 1:
        print(number,":",result)