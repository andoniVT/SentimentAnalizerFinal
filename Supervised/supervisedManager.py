#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 13/11/2014
@author: ucsp
'''
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

from Supervised.vectorModel import VectorModel as VM
from Supervised.supervisedClassifier import NaiveBayes as NB
from Supervised.supervisedClassifier import SVM 
from Supervised.supervisedClassifier import MaxEnt as ME
from Supervised.supervisedClassifier import DecisionTree as DT
from Configuration.settings import pmodelAll , pmodelPNeg , pmodelPNeu , pmodelNegNeu  
from Configuration.settings import smodelAll , smodelPNeg , smodelPNeu , smodelNegNeu
from Configuration.settings import nameCorpus , nameTFCorpus , nameVectorizer , nameTFVectorizer      
from Configuration.settings import peruvianNaiveBayes , peruvianSVM , peruvianMaxEnt , peruvianDecTree
from Configuration.settings import spanishNaiveBayes , spanishSVM , spanishMaxEnt , spanishDecTree
from Configuration.settings import pclassAll, pclassAllTF, pclassPNeg, pclassPNegTF, pclassPNeu, pclassPNeuTF, pclassNegNeu, pclassNegNeuTF
from Configuration.settings import trainSpanish , trainPeruvian , testSpanish , testPeruvian
from Utils.XmlManager import XManager as XM
import cPickle
trainPrueba = 'peruvianTest.xml'

class SupervisedManager(object):
    
    def __init__(self):
        pass 
    
    def get_Traincomments(self , domain):
        pre = XM(domain) 
        pre.get_data()
        trainAll = pre.get_information(0)
        trainPN = pre.get_information(1)
        trainPNeu = pre.get_information(2)
        trainNN = pre.get_information(3)
        return [trainAll , trainPN , trainPNeu , trainNN]
    
    def prepare_all_models(self):
        '''
         Prepare peruvian models
        '''
        domainData = self.get_Traincomments(trainPeruvian)  
        folders = [pmodelAll , pmodelPNeg , pmodelPNeu , pmodelNegNeu]  
        names = [nameVectorizer , nameCorpus , nameTFVectorizer , nameTFCorpus]                
        for i in range(len(domainData)):
            print domainData[i][0]
            model = VM(domainData[i][0])
            allmodels = model.prepare_models()                                     
            for j in range(len(allmodels)):                
                print folders[i] + names[j]
                with open(folders[i] + names[j] , 'wb') as fid:
                    cPickle.dump(allmodels[j] , fid)
        
        '''
        Prepare spanish models
        '''        
        domainData = self.get_Traincomments(trainSpanish)   
        folders = [smodelAll , smodelPNeg , smodelPNeu , smodelNegNeu]  
        names = [nameVectorizer , nameCorpus , nameTFVectorizer , nameTFCorpus]                
        for i in range(len(domainData)):
            model = VM(domainData[i][0])
            allmodels = model.prepare_models()                                      
            for j in range(len(allmodels)):                
                with open(folders[i] + names[j] , 'wb') as fid:
                    cPickle.dump(allmodels[j] , fid)
                                              
    def prepare_all_classifiers(self):
        '''
          Training peruvian classifiers
        '''
        domainData = self.get_Traincomments(trainPeruvian)        
        model_folders = [pmodelAll , pmodelPNeg , pmodelPNeu , pmodelNegNeu]  
        model_names = [nameCorpus ,  nameTFCorpus]        
        class_names = [pclassAll, pclassAllTF, pclassPNeg, pclassPNegTF, pclassPNeu, pclassPNeuTF, pclassNegNeu, pclassNegNeuTF]        
        name_index = 0
        for i in range(len(domainData)):
            labels = domainData[i][1]            
            for j in range(len(model_names)):
                with open(model_folders[i] + model_names[j] , 'rb') as fid:
                     corpus_load = cPickle.load(fid)                                
                classifier = SVM(corpus_load , labels)
                trained = classifier.train()
                classifier2 = NB(corpus_load , labels)
                trained2 = classifier2.train()                
                classifier3 = ME(corpus_load, labels)
                trained3 = classifier3.train()                
                classifier4 = DT(corpus_load , labels)
                trained4 = classifier4.train()                                 
                with open(peruvianSVM + class_names[name_index] , 'wb') as fid:
                    cPickle.dump(trained , fid)                
                with open(peruvianNaiveBayes + class_names[name_index] , 'wb') as fid:
                    cPickle.dump(trained2 , fid)                
                with open(peruvianMaxEnt + class_names[name_index] , 'wb') as fid:
                    cPickle.dump(trained3 , fid)                
                with open(peruvianDecTree + class_names[name_index] , 'wb') as fid:
                    cPickle.dump(trained4 , fid)                                                                    
                name_index+=1
        '''
          Training spanish classifiers
        '''                
        domainData = self.get_Traincomments(trainSpanish)        
        model_folders = [smodelAll , smodelPNeg , smodelPNeu , smodelNegNeu]  
        model_names = [nameCorpus ,  nameTFCorpus]        
        class_names = [pclassAll, pclassAllTF, pclassPNeg, pclassPNegTF, pclassPNeu, pclassPNeuTF, pclassNegNeu, pclassNegNeuTF]        
        name_index = 0
        for i in range(len(domainData)):
            labels = domainData[i][1]            
            for j in range(len(model_names)):
                with open(model_folders[i] + model_names[j] , 'rb') as fid:
                     corpus_load = cPickle.load(fid)                                
                classifier = SVM(corpus_load , labels)
                trained = classifier.train()
                classifier2 = NB(corpus_load , labels)
                trained2 = classifier2.train()                
                classifier3 = ME(corpus_load, labels)
                trained3 = classifier3.train()                
                classifier4 = DT(corpus_load , labels)
                trained4 = classifier4.train()                                 
                with open(spanishSVM + class_names[name_index] , 'wb') as fid:
                    cPickle.dump(trained , fid)                
                with open(spanishNaiveBayes + class_names[name_index] , 'wb') as fid:
                    cPickle.dump(trained2 , fid)                
                with open(spanishMaxEnt + class_names[name_index] , 'wb') as fid:
                    cPickle.dump(trained3 , fid)                
                with open(spanishDecTree + class_names[name_index] , 'wb') as fid:
                    cPickle.dump(trained4 , fid)                                                                    
                name_index+=1
                    
    def load_classifier(self , domain , type , ctype):
        if domain == 1:
            print "Peruvian Classifier" 
            if type == 1:
                print "SVM"
                if ctype == 1:
                    print "PNN classifier"                    
                    location = peruvianSVM + pclassAll
                    print location
                elif ctype == 2:
                    print "PNN TF classifier"
                    location = peruvianSVM + pclassAllTF
                    print location                    
                elif ctype == 3:
                    print "PNeg classifier"
                    location = peruvianSVM + pclassPNeg
                    print location                    
                elif ctype == 4:
                    print "PNeg TF classifier"
                    location = peruvianSVM + pclassPNegTF
                    print location                     
                elif ctype == 5:
                    print "PNeu classifier"
                    location = peruvianSVM + pclassPNeu
                    print location                     
                elif ctype == 6:
                    print "PNeu TF classifier"
                    location = peruvianSVM + pclassPNeuTF
                    print location                     
                elif ctype == 7:
                    print "NegNeu classifier"
                    location = peruvianSVM + pclassNegNeu
                    print location                     
                elif ctype == 8:
                    print "NegNeu TF classifier"
                    location = peruvianSVM + pclassNegNeuTF
                    print location                    
            elif type == 2:
                print "Naive Bayes"
                if ctype == 1:
                    print "PNN classifier"                    
                    location = peruvianNaiveBayes + pclassAll
                    print location
                elif ctype == 2:
                    print "PNN TF classifier"
                    location = peruvianNaiveBayes + pclassAllTF
                    print location                    
                elif ctype == 3:
                    print "PNeg classifier"
                    location = peruvianNaiveBayes + pclassPNeg
                    print location                    
                elif ctype == 4:
                    print "PNeg TF classifier"
                    location = peruvianNaiveBayes + pclassPNegTF
                    print location                     
                elif ctype == 5:
                    print "PNeu classifier"
                    location = peruvianNaiveBayes + pclassPNeu
                    print location                     
                elif ctype == 6:
                    print "PNeu TF classifier"
                    location = peruvianNaiveBayes + pclassPNeuTF
                    print location                     
                elif ctype == 7:
                    print "NegNeu classifier"
                    location = peruvianNaiveBayes + pclassNegNeu
                    print location                     
                elif ctype == 8:
                    print "NegNeu TF classifier"
                    location = peruvianNaiveBayes + pclassNegNeuTF
                    print location
            elif type == 3:
                print "Max Entropy"
                if ctype == 1:
                    print "PNN classifier"                    
                    location = peruvianMaxEnt + pclassAll
                    print location
                elif ctype == 2:
                    print "PNN TF classifier"
                    location = peruvianMaxEnt + pclassAllTF
                    print location                    
                elif ctype == 3:
                    print "PNeg classifier"
                    location = peruvianMaxEnt + pclassPNeg
                    print location                    
                elif ctype == 4:
                    print "PNeg TF classifier"
                    location = peruvianMaxEnt + pclassPNegTF
                    print location                     
                elif ctype == 5:
                    print "PNeu classifier"
                    location = peruvianMaxEnt + pclassPNeu
                    print location                     
                elif ctype == 6:
                    print "PNeu TF classifier"
                    location = peruvianMaxEnt + pclassPNeuTF
                    print location                     
                elif ctype == 7:
                    print "NegNeu classifier"
                    location = peruvianMaxEnt + pclassNegNeu
                    print location                     
                elif ctype == 8:
                    print "NegNeu TF classifier"
                    location = peruvianMaxEnt + pclassNegNeuTF
                    print location
            elif type == 4:
                print "Decision Tree"
                if ctype == 1:
                    print "PNN classifier"                    
                    location = peruvianDecTree + pclassAll
                    print location
                elif ctype == 2:
                    print "PNN TF classifier"
                    location = peruvianDecTree + pclassAllTF
                    print location                    
                elif ctype == 3:
                    print "PNeg classifier"
                    location = peruvianDecTree + pclassPNeg
                    print location                    
                elif ctype == 4:
                    print "PNeg TF classifier"
                    location = peruvianDecTree + pclassPNegTF
                    print location                     
                elif ctype == 5:
                    print "PNeu classifier"
                    location = peruvianDecTree + pclassPNeu
                    print location                     
                elif ctype == 6:
                    print "PNeu TF classifier"
                    location = peruvianDecTree + pclassPNeuTF
                    print location                     
                elif ctype == 7:
                    print "NegNeu classifier"
                    location = peruvianDecTree + pclassNegNeu
                    print location                     
                elif ctype == 8:
                    print "NegNeu TF classifier"
                    location = peruvianDecTree + pclassNegNeuTF
                    print location
        else:
            print "Spanish Classifier"
            if type == 1:
                print "SVM"
                if ctype == 1:
                    print "PNN classifier"                    
                    location = spanishSVM + pclassAll
                    print location
                elif ctype == 2:
                    print "PNN TF classifier"
                    location = spanishSVM + pclassAllTF
                    print location                    
                elif ctype == 3:
                    print "PNeg classifier"
                    location = spanishSVM + pclassPNeg
                    print location                    
                elif ctype == 4:
                    print "PNeg TF classifier"
                    location = spanishSVM + pclassPNegTF
                    print location                     
                elif ctype == 5:
                    print "PNeu classifier"
                    location = spanishSVM + pclassPNeu
                    print location                     
                elif ctype == 6:
                    print "PNeu TF classifier"
                    location = spanishSVM + pclassPNeuTF
                    print location                     
                elif ctype == 7:
                    print "NegNeu classifier"
                    location = spanishSVM + pclassNegNeu
                    print location                     
                elif ctype == 8:
                    print "NegNeu TF classifier"
                    location = spanishSVM + pclassNegNeuTF
                    print location                    
            elif type == 2:
                print "Naive Bayes"
                if ctype == 1:
                    print "PNN classifier"                    
                    location = spanishNaiveBayes + pclassAll
                    print location
                elif ctype == 2:
                    print "PNN TF classifier"
                    location = spanishNaiveBayes + pclassAllTF
                    print location                    
                elif ctype == 3:
                    print "PNeg classifier"
                    location = spanishNaiveBayes + pclassPNeg
                    print location                    
                elif ctype == 4:
                    print "PNeg TF classifier"
                    location = spanishNaiveBayes + pclassPNegTF
                    print location                     
                elif ctype == 5:
                    print "PNeu classifier"
                    location = spanishNaiveBayes + pclassPNeu
                    print location                     
                elif ctype == 6:
                    print "PNeu TF classifier"
                    location = spanishNaiveBayes + pclassPNeuTF
                    print location                     
                elif ctype == 7:
                    print "NegNeu classifier"
                    location = spanishNaiveBayes + pclassNegNeu
                    print location                     
                elif ctype == 8:
                    print "NegNeu TF classifier"
                    location = spanishNaiveBayes + pclassNegNeuTF
                    print location
            elif type == 3:
                print "Max Entropy"
                if ctype == 1:
                    print "PNN classifier"                    
                    location = spanishMaxEnt + pclassAll
                    print location
                elif ctype == 2:
                    print "PNN TF classifier"
                    location = spanishMaxEnt + pclassAllTF
                    print location                    
                elif ctype == 3:
                    print "PNeg classifier"
                    location = spanishMaxEnt + pclassPNeg
                    print location                    
                elif ctype == 4:
                    print "PNeg TF classifier"
                    location = spanishMaxEnt + pclassPNegTF
                    print location                     
                elif ctype == 5:
                    print "PNeu classifier"
                    location = spanishMaxEnt + pclassPNeu
                    print location                     
                elif ctype == 6:
                    print "PNeu TF classifier"
                    location = spanishMaxEnt + pclassPNeuTF
                    print location                     
                elif ctype == 7:
                    print "NegNeu classifier"
                    location = spanishMaxEnt + pclassNegNeu
                    print location                     
                elif ctype == 8:
                    print "NegNeu TF classifier"
                    location = spanishMaxEnt + pclassNegNeuTF
                    print location
            elif type == 4:
                print "Decision Tree"
                if ctype == 1:
                    print "PNN classifier"                    
                    location = spanishDecTree + pclassAll
                    print location
                elif ctype == 2:
                    print "PNN TF classifier"
                    location = spanishDecTree + pclassAllTF
                    print location                    
                elif ctype == 3:
                    print "PNeg classifier"
                    location = spanishDecTree + pclassPNeg
                    print location                    
                elif ctype == 4:
                    print "PNeg TF classifier"
                    location = spanishDecTree + pclassPNegTF
                    print location                     
                elif ctype == 5:
                    print "PNeu classifier"
                    location = spanishDecTree + pclassPNeu
                    print location                     
                elif ctype == 6:
                    print "PNeu TF classifier"
                    location = spanishDecTree + pclassPNeuTF
                    print location 
                elif ctype == 7:
                    print "NegNeu classifier"
                    location = spanishDecTree + pclassNegNeu
                    print location          
                elif ctype == 8:
                    print "NegNeu TF classifier"
                    location = spanishDecTree + pclassNegNeuTF
                    print location        
        with open(location , 'rb') as fid:
            clf_load = cPickle.load(fid)  
        return clf_load  
    
    def get_data_test_peruvian(self):
        testData = self.get_Traincomments(testPeruvian)
        comments = [testData[0][0] , testData[1][0] , testData[2][0] , testData[3][0]]
        labels = [testData[0][1] , testData[1][1] , testData[2][1] , testData[3][1]]        
        commentsModeled = []        
        folders = [pmodelAll , pmodelPNeg , pmodelPNeu , pmodelNegNeu]  
        names = [nameVectorizer, nameTFVectorizer]                
        for i in range(len(folders)):
            loaded = []
            for j in range(len(names)):
                location = folders[i] + names[j]
                print location
                with open(location , 'rb') as fid:
                    modelLoaded = cPickle.load(fid)
                loaded.append(modelLoaded)
            model = VM()
            model.set_models(loaded[0], loaded[1])            
            modelSimple = model.get_comment_frequency_vector(comments[i])
            modelTFIDF = model.get_comment_tf_idf_vector(comments[i])            
            vec = [modelSimple , labels[i]]
            commentsModeled.append(vec)
            vec = [modelTFIDF , labels[i]]
            commentsModeled.append(vec)           
        return commentsModeled
    
    def get_data_test_spanish(self):
        testData = self.get_Traincomments(testSpanish)
        comments = [testData[0][0] , testData[1][0] , testData[2][0] , testData[3][0]]
        labels = [testData[0][1] , testData[1][1] , testData[2][1] , testData[3][1]]        
        commentsModeled = []        
        folders = [smodelAll , smodelPNeg , smodelPNeu , smodelNegNeu]  
        names = [nameVectorizer, nameTFVectorizer]                
        for i in range(len(folders)):
            loaded = []
            for j in range(len(names)):
                location = folders[i] + names[j]
                print location
                with open(location , 'rb') as fid:
                    modelLoaded = cPickle.load(fid)
                loaded.append(modelLoaded)
            model = VM()
            model.set_models(loaded[0], loaded[1])            
            modelSimple = model.get_comment_frequency_vector(comments[i])
            modelTFIDF = model.get_comment_tf_idf_vector(comments[i])            
            vec = [modelSimple , labels[i]]
            commentsModeled.append(vec)
            vec = [modelTFIDF , labels[i]]
            commentsModeled.append(vec)           
        return commentsModeled
    
    def testClassifier(self , typeClassifier , domain):
        names =[pclassAll, pclassAllTF, pclassPNeg, pclassPNegTF, pclassPNeu, pclassPNeuTF, pclassNegNeu, pclassNegNeuTF]
        classifiersP = [peruvianSVM, peruvianNaiveBayes, peruvianMaxEnt, peruvianDecTree]
        classifiersS = [spanishSVM, spanishNaiveBayes, spanishMaxEnt, spanishDecTree]
        if domain == 1:
            dataTest = self.get_data_test_peruvian()
        else:
            dataTest = self.get_data_test_spanish()
        
        
        for i in range(1,8):
            classifier = self.load_classifier(domain, typeClassifier, i)
            if typeClassifier == 1:
                print "Analyzing Support Vector Machine"
                classifierTrained = SVM()
                classifierTrained.set_classifier(classifier)                 
            elif typeClassifier == 2:
                print "Analyzing Naive Bayes"
                classifierTrained = NB()
                classifierTrained.set_classifier(classifier)
            elif typeClassifier == 3:
                print "Analyzing Max Entropy"
                classifierTrained = ME()
                classifierTrained.set_classifier(classifier)
            elif typeClassifier == 4:
                print "Analyzing Decision Tree"
                classifierTrained = DT()
                classifierTrained.set_classifier(classifier)
                       
                    
    
if __name__ == '__main__':
    
    manager = SupervisedManager()
    #classifier_loaded = manager.load_classifier(1, 1, 1)
    #classifier = SVM()
    #classifier.set_classifier(classifier_loaded)
    #information = classifier.classify(test_data)
    #manager.prepare_all_models()
    #manager.prepare_all_classifiers()
    
    manager.testClassifier(3, 1)
    
    
    
    
     