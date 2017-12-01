#read in from file "data.txt" and store content into 2d list
def populateDataSet(fileName):
    file = open(fileName, "r")    #open file
    temp = file.readlines();        #read line by line
    temp1 = []                      #what 2d list with numbers
    for line in temp:               #split each line and store into temp1
        temp1.append(line.split())
    return temp1

def forwardSelection():
    print "I am forward selection"
    
def backwardElimination():
    print "I am backward elimination"

def myAlgorithm():
    print "I don't know what I am yet"

print "Welcome to Nam Nguyen's Feature Selection Algorithm."
fileName = raw_input("Type in the name of the file to test: ")
dataSet = populateDataSet(fileName)
print dataSet[1][2]

print """Choose which algorithm to run:
    1) Forward Selection
    2) Backward Elimination
    3) Nam's Special Algorithm"""
algorithm_input = raw_input("I want to run algorithm #")
if(algorithm_input == "1"):
    forwardSelection()
elif(algorithm_input == "2"):
    backwardElimination()
elif(algorithm_input == "3"):
    myAlgorithm()
else:
    print "Dude...just choose 1, 2, or 3 like a normal person"