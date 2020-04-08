#A program to read the content of a text file ‘input.txt’. For each line in ‘input.txt’, the program writes a new line in a
#new text file ‘output.txt’ that computes the answer to some operation on a list of numbers.

content = open('input.txt','r')             #open text file for reading

infile = content.readlines()                #read contents of text files
content.close()                             #close text file to preserve resources

solution = open('output.txt','w+')          #open new text file for output data




for line in infile:                         # a for loop to split the lines and the operations
    currentline = line.split(":")
    currentline[1] = currentline[1][:-1]
    numberlist = currentline[1].split(",")
    intnumberlist = []
    for number in numberlist:
        intnumberlist.append (number)
            
         
    if currentline[0] == "min":        
        solution.write("The min of : " + str(intnumberlist) +" is "+ str(min(intnumberlist))+ "\n") #checks if the operation is min and calculates the min of the list of numbers
    
       
    if currentline[0] == "max" :
        solution.write("The max of : " + str(intnumberlist) +" is "+ str(max(intnumberlist))+ "\n")#checks if the operation is max and calculates the max of the list of numbers

    if currentline[0] == "avg" :
        totals = 0
        for i in intnumberlist :
            totals += int(i)
        solution.write("The avg of : " + str(intnumberlist) +" is " + str(totals / len(intnumberlist))+ "\n") #checks if the operation is avg and calculates the avg of the list of numbers   
      
    if currentline[0] == "sum":
        totals = 0
        for i in intnumberlist :
            totals += int(i)
        solution.write("The sum of : " + str(intnumberlist) +" is " + str(totals )+ "\n")#checks if the operation is sum and calculates the sum of the list of numbers


    if currentline[0] == "p90":
        ans = int(0.90 * len(intnumberlist))
        solution.write ("The 90th percentile of " + str(intnumberlist) +" is " + str(intnumberlist[ans-1])+ "\n")#checks if the operation is 90th percentile and calculates the 90th percentile of the list of numbers
        
    

  
    if currentline[0] == "p70":
        ans = int(0.70 * len(intnumberlist))
        solution.write ("The 70th percentile of " + str(intnumberlist) +" is " + str(intnumberlist[ans-1])+ "\n")#checks if the operation is 70th percentile and calculates the 70th percentile of the list of numbers
        
        
solution.close()

