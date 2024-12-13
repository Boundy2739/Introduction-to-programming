from Input import inputs
from processing import calculation
from output import outputs



num1= 0
num2=0
sign='+'
result = 0
num1,num2,sign = inputs(num1,num2,sign)
calculation(num1,num2,sign,result)
outputs(num1,num2,sign,result)

