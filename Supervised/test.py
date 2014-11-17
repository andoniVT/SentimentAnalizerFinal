'''
Created on 16/11/2014

@author: andoni
'''

def evaluar(pos , neg, neu , evalPNeg , evalPNeu, evalNegNeu):
    etapa1 = [] 
    etapa2 = [] 
    etapa3 = []
    for i in range(pos + neg + neu):
        etapa1.append('NOT')
        etapa2.append('NOT')
        etapa3.append('NOT')    
    for i in range(len(evalPNeg)):
        etapa1[i] = evalPNeg[i]    
    index = 0
    for i in range(pos):
        etapa2[i] = evalPNeu[index]
        index+=1
    for i in range(pos+neg , pos+neg+neu):
        etapa2[i] = evalPNeu[index]
        index+=1    
    index = 0
    for i in range(pos, pos+neg+neu):
        etapa3[i] = evalNegNeu[index]
        index+=1      
    result = []
    for i in range(len(etapa1)):
        if (etapa1[i] == 'P' and etapa2[i] == 'P') or (etapa1[i]=='P' and etapa3[i]=='P') or (etapa2[i]=='P' and etapa3[i]=='P'):
            value = 'P'
        elif (etapa1[i] == 'N' and etapa2[i] == 'N') or (etapa1[i]=='N' and etapa3[i]=='N') or (etapa2[i]=='N' and etapa3[i]=='N'):
            value = 'N'
        else:
            value = 'NEU'
        result.append(value)
    return result                              
    
if __name__ == '__main__':
    
    y_true = []
    for i in range(6):
        y_true.append('P')
    for i in range(10):
        y_true.append('N')
    for i in range(4):
        y_true.append('NEU')
    #print y_true
    
    evalPNeg = ['P','P','N','N','P','P','P','P','N','N','N','P','N','N','N','N']        
    evalPNeu = ['P','NEU','P','NEU','P','P','NEU','NEU','NEU','P']
    evalNegNeu = ['NEU','N','N','N','N','N','NEU','N','N','N','N','NEU','NEU','N']
    
    res = evaluar(6,10 ,4 , evalPNeg, evalPNeu, evalNegNeu)
    print res
    
    
    
    
    
    