from scipy.spatial import distance  #for euclidian distance
from pprint import pprint

def intersect(dataSet, k):
  if not dataSet:   #if data set is empty then doesn't intersect
    return False
  for x in dataSet:
    if(x == k):
      return True
  return False

def leave_one_out_cross_validation(dataSet, current_set_of_features, k):
  column_array = []
  #if current set isn't empty then add each corresponding column
  #onto column_array
  if current_set_of_features:
    for i in range(len(current_set_of_features)):
      column_temp = []
      for j in range(len(dataSet)):
        column_temp.append(float(dataSet[j][current_set_of_features[i]]))
      column_array.append(column_temp)
  
  #add feature k onto column_array
  column_temp2 = []
  for x in range(len(dataSet)):
    column_temp2.append(float(dataSet[x][k]))
  column_array.append(column_temp2)
  
  points = []
  #form points from the row i.g. "[x,y,z,...,n]"
  #append to points; list of point
  for i in range(len(column_array[0])):
    points_temp = []
    for j in range(len(column_array)):
      points_temp.append(float(column_array[j][i]))
    points.append(points_temp)
  
  class_list = [] #list containing if class matches or not
  index_i = -1;
  index_j = -1;
  
  #compare each points with one another
  #find nearest neighbor for every point then check
  #if they're the same class/if it's the correct class
  for i in range(len(points)):
    shortest_distance = float('inf')
    for j in range(len(points)):
      temp_dst = distance.euclidean(points[i],points[j])
      if(shortest_distance > temp_dst and j != i):
        shortest_distance = temp_dst
        index_i = i
        index_j = j
    
    #if matches then true, else false1
    if(dataSet[index_j][0] == dataSet[index_i][0]):
      class_list.append(True)
    else:
      class_list.append(False)
    
  cnt = 0.0
  for i in range(len(class_list)):
    if(class_list[i]):
      cnt += 1
  
  return cnt
  
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
  is_Decreasing = False
  current_best_features = [];
  
  for i in range(1,len(dataSet)):
    print "On Level " + str(i) + " of the search tree:"
    feature_to_add_on_this_level = -1
    best_accuracy_so_far = 0
    for j in range(1,len(dataSet[i])):
      if not intersect(current_set_of_features, j):
        accuracy = leave_one_out_cross_validation(dataSet, current_set_of_features, j)
        if not current_set_of_features:
          print "---Using feature(s) {" + str(j) + "} accuracy is " + str(accuracy) + "%"
        else:
          print "---Using feature(s) {" + str(j) + ", " + "".join(str(current_set_of_features)) + "} accuracy is " + str(accuracy) + "%"

        if(accuracy > best_accuracy_so_far):
          best_accuracy_so_far = accuracy
          feature_to_add_on_this_level = j
          if(best_accuracy_so_far > best_best_accuracy):
            best_best_accuracy = best_accuracy_so_far
            current_best_features.append(j)

          else:
            is_Decreasing = True

    if(feature_to_add_on_this_level != -1):
      print "On level " + str(i) + ", I added feature " + str(feature_to_add_on_this_level) + " to current set.\n"
      current_set_of_features.append(feature_to_add_on_this_level)
    if(is_Decreasing):
      print "\n(Warning, Accuracy has decreased! Continuing search in case of local maxima)"
      is_Decreasing = False
      

  print(current_best_features)
  


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