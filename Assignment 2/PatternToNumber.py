# -*- coding: utf-8 -*-

def NumberToSymbol(x):
    '''    
    (str) -> int
    Returns corresponding number to given nucleotide.  
    ''' 
    dict = {0 : 'A', 
            1 : 'C',
            2 : 'G',
            3 : 'T'}
    return dict[x]

def SymbolToNumber(x):
    '''    
    (str) -> int
    Returns corresponding nucleotide to a given integer.
    ''' 
    dict = {'A' : 0, 
            'C' : 1,
            'G' : 2,
            'T' : 3}
    return dict[x]

def PatternToNumber(pattern):
    '''
    (str) -> int
    Returns the corresponding number to a given kmer.
    '''
    if pattern == '':
        return 0
    if pattern != '':
        symbol = pattern[-1]
        prefix = pattern[:-1]
        return 4*PatternToNumber(prefix)+SymbolToNumber(symbol)
