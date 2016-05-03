# coding: utf-8

import math
from node import Node
import sys

def ID3(data_set, attribute_metadata, numerical_splits_count, depth):
    '''
    See Textbook for algorithm.
    Make sure to handle unknown values, some suggested approaches were
    given in lecture.
    ========================================================================================================
    Input:  A data_set, attribute_metadata, maximum number of splits to consider for numerical attributes,
	maximum depth to search to (depth = 0 indicates that this node should output a label)
    ========================================================================================================
    Output: The node representing the decision tree learned over the given data set
    ========================================================================================================

    ID3 (Examples, Target_Attribute, Attributes)
    Create a root node for the tree
    If all examples are positive, Return the single-node tree Root, with label = +.
    If all examples are negative, Return the single-node tree Root, with label = -.
    If number of predicting attributes is empty, then Return the single node tree Root,
    with label = most common value of the target attribute in the examples.
    Otherwise Begin
        A ← The Attribute that best classifies examples.
        Decision Tree attribute for Root = A.
        For each possible value, vi, of A,
            Add a new tree branch below Root, corresponding to the test A = vi.
            Let Examples(vi) be the subset of examples that have the value vi for A
            If Examples(vi) is empty
                Then below this new branch add a leaf node with label = most common target value in the examples
            Else below this new branch add the subtree ID3 (Examples(vi), Target_Attribute, Attributes – {A})
    End
    Return Root
    '''
    # create the root node
    root = Node()
    # if the training set is hemogenous, set the root node's label to this value
    root.label = check_homogenous(dataset)
    if not root.label:
        # find the best attribute to split on
        attribute = pick_best_attribute(dataset,attribute_metadata,numerical_splits_count)
        # get the index of the decision attribute
        root.decision_attribute = attribute[0]
        root.is_nominal = attribute_metadata[root.decision_attribute]['is_nominal']
        root.splitting_value = attribute[1]
        root.name = attribute_metadata[attribute[0]]['name']
        if root.is_nominal:
            split_dataset = split_on_nominal(dataset,attribute[0])
            for example in split_dataset:
                root.children[example] = ID3(split_dataset[example],attribute_metadata,numerical_splits_count,depth)
        else:
            root.children = []
            split_dataset = split_on_numerical(dataset,attribute[0],attribute[1])
            for example in split_dataset:
                root.children.append(ID3(example,attribute_metadata,numerical_splits_count,depth))
    return root
    pass

#Jim
def check_homogenous(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Checks if the output value (index 0) is the same for all examples in the the data_set, if so return that output value, otherwise return None.
    ========================================================================================================
    Output: Return either the homogenous attribute or None
    ========================================================================================================
     '''
	index0 = [i[0] for i in data_set]
    if len(set(index0)) == 1:
        check_homogenous = 1
    else :
        check_homogenous = None
    return check_homogenous
# ======== Test Cases =============================
# data_set = [[0],[1],[1],[1],[1],[1]]
# check_homogenous(data_set) ==  None
# data_set = [[0],[1],[None],[0]]
# check_homogenous(data_set) ==  None
# data_set = [[1],[1],[1],[1],[1],[1]]
# check_homogenous(data_set) ==  1

#Mark
def pick_best_attribute(data_set, attribute_metadata, numerical_splits_count):
    '''
    ========================================================================================================
    Input:  A data_set, attribute_metadata, splits counts for numeric
    ========================================================================================================
    Job:    Find the attribute that maximizes the gain ratio. If attribute is numeric return best split value.
            If nominal, then split value is False.
            If gain ratio of all the attributes is 0, then return False, False
            Only consider numeric splits for which numerical_splits_count is greater than zero
    ========================================================================================================
    Output: best attribute, split value if numeric
    ========================================================================================================
    '''
    attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
    data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [0, 0.51], [1, 0.4]]
    numerical_splits_count = [20,20]

    best_attribute = False
    best_attribute_index = False
    max_gain = 0
    split_value = False

    for i, attribute in enumerate(attribute_metadata):
        if attribute['is_nominal'] == True:
            gain_ratio = gain_ratio_nominal(data_set, attribute)
            if gain_ratio > max_gain:
                max_gain = gain_ratio
                best_attribute = attribute
                best_attribute_index = i
                split_value = False
        elif attribute['is_nominal'] == False and numerical_splits_count[i] > 0:
            gain_ratio, attr_split_value = gain_ratio_numeric(data_set, attribute, steps=1) #HOW TO SUBSET DATA?
            if gain_ratio > max_gain:
                max_gain = gain_ratio
                best_attribute = attribute
                best_attribute_index = i
                split_value = attr_split_value
    #return (best_attribute, split_value)
    #print (best_attribute, split_value)
    return (best_attribute_index, split_value)
    #print (best_attribute, split_value) == (1, 0.51)

# # ======== Test Cases =============================
# numerical_splits_count = [20,20]
# attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
# data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [0, 0.51], [1, 0.4]]
# pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, 0.51)

# attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}]
# data_set = [[0, 0], [1, 0], [0, 2], [0, 2], [0, 3], [1, 1], [0, 4], [0, 2], [1, 2], [1, 5]]
# pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, False)

# Uses gain_ratio_nominal or gain_ratio_numeric to calculate gain ratio.

#Kyosuke
def mode(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Takes a data_set and finds mode of index 0.
    ========================================================================================================
    Output: mode of index 0.
    ========================================================================================================
    '''
    # Your code here
    mode_set = [i[0] for i in data_set]
    mode = max(set(mode_set), key=mode_set.count)
    return mode
    pass
    
# ======== Test case =============================
# data_set = [[0],[1],[1],[1],[1],[1]]
# mode(data_set) == 1
# data_set = [[0],[1],[0],[0]]
# mode(data_set) == 0

#Jim
def entropy(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Calculates the entropy of the attribute at the 0th index, the value we want to predict.
    ========================================================================================================
    Output: Returns entropy. See Textbook for formula
    ========================================================================================================
    '''
    index0 = [i[0] for i in data_set]
    t = len(index0) # total num of instances
    entropy = 0.0
    for i in set(index0):
        entropy += -(index0.count(i)/float(t))*math.log(index0.count(i)/float(t), 2)
    return entropy
    pass

# ======== Test case =============================
# data_set = [[0],[1],[1],[1],[0],[1],[1],[1]]
# entropy(data_set) == 0.811
# data_set = [[0],[0],[1],[1],[0],[1],[1],[0]]
# entropy(data_set) == 1.0
# data_set = [[0],[0],[0],[0],[0],[0],[0],[0]]
# entropy(data_set) == 0

#Kyosuke
def gain_ratio_nominal(data_set, attribute):
    '''
    ========================================================================================================
    Input:  Subset of data_set, index for a nominal attribute
    ========================================================================================================
    Job:    Finds the gain ratio of a nominal attribute in relation to the variable we are training on.
    ========================================================================================================
    Output: Returns gain_ratio. See https://en.wikipedia.org/wiki/Information_gain_ratio
    ========================================================================================================
    '''
    # Your code here
    index0 = [i[0] for i in data_set]
    index1 = [i[1] for i in data_set]
#    child_instances = []
#    for i in index1:
#        child_instances.append(i)
    
    t = len(index0) # total num of instances
    avg_entropy_children = 0.0
    for j in set(index1):
        avg_entropy_children += (index1.count(j)*entropy([[v[0]] for i,v in enumerate(data_set) if v[1]==j])/float(t))
    
    #information gain
    IG = entropy([[i] for i in index0]) - avg_entropy_children
    #print IG
    #intrinsic value
    IV = 0.0
    for k in set(index1):
        IV += -(index1.count(k)/float(t))*math.log(index1.count(k)/float(t), 2)
    #print IV
    gain_ratio_nominal = IG/IV
    return gain_ratio_nominal
    pass
# ======== Test case =============================
# data_set, attr = [[1, 2], [1, 0], [1, 0], [0, 2], [0, 2], [0, 0], [1, 3], [0, 4], [0, 3], [1, 1]], 1
# gain_ratio_nominal(data_set,attr) == 0.11470666361703151
# data_set, attr = [[1, 2], [1, 2], [0, 4], [0, 0], [0, 1], [0, 3], [0, 0], [0, 0], [0, 4], [0, 2]], 1
# gain_ratio_nominal(data_set,attr) == 0.2056423328155741
# data_set, attr = [[0, 3], [0, 3], [0, 3], [0, 4], [0, 4], [0, 4], [0, 0], [0, 2], [1, 4], [0, 4]], 1
# gain_ratio_nominal(data_set,attr) == 0.06409559743967516

#Kyosuke
def gain_ratio_numeric(data_set, attribute, steps):
    '''
    ========================================================================================================
    Input:  Subset of data set, the index for a numeric attribute, and a step size for normalizing the data.
    ========================================================================================================
    Job:    Calculate the gain_ratio_numeric and find the best single threshold value
            The threshold will be used to split examples into two sets
                 those with attribute value GREATER THAN OR EQUAL TO threshold
                 those with attribute value LESS THAN threshold
            Use the equation here: https://en.wikipedia.org/wiki/Information_gain_ratio
            And restrict your search for possible thresholds to examples with array index mod(step) == 0
    ========================================================================================================
    Output: This function returns the gain ratio and threshold value
    ========================================================================================================
    '''
    # Your code here
    index0 = [i[0] for i in data_set]
    index1 = [i[1] for i in data_set]
    
    t = len(index0) # total num of instances
    avg_entropy_children = 0.0
    
    #replace value... based on threshold
    #and make a new dataset combining a new index1 
    num_index1 = [1 if index1[i] >= index1[steps] else 0 for i,v in enumerate(index1)]
    data_set2 = [[index0[i], num_index1[i]] for i in range(len(index0))]    
    
    for j in set(num_index1):
        avg_entropy_children += (num_index1.count(j)*entropy([[v[0]] for i,v in enumerate(data_set2) if v[1]==j])/float(t))
        
    #information gain
    IG = entropy([[i] for i in index0]) - avg_entropy_children
    #print IG
    #intrinsic value
    IV = 0.0
    for k in set(num_index1):
        IV += -(num_index1.count(k)/float(t))*math.log(num_index1.count(k)/float(t), 2)
    #print IV
    gain_ratio_numeric = IG/IV
    return (gain_ratio_numeric, index1[steps])
    pass
# ======== Test case =============================
# data_set,attr,step = [[1,0.05], [1,0.17], [1,0.64], [0,0.38], [1,0.19], [1,0.68], [1,0.69], [1,0.17], [1,0.4], [0,0.53]], 1, 2
# gain_ratio_numeric(data_set,attr,step) == (0.31918053332474033, 0.64) <- something wrong here
# data_set,attr,step = [[1, 0.35], [1, 0.24], [0, 0.67], [0, 0.36], [1, 0.94], [1, 0.4], [1, 0.15], [0, 0.1], [1, 0.61], [1, 0.17]], 1, 4
# gain_ratio_numeric(data_set,attr,step) == (0.11689800358692547, 0.94)
# data_set,attr,step = [[1, 0.1], [0, 0.29], [1, 0.03], [0, 0.47], [1, 0.25], [1, 0.12], [1, 0.67], [1, 0.73], [1, 0.85], [1, 0.25]], 1, 1
# gain_ratio_numeric(data_set,attr,step) == (0.23645279766002802, 0.29)


#Mark
def split_on_nominal(data_set, attribute):
    '''
    ========================================================================================================
    Input:  subset of data set, the index for a nominal attribute.
    ========================================================================================================
    Job:    Creates a dictionary of all values of the attribute.
    ========================================================================================================
    Output: Dictionary of all values pointing to a list of all the data with that attribute
    ========================================================================================================
    '''
    data_set, attribute = [[0, 4], [1, 3], [1, 2], [0, 0], [0, 0], [0, 4], [1, 4], [0, 2], [1, 2], [0, 1]], 1

    dictionary = {}

    for data in data_set:
        attr_value = data[attribute]
        if attr_value in dictionary:
        #if the attribute value is already in the dictionary, add the data point to the dictionary value list list
            dp_list = dictionary[attr_value]
            dp_list.append(data)
            dictionary[attr_value] = dp_list
        else:
            #if the attribute value is not in the dictionary, add it and set the value to a list containing the data point
            dictionary[attr_value] = [data]
        #key = attr_value, value = all data points with that value
    #print dictionary == {0: [[0, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3]], 4: [[0, 4], [0, 4], [1, 4]]}
    return dictionary

# ======== Test case =============================
# data_set, attr = [[0, 4], [1, 3], [1, 2], [0, 0], [0, 0], [0, 4], [1, 4], [0, 2], [1, 2], [0, 1]], 1
# split_on_nominal(data_set, attr) == {0: [[0, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3]], 4: [[0, 4], [0, 4], [1, 4]]}

# data_set, attr = [[1, 2], [1, 0], [0, 0], [1, 3], [0, 2], [0, 3], [0, 4], [0, 4], [1, 2], [0, 1]], 1
# split on_nominal(data_set, attr) == {0: [[1, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3], [0, 3]], 4: [[0, 4], [0, 4]]}

#Mark
def split_on_numerical(data_set, attribute, splitting_value):
    '''
    ========================================================================================================
    Input:  Subset of data set, the index for a numeric attribute, threshold (splitting) value
    ========================================================================================================
    Job:    Splits data_set into a tuple of two lists, the first list contains the examples where the given
	attribute has value less than the splitting value, the second list contains the other examples
    ========================================================================================================
    Output: Tuple of two lists as described above
    ========================================================================================================
    '''
    data_set,attribute,splitting_value = [[1, 0.25], [1, 0.89], [0, 0.93], [0, 0.48], [1, 0.19], [1, 0.49], [0, 0.6], [0, 0.6], [1, 0.34], [1, 0.19]],1,0.48

    lower_value = []
    other_values = []
    
    for data in data_set:
        attr_value = data[attribute]
        if attr_value < splitting_value:
            lower_value.append(data)
        else:
            other_values.append(data)
    #print (lower_value, other_values) == ([[1, 0.25], [1, 0.19], [1, 0.34], [1, 0.19]],[[1, 0.89], [0, 0.93], [0, 0.48], [1, 0.49], [0, 0.6], [0, 0.6]])
    return (lower_value, other_values) 

# ======== Test case =============================
# d_set,a,sval = [[1, 0.25], [1, 0.89], [0, 0.93], [0, 0.48], [1, 0.19], [1, 0.49], [0, 0.6], [0, 0.6], [1, 0.34], [1, 0.19]],1,0.48
# split_on_numerical(d_set,a,sval) == ([[1, 0.25], [1, 0.19], [1, 0.34], [1, 0.19]],[[1, 0.89], [0, 0.93], [0, 0.48], [1, 0.49], [0, 0.6], [0, 0.6]])

# d_set,a,sval = [[0, 0.91], [0, 0.84], [1, 0.82], [1, 0.07], [0, 0.82],[0, 0.59], [0, 0.87], [0, 0.17], [1, 0.05], [1, 0.76]],1,0.17
# split_on_numerical(d_set,a,sval) == ([[1, 0.07], [1, 0.05]],[[0, 0.91],[0, 0.84], [1, 0.82], [0, 0.82], [0, 0.59], [0, 0.87], [0, 0.17], [1, 0.76]])
