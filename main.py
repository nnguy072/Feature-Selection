import random #for now
from scipy.spatial import distance
from pprint import pprint

def intersect(dataSet, k):
  if not dataSet:   #if data set is empty then doesn't intersect
    return False
  for x in dataSet:
    if(x == k):
      return True
  return False

def leave_one_out_cross_validation(dataSet, current_set_of_features, k):
  column = [] #column in dataSet
  for x in range(len(dataSet)):
    column.append(dataSet[x][k])
  
  for i in range(len(column)):
    for j in range(len(column)):
      distance.euclidian(column[i], column[j])
  
  return 0
    
#read in from file "data.txt" and store content into 2d list
def populateDataSet(fileName):
  file = open(fileName, "r")    #open file
  temp = file.readlines()        #read line by line
  temp1 = []                      #what 2d list with numbers
  for line in temp:               #split each line and store into temp1
    temp1.append(line.split())
  return temp1

def forwardSelection(dataSet):
  current_set_of_features = [];
  best_best_accuracy = 0;

  for i in range(1,len(dataSet) + 1):
    print "On Level " + str(i) + " of the search tree:"
    feature_to_add_on_this_level = -1
    best_accuracy_so_far = 0
    for j in range(1, len(dataSet[0])):
      if not intersect(current_set_of_features, j):
        accuracy = leave_one_out_cross_validation(dataSet, current_set_of_features, j)
        if not current_set_of_features:
          print "\tUsing feature(s) {" + str(j) + "} accuracy is " + str(accuracy) + "%"
        else:
          print "\tUsing feature(s) {" + str(j) + ", " + "".join(str(current_set_of_features)) + "} accuracy is " + str(accuracy) + "%"

        if(accuracy > best_accuracy_so_far):
          best_accuracy_so_far = accuracy
          feature_to_add_on_this_level = j

    if(best_accuracy_so_far >= best_best_accuracy):
      best_best_accuracy = best_best_accuracy
    else:
      print "\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)"
      current_set_of_features_temp = current_set_of_features

    if(feature_to_add_on_this_level != -1):
      print "On level " + str(i) + ", I added feature " + str(feature_to_add_on_this_level) + " to current set.\n"
      current_set_of_features.append(feature_to_add_on_this_level)

  pprint(current_set_of_features)


def backwardElimination():
  print "I am backward elimination"

def myAlgorithm():
  print "I don't know what I am yet"

#program starts here
print "Welcome to Nam Nguyen's Feature Selection Algorithm."
#fileName = raw_input("Type in the name of the file to test: ")
smallSet = "small.txt"
bigSet = "big.txt"
dataSet = populateDataSet(smallSet)

print """Choose which algorithm to run:
1) Forward Selection
2) Backward Elimination
3) Nam's Special Algorithm"""

forwardSelection(dataSet)

'''
algorithm_input = raw_input("I want to run algorithm #")
if(algorithm_input == "1"):
forwardSelection()
elif(algorithm_input == "2"):
backwardElimination()
elif(algorithm_input == "3"):
myAlgorithm()
else:
print "Dude...just choose 1, 2, or 3 like a normal person"
'''