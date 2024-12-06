def grade(average,valutation):
    
    if average > 85:
        return "Distinction"
    if average > 69:
        return "Merit"
inputfile = open('input.txt','r')

inputfile = inputfile.readlines()
outputfile = open('output.txt','w')
marka = 0
average = 0
i = 0
for lines in inputfile:
    name,subject,mark,weight = lines.strip().split(',')
    
    

    mark = float(mark)
    weight = float(weight)
    
    marka = mark + marka
    average = marka / 3 
    
    
    
    if i == 2:
        valutation = "none"
         
        valutation = grade(average, valutation)
        average = str(average)
        outputfile.write(name)
        outputfile.write(',')
        outputfile.write(average)
        outputfile.write(',')
        outputfile.write(valutation)
        outputfile.write('\n')
    i = i + 1
    


outputfile.close()   


