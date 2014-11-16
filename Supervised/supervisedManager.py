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
                    
    def load_classifier(self):
        pass
    
if __name__ == '__main__':
    
    manager = SupervisedManager()
    #manager.prepare_all_models()
    manager.prepare_all_classifiers()
    
    '''
    data = [[1,2,3,4] , [5,2,1,4] , [6,1,4,2]]
    labels = [0 , 1, 1]    
    classifier = NB(data , labels)
    trained = classifier.train()    
    with open(peruvianNaiveBayes + "/test.pk1" , 'wb') as fid:
        cPickle.dump(trained , fid)            
    with open(peruvianNaiveBayes + "/test.pk1" , 'rb') as fid:
        clf_load = cPickle.load(fid)    
    classifier2 = NB()
    classifier2.set_classifier(clf_load)
    data = classifier2.classify([[1,5,6,8]])
    for i in data:
        print i
    
    
    
    comentarios = ['esta es una prueba' , 'yo me llamo andoni' , 'este es otro comentario' , 'esta es otra prueba']
    model = VM(comentarios)
    modelos = model.prepare_models()
    
    vectorizer = modelos[0] 
    corpus_simple_vector = modelos[1] 
    transformer = modelos[2]  
    corpus_tf_idf = modelos[3]    
    print model.get_comment_frequency_vector(["comentario de prueba"])
    print model.get_comment_tf_idf_vector(["comentario de prueba"])      
    '''
    
    
    
    
     