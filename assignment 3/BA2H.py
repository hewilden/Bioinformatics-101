# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:10:50 2018

@author: Helen
"""
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
        act_distance = 1000
        for i in range(0,len(Text)-k+1): 
            kmer = Text[i:i+k]
            var = HammingDistance(Pattern, kmer)
            if act_distance > var:
                act_distance = var
        distance = distance + act_distance
    return distance