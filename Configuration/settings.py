'''
Created on 13/11/2014
@author: ucsp
'''

''' path  '''
path_cicc = '/home/ucsp/workspace/SentimentAnalizerFinal'
path_home ='/home/andoni/Escritorio/PythonProjets/SentimentAnalizerFinal'
path_home2 = '/home/andoni/Escritorio/PythonProjets'
#path = path_cicc
path = path_home
path_classifiers = path_home2

'''resource '''
big_text = path + '/Resource/big2.txt'
stop_words = path + '/Resource/stopwords_spanish.txt'

''' data test and training '''
trainSpanish = path + '/Data/train/spanishTrain.xml'
trainPeruvian = path + '/Data/train/peruvianTrain.xml'
testSpanish = path + '/Data/test/spanishTest.xml'
testPeruvian = path + '/Data/test/peruvianTest.xml'
prueba = path + '/Data/train/prueba.xml'

''' supervised classifiers '''
spanish_path = path_classifiers + '/DataTrained/classifierTrained/spanish'
spanishSVM = spanish_path + '/SVM'
spanishNaiveBayes = spanish_path + '/NaiveBayes'
spanishMaxEnt = spanish_path + '/MaxEnt'
spanishDecTree = spanish_path + '/DecTree'

peruvian_path = path_classifiers + '/DataTrained/classifierTrained/peruvian'
peruvianSVM = peruvian_path + '/SVM'
peruvianNaiveBayes = peruvian_path + '/NaiveBayes'
peruvianMaxEnt = peruvian_path + '/MaxEnt'
peruvianDecTree = peruvian_path + '/DecTree'
 
pclassAll = '/PNN_classifier.pk1'
pclassAllTF = '/PNN_TFclassifier.pk1'
pclassPNeg = '/PNeg_classifier.pk1'
pclassPNegTF = '/PNeg_TFclassifier.pk1'  
pclassPNeu = '/PNeu_classifier.pk1'
pclassPNeuTF = '/PNeu_TFclassifier.pk1'
pclassNegNeu = '/NegNeu_classifier.pk1'
pclassNegNeuTF = '/NegNeu_TFclassifier.pk1' 

 
spanishVectorModel = path_classifiers + '/DataTrained/vectorModel/spanish'
peruvianVectorModel = path_classifiers + '/DataTrained/vectorModel/peruvian'

pmodelAll = peruvianVectorModel + '/PosNegNeu'
pmodelPNeg = peruvianVectorModel + '/PosNeg'
pmodelPNeu = peruvianVectorModel + '/PosNeu'
pmodelNegNeu = peruvianVectorModel + '/NegNeu'

smodelAll = spanishVectorModel + '/PosNegNeu'
smodelPNeg = spanishVectorModel + '/PosNeg'
smodelPNeu = spanishVectorModel + '/PosNeu'
smodelNegNeu = spanishVectorModel + '/NegNeu'


nameCorpus = '/simpleCorpus.pk1'
nameTFCorpus = '/tfidfCorpus.pk1'
nameVectorizer = '/simpleVectorizer.pk1'
nameTFVectorizer = '/tfidfVectorizer.pk1'