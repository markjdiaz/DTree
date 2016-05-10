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
        dnf_list = self._print_dnf_tree()
        result = {}
        print dnf_list
        for d in dnf_list:
            print d['class'],d['rule']
            if d['class'] in result:
                result[d['class']] = '{0} ^ ({1})'.format(result[d['class']],d['rule'])
            else:
                result[d['class']] = '({0})'.format(d['rule'])
        print result
        return result

    def _print_dnf_tree(self):
        '''
        returns the disjunct normalized form of the tree.
        '''
        dnf_list = []
        if self.label is not None:
            dnf = {'class':self.label}
            print dnf
            return [dnf]
        else:
            for i,c in enumerate(self.children):
                if self.is_nominal:
                    print c
                    temp_dnf_list = self.children[c]._print_dnf_tree()
                    for d in temp_dnf_list:
                        rule = '{0}={1}'.format(self.decision_attribute,c)
                        if 'rule' in d:
                            d['rule'] = '{0} v {1}'.format(d['rule'],rule)
                        else:
                            d['rule'] = '{0}'.format(rule)
                    
                else:
                    print c.label
                    temp_dnf_list = c._print_dnf_tree()
                    for d in temp_dnf_list:
                        print dnf_list
                        if i == 0:
                            rule = '{0}<{1}'.format(self.decision_attribute,self.splitting_value)
                        else:
                            rule = '{0}>={1}'.format(self.decision_attribute,self.splitting_value)
                        if 'rule' in d:
                            d['rule'] = '{0} v {1}'.format(d['rule'],rule)
                        else:
                            d['rule'] = '{0}'.format(rule)
                    print dnf_list
                dnf_list = dnf_list + temp_dnf_list
            return dnf_list
        pass

def dnf_test():
    n = []
    for i in xrange(5):
        n.append(Node())
    
    n[0].decision_attribute = 'A'
    n[0].is_nominal = True
    n[0].splitting_value = 0
    n[0].children = {'0':n[1],'1':n[2]}
    #n[0].children = [n[1],n[2]]
    n[0].name = 'A'
    n[1].label = 1
    n[2].decision_attribute = 'B'
    n[2].is_nominal = True
    n[2].splitting_value = 0
    n[2].children = {'0':n[3],'1':n[4]}
    #n[2].children = [n[3],n[4]]
    n[2].name = 'B'
    n[3].label = 1
    n[4].label = 0
    n[0].print_dnf_tree()

dnf_test()
