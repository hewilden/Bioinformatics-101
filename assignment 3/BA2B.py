# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:24:42 2018

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

def NumberToPattern (index, k):
    '''
    (int, int) -> str
    
    Returns the corresponding pattern to a given number and patternlength.
    '''
    if k==1:
        return NumberToSymbol(index)   
    if k>1:
        prefixIndex = index//4
        r = index % 4
        symbol = NumberToSymbol(r)
        PrefixPattern = NumberToPattern(prefixIndex, k-1) + symbol
    return PrefixPattern


def HammingDistance(Pattern, kmer):
    hdist = 0
    i = 0
    while i < len(Pattern):
        if Pattern[i] != kmer[i]:
            hdist += 1 
        i = i+1
    return hdist

def DistancePatternStrings(Pattern, DNA):
    k = len(Pattern)
    distance = 0
    for Text in DNA:
        act_distance = k+1
        for i in range(0,len(Text)-k+1): 
            kmer = Text[i:i+k]
            var = HammingDistance(Pattern, kmer)
            if act_distance > var:
                act_distance = var
        distance = distance + act_distance
    return distance

def MedianString(DNA, k):
    distance = k*len(DNA)+1
    for i in range (0, 4**k - 1):
        Pattern = NumberToPattern(i, k)
        if distance > DistancePatternStrings(Pattern, DNA):
            distance = DistancePatternStrings(Pattern, DNA)
            median = Pattern    
    return median
     