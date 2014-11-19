'''
Created on 19/11/2014

@author: andoni
'''

from Supervised.supervisedManager import SupervisedManager as SM


def NaiveVoting(matrix):    
    positive = []
    negative = []
    neutral = []
    result = []    
    for i in range(len(matrix[0])):
        positive.append(0)
        negative.append(0)
        neutral.append(0)    
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'P':
                positive[j]+=1
            elif matrix[i][j] == 'N':
                negative[j]+=1
            elif matrix[i][j] == 'NEU':
                neutral[j]+=1      
    for i in range(len(positive)):
        if (positive[i] > negative[i]) and (positive[i]>neutral[i]):
            result.append('P')
        elif (negative[i]>positive[i]) and (negative[i]>neutral[i]):
            result.append('N')
        else:
            result.append('NEU')
    return result                                                                                                                                                        

if __name__ == '__main__':
    
    #matrix = [['P','P','NEU','N','P'],['P','N','NEU','P','P'],['N','NEU','P','P','N'],['P','P','NEU','NEU','P']]
    #NaiveVoting(matrix)
    
    
    manager = SM()
    resultSVM = manager.optimize_classifierTFIDF(1, 1)
    resultNB = manager.optimize_classifierTFIDF(2, 1)
    resultME = manager.optimize_classifierTFIDF(3, 1)
    resultDT = manager.optimize_classifierTFIDF(4, 1)
    
    print "Result SVM"
    print resultSVM[0] 
    print "Result NB"
    print resultNB[0]
    print "Result ME"
    print resultME[0]
    print "Result DT"
    print resultDT[0]
    
    
    matrix = [resultSVM[0] , resultNB[0] , resultME[0] , resultDT[0]]
    
    final_results = NaiveVoting(matrix)
    print "Final Result"
    print final_results
    
    y_true = resultSVM[1]
    
    manager.show_classificator_report(y_true, final_results)
    
    
    
    
    