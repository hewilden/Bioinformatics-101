# -*- coding: utf-8 -*-

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