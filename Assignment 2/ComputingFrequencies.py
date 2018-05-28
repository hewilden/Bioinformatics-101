# -*- coding: utf-8 -*-
"""
Created on Mon May 28 08:50:55 2018

@author: Helen
"""
def NumberToSymbol(x):
    '''    
    (str) -> int
    Returns corresponding number to integer  
    ''' 
    dict = {0 : 'A', 
            1 : 'C',
            2 : 'G',
            3 : 'T'}
    return dict[x]

def SymbolToNumber(x):
    '''    
    (str) -> int
    Returns corresponding number to integer  
    ''' 
    dict = {'A' : 0, 
            'C' : 1,
            'G' : 2,
            'T' : 3}
    return dict[x]

def PatternToNumber(pattern):
    if pattern == '':
        return 0
    if pattern != '':
        symbol = pattern[-1]
        prefix = pattern[:-1]
        return 4*PatternToNumber(prefix)+SymbolToNumber(symbol)
        
  
def NumberToPattern (index, k):
    '''
    '''
    if k==1:
        return NumberToSymbol(index)   
    if k>1:
        prefixIndex = index//4
        r = index % 4
        symbol = NumberToSymbol(r)
        PrefixPattern = NumberToPattern(prefixIndex, k-1) + symbol
        
    return PrefixPattern

#SymbolToNumber, NumberToSymbol, PatternToNumber and NumberToPattern are 
#implemented as in Exercise 2, 3
    
def ComputingFrequencies(Text,k):
    FrequencyArray = [0]*4**k 
    for i in range(0, len(Text)-k+1):
        pattern = Text[i:i+k]
        j = PatternToNumber(pattern)
        FrequencyArray[j]=FrequencyArray[j]+1
    return FrequencyArray