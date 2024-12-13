def outputs(num1,num2,sign,result):
    outputfile = open('modules/calculations.txt','w')
    num1 = str(num1)
    num2 = str(num2)
    sign = str(sign)
    result = str(result)

    if sign == '+':
        outputfile.write("The sum between ")
    if sign == '-':
        outputfile.write("The difference between ")
    if sign == '*':
        outputfile.write("The product between ")
    if sign == '/':
        outputfile.write("The quotient between ")
    
    outputfile.write(num1)
    outputfile.write(" and ")
    outputfile.write(num2)
    outputfile.write(" is ")
    outputfile.write(result)



    

