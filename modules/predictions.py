import os.path
from operator import xor
from parse import *

# DOCUMENTATION
# ========================================
# this function outputs predictions for a given data set.
# NOTE this function is provided only for reference.
# You will not be graded on the details of this function, so you can change the interface if 
# you choose, or not complete this function at all if you want to use a different method for
# generating predictions.

def create_predictions(tree, predict):
    '''
    Given a tree and a url to a data_set. Create a csv with a prediction for each result
    using the classify method in node class.
    '''
    f = predict
    t = [x for x in parse(f, True)]
    t.pop()
    #print t
    [y for y in t]
    #print i
    test_outcome = [z[0] for z in y]
    tree_outcome = [tree.classify(x) for x in y]
    #print test_outcome
    #print tree_outcome
    create_predictions = open('data\predict.csv','wb')    
    for i in xrange(len(test_outcome)):
        create_predictions.write('{}, {}\n'.format(test_outcome[i],tree_outcome[i]))
    create_predictions.close()
    return