'''
Created on 13/11/2014

@author: ucsp
'''
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression

class SupervisedClassifier(object):
    
    def __init__(self , data=None, labels=None):
        print "Suppervised Classifier"
        self.data = data
        self.labels = labels
        self.classifier = []
        
    def train(self):
        pass
    
    def classify(self, test_data):
        pass 
    
    def set_classifier(self , classifier):
        self.classifier = classifier
    
class NaiveBayes(SupervisedClassifier):
    
    def __init__(self , data=None , labels = None):
        SupervisedClassifier.__init__(self , data , labels)
        print " -- Naive Bayes Classifier -- "
    
    def train(self):
        super(NaiveBayes , self).train()
        classifier = MultinomialNB()
        classifier = classifier.fit(self.data, self.labels)
        return classifier
    
    def classify(self, test_data):
        super(NaiveBayes , self).classify(test_data)
        predictions = []
        for i in test_data:
            value = self.classifier.predict(i)
            predictions.append(value)
        return predictions

class SVM(SupervisedClassifier):
    
    def __init__(self , data=None , labels = None):
        SupervisedClassifier.__init__(self , data , labels)
        print " -- Support Vector Machine Classifier -- "
    
    def train(self):
        super(SVM , self).train()
        classifier = LinearSVC()
        classifier = classifier.fit(self.data, self.labels)
        return classifier
    
    def classify(self, test_data):
        super(SVM , self).classify(test_data)
        predictions = []
        for i in test_data:
            value = self.classifier.predict(i)
            predictions.append(value)
        return predictions
        
class DecisionTree(SupervisedClassifier):
    
    def __init__(self , data=None , labels = None):
        SupervisedClassifier.__init__(self , data , labels)
        print " -- Decision Tree Classifier -- "
    
    def train(self):
        super(DecisionTree , self).train()
        classifier = DecisionTreeClassifier()
        classifier = classifier.fit(self.data, self.labels)
        return classifier
    
    def classify(self, test_data):
        super(DecisionTree , self).classify(test_data)
        predictions = []
        for i in test_data:
            value = self.classifier.predict(i)
            predictions.append(value)
        return predictions  

class MaxEnt(SupervisedClassifier):
    
    def __init__(self , data=None , labels = None):
        SupervisedClassifier.__init__(self , data , labels)
        print " -- Maximum Entropy Classifier -- "
    
    def train(self):
        super(MaxEnt , self).train()
        classifier = LogisticRegression()
        classifier = classifier.fit(self.data, self.labels)
        return classifier
    
    def classify(self, test_data):
        super(MaxEnt , self).classify(test_data)
        predictions = []
        for i in test_data:
            value = self.classifier.predict(i)
            predictions.append(value)
        return predictions      
        
         
