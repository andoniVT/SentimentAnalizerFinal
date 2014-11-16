#!/usr/bin/env python
# -*- coding: utf-8 -*- 
'''
Created on 15/11/2014

@author: andoni
'''
from Unsupervised.classifier import Classifier

if __name__ == '__main__':
    
    comment = "esto esta muy bueno"
    obj = Classifier()
    obj.classify(comment)
    sentiment = obj.get_label()
    print sentiment
