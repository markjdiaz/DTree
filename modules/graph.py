import random
from ID3 import *
from operator import xor
from parse import parse
import matplotlib.pyplot as plt
import os.path
from pruning import validation_accuracy

# NOTE: these functions are just for your reference, you will NOT be graded on their output
# so you can feel free to implement them as you choose, or not implement them at all if you want
# to use an entirely different method for graphing

def get_graph_accuracy_partial(train_set, attribute_metadata, validate_set, numerical_splits_count, pct, depth):
    '''
    get_graph_accuracy_partial - Given a training set, attribute metadata, validation set, numerical splits count, and percentage,
    this function will return the validation accuracy of a specified (percentage) portion of the training setself.
    '''
    train_set_size = len(train_set)
    subset = random.sample(train_set, int(float(train_set_size*pct)/100))
    print len(subset)
    tree = ID3(subset, attribute_metadata, numerical_splits_count, depth)
    return validation_accuracy(tree,validate_set)

def get_graph_data(train_set, attribute_metadata, validate_set, numerical_splits_count, iterations, pcts, depth):
    '''
    Given a training set, attribute metadata, validation set, numerical splits count, iterations, and percentages,
    this function will return an array of the averaged graph accuracy partials based off the number of iterations.
    '''
    arr = []
    for pct in pcts:
        train_set_size = len(train_set)
        partials = []
        for i in range(0,iterations):
            #take a random sample from the train_set of size pct
            accuracy = get_graph_accuracy_partial(train_set, attribute_metadata, validate_set, numerical_splits_count, pct, depth)
            partials.append(accuracy)
        average = float(sum(partials))/len(partials)
        arr.append(average)
    return arr

# get_graph will plot the points of the results from get_graph_data and return a graph
# increment is the x-axis step size
# upper is the upper bound on test set size
# iterations is the number of times to test each size
def get_graph(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, lower, upper, increment):
    '''
    get_graph - Given a training set, attribute metadata, validation set, numerical splits count, depth, iterations, lower(range),
    upper(range), and increment, this function will graph the results from get_graph_data in reference to the drange
    percentages of the data.
    '''
    increment = 1
    iterations = 5
    upper = 5
    lower = 0

    #tree = ID3(train_set, attribute_metadata, numerical_splits_count, depth)
    pcts = []
    #starting from lower (0), add increasing percents of train_set. (e.g. 0, 5%, 10%....upper bound)
    for i in xrange(lower, 96, increment):
        if i == 0: continue
        pcts.append(i)
    accuracy_partials = get_graph_data(train_set, attribute_metadata, validate_set, numerical_splits_count, iterations, pcts, depth)
    accuracy_partials.insert(0,0)
    pcts.insert(0,0)
    #make graph using partials and pcts as x values
    #pcts = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    #accuracy_partials = [0.6, 0.7, 0.8, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
    plt.scatter(pcts,accuracy_partials) #plot the points
    plt.plot(pcts, accuracy_partials) #connect the points with lines
    plt.show()