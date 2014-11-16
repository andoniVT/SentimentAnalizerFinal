'''
Created on 13/11/2014

@author: ucsp
'''

class SAManager(object):
    
    def __init__(self):
        pass
    
    def analyzeSuppervised(self , type=0):
        if type == 0:
            self.analyzeAllClassifiers()
        if type == 1:
            self.analyzeSVM()
        if type == 2:
            self.analyzeNB()
        if type == 3:
            self.analyzeME()
        if type == 4:
            self.analyzeDT()
            
    def analyzeUnsuppervised(self):
        pass
    
    def analyzeVotingSystem(self , type=0):
        pass
    
    
    
    
    def manage(self , typeA , stype=0):
        if typeA == 1:
            self.analyzeSuppervised(stype)
        if typeA == 2:
            self.analyzeUnsuppervised()
        if typeA == 3:
            self.analyzeVotingSystem(stype)
 
        
        
if __name__ == '__main__':
    
    print "Hello World!"
    