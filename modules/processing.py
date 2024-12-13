def calculation(num1,num2,sign,result):
    if sign =='+':
        result = 0
        sum = num1 + num2
        return [num1,num2,sign,sum]
    if sign =='-':
        result = num1 - num2
        return num1,num2,sign,result
    if sign =='*':
        result = num1 * num2
        return num1,num2,sign,result
    if sign =='/':
        result = num1 / num2
        return num1,num2,sign,result
    
        
        
    
