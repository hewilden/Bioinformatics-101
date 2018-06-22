# -*- coding: utf-8 -*-
"""
Created on Sat Jun 16 18:54:27 2018

@author: Helen
"""

import random 


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
    

def Consensus(motifs):
    profile=Profile(motifs)
    consensus = ''
    for i in range(0, len(motifs[0])):
        liste2 = []
        for lis in profile.values():
            liste2.append(lis[i])
        ind = liste2.index(max(liste2))
        base = NumberToSymbol(ind)
        consensus = consensus + base
    return consensus

def HammingDistance(motif1, motif2):
    hdist = 0
    i = 0
    while i < len(motif1):
        if motif1[i] != motif2[i]:
            hdist += 1 
        i = i+1
    return hdist

def Profile(motifs):
    k = len(motifs[0])
    profile = {
            'A' : [1/(len(motifs)+4)]*k,
            'C' : [1/(len(motifs)+4)]*k,
            'G' : [1/(len(motifs)+4)]*k,
            'T' : [1/(len(motifs)+4)]*k
            }
    for kmer in motifs:
        for index, base in enumerate(kmer):
            profile[base][index] +=1/(len(motifs)+4) 
    return profile


def Motifs(profile, DNA):
    k = len(profile['A'])
    motifs = []
    bestprobs=[]
    for string in DNA:
        bestprob = 0
        for i in range (0,len(DNA[0]) - k  + 1 ):
            kmer = string[i:i+k]
            l = 0
            prob = 1
            for base in kmer:
                p = profile [base][l]
                prob = prob * p
                l += 1
            if prob > bestprob:
                bestprob = prob
                bkmer = kmer
        bestprobs.append(bestprob)
        motifs.append(bkmer)
    return motifs

def Score(motifs):
    consensus = Consensus(motifs)
    score = 0
    for motif in motifs:
        hdist = HammingDistance(consensus, motif)
        score = score + hdist
    return score

def RandMotifSearch(DNA, k, t):
    motifs = [] 
    for string in DNA:
        i = random.randint(0, len(DNA[0])-k)
        motifs.append(string[i:i+k])
    #print(motifs)   
    BestMotifs = motifs
    while True :
        profile = Profile(BestMotifs)
        motifs = Motifs(profile, DNA)
        #print(Score(BestMotifs))
        #print(Score(motifs))
        #print(motifs)
        #print(profile)
        if Score(motifs) < Score(BestMotifs):
            BestMotifs = motifs
        else:
            return BestMotifs
        
DNA1 =['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA',
      'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG',
      'TAGTACCGAGACCGAAAGAAGTATACAGGCGT',
      'TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 
      'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']

DNA2 = ['ACTTATATCTAGAGTAAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCGAGTGATTGAACTGACTTATATCTAGAGT',
'AAAGCCCTGATTCCATTGACGCGATCCCTACCTCCATCATACTCCACAGGTTCTTCAATAGAACATGGGGAAAACTGAGGTACACCAGGTCTAACGGAGATTTCTGGCACTAACTACCCAAAATCCTCTCGATCACCGACGAGTGATTGAACTGACTTATATCTAGAGT',
'CACTCCCGTCCGTCTGACGCCAGGTGCTCTACCCCGCTGATTGTCTGGTACATAGCAGCCTATAGATCACCGATGCAGAAACACTTCGAGGCAGCCGATTTCGCTTATCACAACGTGACGGAATTTGATAAACCACGTACTCTAATACCGTCACGGGCCCATCAACGAA',
'ACAAGAACTGGTGGGGAGACTATGACACTCTAGCGGTCGCATAAGGGCCGGAAACCAGGACAAATCGATAAGATGAAGCGGGGATATAAGCCTTATACTGCGACTGGTTCCTTATATTATTTAGCCCCGATTGATCACCGATTAAAATATTCTGCGGTTTTCGAGACGG',
'TAACCACACCTAAAATTTTTCTTGGTGAGATGGACCCCCGCCGTAAATATCAGGATTAAATGTACGGATACCCATGACCCTCCAGTCATCTACCTTCCCGTGGTGGTCGCTCAGCCTTGTGCAGACCGAACTAGCACCTGTCACATACAATGTTGCCCGCATAGATCGT',
'ATCCGACAGAGGCAGTGAATAAGGTTTCGTTTCCTCAGAGAGTAGAACTGCGTGTGACCTTGCCTTCACCGACATCCGTTTCCAATTGAGCTTTTCAGGACGTTTAGGTAACTGATTGTCATTGCAATTGTCCGGGGGATTTAGATGGCCGGGTACCTCTCGGACTATA',
'CCTTGTTGCCACCGATTCGCGAGCAACATCGGAGTGCTCTGATTCACGGCGATGCTCCACGAAGAGGACCGCGGCACGACACGCCCTGTACCTACGTTTCTGGATATCCTCCGGCGAGTTAATAGAGCAATACGACCTGGTCGTCGAGATCGTGTATCTAGCCCTACCT',
'ATAGGTTAACGAATCAGGAGAGTTAATTTTACCTAGCTAGAGCGGACGGTGCCTGGCTGTATTCGCGTTTGACTTTCGGGCTCGCTGATAACTTGTGATCACCTTTTACGCTTACTGGATCCAACGATGGATCAAAGTTGAGAATTTCTGTGCCTTGGGTGTGAGCTGT',
'CTGACGAAAGGACGGGCGGTGTACTTAGTTTGGGGTAAAATAGTTGGTATAATTCTGTGCGACAGACATTTGGTCAGGCCATACTGCCATATCGTGATGTAACTATCCACACTACGTCATAGGCCCTTGTGATCAATTAAACGTTCCTCATGCCAGGCTATCTGTTTAA',
'GGCTTCGCGTTTAAGGCTGGATTAAGTACTCCGCCTTGTGATCTGTGATCCTCCGACCTGTGATCAGCAAGATTGGAACCTAGGTAGGCGGCGGGTCTACGCTGGCCCACAATCGTGAGTCCCCCACTCCGTAGGTTGTGGAATTTATAGACCCGCAAGGGGCACCACT',
'AGGATGACACCCAGGATGAATCTGGATTAGGAACACCAACCCGACATATTTGTTACCGCTGCAGCATTTCGCTCTTGGACGCGTAACCCGAGATCCGTCTCGCGATCGTCACGGATCGGGATTATGCAGGCAATACCTTGTGATCACTCCGCGCTTGGTTTTGCTAGCG',
'ACATCTCTAGTCACTTTTATTGAGCAGGTGGGCGGATTCATGATCCGGCTCTGTCGTACGTCCAACCACGGTGACATGTTCGGAGCTGTCGCCGTGGAGCAGAGATACATCGGATCTATCAATTTTACTAAGAGCAACTAGCCACGACAAACTGTGATCACCGATTGGA',
'AATTTGCGTATCTCTAGGACTCCCTCATACAAATCAAAGCTTGGATGGGTAAGATGCCGCAGCAGCAGGTATCTCATATTGGCTATTAAGAGCCAGGCCCTATGGCCTTAGTATCACCGATCAGACGTCGCATGAGCGGGCCCGTTGTCCTATCTCTTTAGCTGCCGCA',
'GAAGTAAAGGGGTTCCACTGCGTAGAGCGTGCCCCTCTGGTGTGCCGTACTGTTATGGTGATACAGCTTCCTTATACCCCTCGTAAAGCGGCTAATGGTCCTAATGAATGCCCTTGTGAAATCCGAATCGCTTTACAATTGCGTTCGGCGGAATGCAGTCACCAGTGTT',
'TACACTACGCGTTATTTACTTTTACTGAGTCCTTGTCGCCACCGAACGAGGATTGTTCATTGTATCCGGAGATTAGGAGTTCGCATCGCTGACACAGCCAGTTCGTAGCAAATACCGCTGGCCCTGGGCACTCCAGATCAGAACTACTAGCCCTAAACTCTATGACACA',
'TTGGGTCTCGATCCCTCTATGTTAAGCTGTTCCGTGGAGAATCTCCTGGGTTTTATGATTTGAATGACGAGAATTGGGAAGTCGGGATGTTGTGATCACCGCCGTTCGCTTTCATAAATGAACCCCTTTTTTTCAGCAGACGGTGGCCTTTCCCTTTCATCATTATACA',
'TTTCAAGTTACTACCGCCCTCTAGCGATAGAACTGAGGCAAATCATACACCGTGATCACCGACCCATGGAGTTTGACTCAGATTTACACTTTTAGGGGAACATGTTTGTCGGTCAGAGGTGTCAATTATTAGCAGATATCCCCCAACGCAGCGAGAGAGCACGGAGTGA',
'GATCCATTACCCTACGATATGTATATAGCGCCCTAGTACGGCTTCTCCCTTGCAGACACGCAGGCGCTGTGCGCTATCGGCTTCCTCGGACATTCCTGGATATAAGTAACGGCGAACTGGCTATCACTACCGCCGCTCCTTAAGCCTTGGTTTCACCGACGATTGTCGT',
'TAGTAGATTATTACCTGTGGACCGTTAGCTTCAAGACCGAAACGTTGGTGATGCTACTTAAATGTCAAGAGTTGCGAAGTTGGGCGAAGCACATCCGTACTCCCAAGTGGACGATCGATAGATCCATGGAGTTTCCATCCATCTTAATCCGCCCTTTGCATCACCGACG',
'TACAAGGCACAAACGAGACCTGATCGAACGGTGCACGGTCGAGGCAGCGAGATAAATGTACATTGAGAGCACCTTGTGATTTACGACCTGCATCGAAGGTTTCTTGGCACCCACCTGTCGTCCGCCAGGGCAGAGCCGACATTATATGACGCTGATGTACGAAGCCCCT']


scores = []
motifs = []

for x in range(0, 1000):
    
    result = RandMotifSearch(DNA2, 15, 20)
    score = Score(result)
    scores.append(score)
    motifs.append(result)
  
#print(motifs)    
#print(scores)
index = scores.index(min(scores))
print(motifs[index], scores[index])
    