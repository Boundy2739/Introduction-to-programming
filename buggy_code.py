"""
This code contains some bugs and some errors.  
Find them and fix them.  
When you are done the program will print a message.
Write the message at the bottom of the code before submission
"""
# there was no space between the key word def and the name of the function, the name of the function was misspelt
def extract_and_rearrange(string):
    str_1 = "".join(reversed(string[0:4].split('g'))).capitalize()
    
    #[6:13].split was misspelled
    str_2 = "".join(string[6:13].split('ro'))
    
    #the name of the variable was misspelt
    str_3 = "".join("".join(reversed(list(string[14:20]))).split(string[17]))
    str_4 = "".join(string[21:29].split(string[23:28]))

    #missing plus sign before str_4
    return str_1 + " " + str_2 + " " + str_3 + " " + str_4

#colon missing at the end of the line
def ultra_extrct_and_rearrange(string):
    first_transform = extract_and_rearrange(string)
    return first_transform

# the name of the function was misspelt  and there was an extra quotation mark
print(ultra_extrct_and_rearrange("egthb quirock nwoGrb forijmpxv"))

