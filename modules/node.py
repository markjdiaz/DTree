# DOCUMENTATION
# =====================================
# Class node attributes:
# ----------------------------
# children - a list of 2 nodes if numeric, and a dictionary (key=attribute value, value=node) if nominal.  
#            For numeric, the 0 index holds examples < the splitting_value, the 
#            index holds examples >= the splitting value
#
# label - is None if there is a decision attribute, and is the output label (0 or 1 for
#	the homework data set) if there are no other attributes
#       to split on or the data is homogenous
#
# decision_attribute - the index of the decision attribute being split on
#
# is_nominal - is the decision attribute nominal
#
# value - Ignore (not used, output class if any goes in label)
#
# splitting_value - if numeric, where to split
#
# name - name of the attribute being split on

class Node:
    def __init__(self):
        # initialize all attributes
        self.label = None
        self.decision_attribute = None
        self.is_nominal = None
        self.value = None
        self.splitting_value = None
        self.children = {}
        self.name = None

    def classify(self, instance):
        '''
        given a single observation, will return the output of the tree
        '''
        # still don't know the meaning of "label - is None if there is a decision attribute"
        # iterate until no children and return self.label
        while self:
            if bool(self.children) == False:
                return self.label
            else:
                # if an attribute is nominal or numerical
                if self.is_nominal == True:
                    #print instance
                    #get a value from dics, given an instance value on attribute
                    self = self.children.get(instance[self.decision_attribute]) 
                    #print self
                else:
                    # whether an instance value on given attribute is smaller than splitting_value
                    if instance[self.decision_attribute] < self.splitting_value:
                        self = self.children[0] #spcify index 0 -> define the value for self
                        #print self
                    else:
                        self = self.children[1]
                        #print self
        pass

    def print_tree(self, indent = 0):
        '''
        returns a string of the entire tree in human readable form
        IMPLEMENTING THIS FUNCTION IS OPTIONAL
        '''
        # Your code here
        pass


    def print_dnf_tree(self):
        '''
        returns the disjunct normalized form of the tree.
        '''
        pass