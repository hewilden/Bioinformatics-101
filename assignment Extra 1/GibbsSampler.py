# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 15:08:37 2018

@author: Helen
"""
import random
import numpy as np

def HammingDistance(motif1, motif2):
    hdist = 0
    i = 0
    while i < len(motif1):
        if motif1[i] != motif2[i]:
            hdist += 1 
        i = i+1
    return hdist

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

def Score(motifs):
    consensus = Consensus(motifs)
    score = 0
    for motif in motifs:
        hdist = HammingDistance(consensus, motif)
        score = score + hdist
    return score

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

def Motif(profile, DNA):
    k = len(profile['A'])
    motifs = []
    probs=[]
    for i in range (0,len(DNA) - k  + 1 ):
        kmer = DNA[i:i+k]
        l = 0
        prob = 1
        for base in kmer:
                p = profile [base][l]
                prob = prob * p
                l += 1
        probs.append(prob)
        motifs.append(kmer)
    b = len(probs)
    bias = []
    Sum = sum(probs)
    for prob in probs:
        rnprob = prob/Sum
        bias.append(rnprob)
    j = np.random.choice(b, p = bias)
    motif = motifs[j]
    return motif

def GibbsSampler(DNA, k, t, N):
    motifs = [] 
    for string in DNA:
        i = random.randint(0, len(DNA[0])-k)
        motifs.append(string[i:i+k])
    #print(motifs)   
    BestMotifs = motifs
    for j in range(1, N):
        i = random.randint(0,t-1)
        motifs.remove(motifs[i])
        profile = Profile(motifs)
        imotif = Motif(profile, DNA[i])
        motifs.insert(i, imotif)
        if Score(motifs) < Score(BestMotifs):
            BestMotifs = motifs
    return BestMotifs

DNA1 = ['CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA', 'GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG', 'TAGTACCGAGACCGAAAGAAGTATACAGGCGT','TAGATCAAGTTTCAGGTGCACGTCGGTGAACC', 'AATCCACCAGCTCCACGTGCAATGTTGGCCTA']
    
DNA2 = ['CTCTTGATTAAGGAGATGTAAAACTCTTTCCGGACATTAACTTGTCGATTGGTTCGTTTTATGATTGTTAGCCCATACAACGAGTGCTACTTTCGACGATTACCTGGCAACAATAGACAAGTCAGGGCCGCGGAAGACTGATCCCCTATACAGACCGTTATCATGCTACGAGAACGGTTGTCTAGCAACTCTTAGCTACGTGTGACGTCCACCGGCGTCGAGCCTGGCGACTATTAAATTCGCATGCGCTAAAAGCACCTGTTATAAACGGCTGTCAGCGATGTTCGGCCGATATGCGCATCTTCGTTTCCTCTTGATTAAGGAG',
'ATGTAAAACTCTTTCCGGACATTAACTTGTCGATTGGTTCGTTTTATGATTGTTAGCCCATACAACGAGTGCTACTTTCGACGATTACCTGGCAACAATAGACAAGTCAGGGCCGCGGAAGACTGATCCCCTATACAGACCGTTATCATGCTACGAGAACGGTTGTCTAGCAACTCTTAGCTACGTGTGACGTCCACCGGCGTCGAGCCTGGCGACTATTAAATTCGCATGCGCTAAAAGCACCTGTTATAAACGGCTGTCAGCGATGTTCGGCCGATATGCGCATCTTCGTAAGCGCACCGGGGTGTTCCTCTTGATTAAGGAG',
'GAGATGATAGGTTGGCCGGTTCGCCTCGATACGGTCCACGCCTGCTGGAATCTAGCTAGACAATTGCTTAGTGGATTCATTCTCCTCACCCCTGTAATTTACCCTTACCGGGGTGGGGAGGAAATACTCCACGTAGAACACGTTTACGAGCCTAAGGGCCGAGAATCACATAAGGCGTCTAACTATTAAGTGCCTTTGGTATCGATTATTGTGTTTTTCCCCATGCCCGCAGTCCTCCACTTAATAGACTGCTATCAACTATGGTAAATCAATTTCCACGATCGGGCTCTCGAACTTCTGTGTTATCCGATACGTCGCCGAAATC',
'GCCTAATTGAATTATAAAGTATTTCGTCCGACATATCGCCATGTTGACTGTATGCGCATGGAATTCGCTTCGAGAAGTTCCTCGGGGTGAGGCACGTTTTGAAGAACCCGGAAGCTCCTTCGGTTGAGCCTAAGTTTACTCTATAGGCAATCTCACCATCCGCGTCCACCCAATCGCGTGAGGTAAGATCTAAGTCCGGCTGCAAGTATCCATAAGGCCCCTTGCGGATGGTCACGTCTCTTAGCAAGGAGTCAATGAGATCGGCCCTCCCTACCCTTAGTCTATGTTTTGGCATAAGCATTGGGAATTGTGTAGGATATGTGAG',
'CGTTTCATCTACATGACATTGCTGCTACGACATGCGTGTCGCCCTCCTGGAGCCCAGTGTTGATCACCGTGGGAACGTTCCTAATAGCTGAAGTGAGGACTGGGAATTCGTTCACTTGACGTCTCACCTGTCGATTTATGCATTTGAAGCTCAATTTGGGGGTAAATTGGAATGAGAGCGAAGAGACGTTTACCTATCCTTCTAATAGGAAACTTCTAGTTGGATGATGAGATAAGTTTTATGGGGTGTATATTGGGCGTCAATGAACCCTCGCCAGTGTAAACACCAATTTCCATTGAGGTTGGGTGGTAGAGTCCGCGGGACA',
'TAGACTAACCCACACGTAACCAATTGGTTTTTCGGACAGGGTGAAGGGATGTGTGCATCGAAAGTTTTTAGCTACGACTGTAATATCCACTTCACCTCTGTCCACCAGTACAATCCAGGTAATAAATCTCCTCTGGCTGGTGCTTTAAAGGGAGTCTGTTTCACGATCCTTGAACAGGTGCGTCTCACGAGGACGTGTATGAATTTTCATAATAGACGTGTTCCCGAGCCACCAACAGGAGCGTGCCTGATTCGGAAGATGCAAAGCCAATTGCATACCACCTGCACAGGAGGAGGCATGGATCGCAAGTTTACCGGGTGCAAGG',
'CCTACTTGACAAGCGTAGGCGCGGTACGCAAGTGTTGCGTTCTCCCTCGCAACACCCGTCAGTGCTACGGGGACGGGTTTTACGACTTGACGCTCTTCCGGCCACCTGCATTAACTCGACGGAATGAGCACGGCTCGGTAGGCGATCGAGTATGCGTCATGGGAAAATAGGAATCGGACGCCCCTCGGGCATATTAAGCCTGCGTTCGTGTTGTCCTTACGATATTAGCCTACCAAGTTTCGAGGGGTGCCAAGCTCAAGTGATCCGGAACTTTGCTTTACCACCACCGCCATCCAGGGCATTATACATCGCTCCCTTGTGACCT',
'TAATACACATCCTCGGACTCCACATGACGATACCACTAAAAAATCAACGACCTTTCGGCCGCATGATAGGTCATGAGGGGGCAGTTTATTCTCGGTTCCTGTTTACCGGGGTATGGTAAATCTGCAGGGTTGCACACCCGATCAGCTTGTAGGCTTTCGTGCTTTCAGATTTCTAACAATACGTTAAAGATTTTTGAGTTAGAGAAAGAGCGTCGAACATACTGTCGTACCAATTTACTCTTTACGATCATTCGCCCGCAGCATTCCGGTGCAATCGATTATTCGCATAGTCATTCCCCTGTTCCGTGGCTATTCTTCGTACCTT',
'AATGGGATTGCTGAACAAGAAGGCGGCTTAGACTGTCTATGGCTTCCGATCGGACTAACGGCGAATAATAGTAAGATTACGGATCCCTGACAGCTTCAGTCCGCAAACGACACCACAGGCTCCTGTAGTAAAACAGACAGCCACTATAGCGCGATTGTTGGCCCCCCCTTAAGTTGCTCGGGGTGGTCCAACAGTCCCCAGAAGACATACGACGGGATGTATATAATGAAATTCGCCTTCTTTAAGAAGATGCTCTGGCAGTTTCATATAGGGGCCCGCTGTTGAAAATCGGATGAGTGAGGATACATGCGTTTGCGTTCGTGTC',
'GATACTCCTATCGCGCAGTGACCTCCCTGCGTTCATATTTAGCCCTACTTTGACGAGACAGATAGCTGGGAAAGCCTATTCGACATATATACTGCGATGACTCCGGAACGTAAAAGAGTAAATCGACATATTTAGTGGCTTGGATTTGAGTAGTATCGCAACCTACGCCGATGCGGAAAATTAAACATACCGGGGTGTCCCATATGAGGGGGGCGAAATCTCCGAGGATTGAGTACTCGTGCCCCCGACTTTTTTTCGACTCGCGGCAATGAAAACCGAAGGAGGCACGAAGTGGTACATGTGTACCCCTCTTTGGTTACTCATG',
'CGCAGGCTCATTCGTTCACGAACACACGGAACTACCCAGCGCGTTGATGCTCCAAAACGAGGCCACGTTCACAGAACCGAAACACCGATAAAAGCGCGCCAACAACCCGACGACGCACAGGGTGAAATGGCACTTACGGCTCTTTCATGATCTTCGACCGAAGGAATGGAGGGGGTCACCTGGCCCGGCCCGGTGAGTGCTTGTATAGGCGTTTGTACTGAGGTACCAGGACCGGGCGCTGCACAAGCTGCCATTCTAGCGTATTCTCATATCCAAATGGCTCGCAAGTTTAGGAGGGTGGGGCTCCCGCCAGGCCGTCATATCC',
'ACGTTTCGCAGCTGAGGTAAGGAAACCGGGGTGGAATCACCCTCGAAGCTGGTCGCGCCGGCATCTATTGTTGAGCAGGTCATCACAATTCCTCTATTTCTATGATACAACTTCGACGATCCACGGGATATGTAACGCCGGAACACAGGAGTAAATGTGATTGACAGGGGCTCATCCGTCTGCCCAAACGGCATCTACGCAATGACTGCATAGGTTTTGTGTAAAAGAGTTTGTCATCTACCCAACCAGGACAAGTCAGCCCGCGCAAACGGCCCACGCGCACATATCAAGCCCGTCAGGCGCCCGCAGAAACAGATCCTAAGTT',
'GTGGCTGTGCGTAACCGTCTAAATGTAAAAGCGCACATGAGGTAAGTTTACACAGGTGACCCAAGTGATCCTGATCGAGATGGGTAACCGCATTTCTGTGAGTCGGGACACTGGGTGTTACCAGTTGCCAGAAATTCGGCGGGGAGTGAGTTCGGTCGGTATTTATGACTAGGTCATTGGGCTGCAGCGCTCCGCAACAGTCCATGGTTTATAGTTGGAACAGACCGGGGTGATTCATTAAAAGAACATTCATCTGCTTAGAAAAATAGATTTACGTTCCGTAGAACCGTAAGAAATTACTGGCTAACCCAACATAAAAGCTGAG',
'TCGAATCCGCCACATGCAAGGCTCAATGTTGACAACTCTTGTGGAGAAGACATTGCAAGACAGCTTGAAGGAGGTCCGCTAGAGCTAGTCTACGCTCCGTGTCAAAGCCTGGAGAACATACGATAATGAGTTAGACCGGGGCCAATTAGTTTACCGGGGATCGCTGAACAACCGGTCCGTGACCATACACTTAGTTGGGTAGCAATACATCTGGCCCGGTCAATTTCATCTAAGGCACCCGATATGAGGACGTGTGCAATACACATATTTTCGGTGCTGTCATGTCCTGTGAGGTTTGCATGGCTGACCGTACTAGTATTAACAG',
'GGCCTTAATGAATCGCTCTGTCATGCATGCATTGGGATGGGGACCCCTCCGTTAGCTGTGATGGGTCGAGACGTACGATGTACCGCCCCTTTTACCGGGGTGAGCGATTCTCGTGCGAAATGTTCTCCCACTTTGTCCGGCCGTGCGCGCAGCATACTGGGCAGCCTGCGTTCCCCGCCCCCCCACATGACCACGACTGGGTTCGCCATCGTCAGCTTAAAATCCGTATGGTTAGGGAAGATAGCGTCCAAATGGGAAGCATGCACGTAATTCAGACTGAGTCCCTCTGTATTCTGTCTTGGACGTAATGAAACTCTATAAAACT',
'CCCTAGCAAAAGCCCTCTTCAATCACTTGCAATTGTTCTTTACCCCCTTAACTCAGCTTGACCATCATCAATCCAAACCGAAGCTTCGGCCACATCCAGTATGCCGAACAAAGGCAGTAGATTATGCGATCATTCTGTTCTATAACTTTCTTTCTACCCTCACCGATCCACATATTAGCTGTGATTTCGAGTCATTCTGATTGACTATTCATGACTTCCGGCTAAAGACAGGTACATGAAGTGAGCCGGGGTGATACAGGAGTGGGATGCTTGGGCAGCGTTCAATTGGAGAAATCGGAGAGTTGCTACCATTCCTGCTGTCTGG',
'GCGTGACGGCTCTATAAGAGAACTACGACCAATAGTACCGGTGGTCCTCAGCCTTAAATATAGTGTAAAGTCGTCCGGGGTGATTCAAATGGGTGTCTTTAAACTTATTTAGAAGTACATTGTGCCTAGGTTTCCGGGACTTGCCATAATTGAGAGTCCCTCATTCTCGGTGAGGAGCGCCGAAGTCCCGTTAATCTGGCGTGTCCCGTGATGCATCATCTAAGTTATCAGTCAGTCGCACGCACTCCTACATGACTGAACCAGTGCGCGCTGAGATGGTACGCGTGCTCACTGTCCAAGGAGACGGACACGTATCAACTGGCGC',
'GCCTATGGAATTGCAATGGAGTTATGTCCAGTACAGAGGTGAAAGTTTACCGGACAGAGATTACCAACCCCGGGATTAGGGGAGATCGAGCTGCGGGCTCGTGGGCCAAGTATTCAACGAACAAAGCTTAAGTAAAGCAGCGAAACGCCTACCGGTACAACAGGCGGTTCAGGTGACTACCAATAAAGTAAATGTTCGGACGCAGACGTCTAAGCAAGTGACGGCCTAGGAGTTTACGCCCTACAACCCACCAGCCACCAACGGCAAATAAGTCCCTACTGACCGCGGCATTTTGCGCACCGAACTAGCCGTCAACCACATCACG',
'CGGTCCATGTCTCTAGCGCAAATGGATAGGTTCTGTATATACGGCACCTGGCCCAGCACGTCTTTACACAATAAACAATAACCCGAGTGGTGTTAGGTGAGACTTACTAAGGGACCCGCGCAACAACGGGTCCAAGGTGACGGATTTTAATCGTTGCGTGTCGATATCTCGCAGCATCTAAGACTGAGAATGGCGGGATTCACTCCTCGGACTAGGACATCTTCCCAAAGTTTACCAATGTGAGAGACAGAGGTGCACCACTAGGCACGGATGTATGCGCGAGCAATTGAACAATACGGTCCTGTTATACAGTTCACGTTAACAC',
'GTCGGTTCAGAGCAACTTTACATAGAGGAACGGAAAGAGCAACATTCTTCCCAAGTTTACCGTCATGGTTTGCGAGTACAGCGGCCGGCACTACTGGCGGAGTGAGCCACATCGTTGGCTGGGACCGAGAAACTGCGAGTCTTTAAACGGACCCGCGCCCCAGACACTAGTGTTTCCTATGCGCGCGCATAAAAAGCCAGTCCCGGTAACTGGAGTTCAGGACCAAGGAGTTTGGACAAGCTTGCTAATCGAAATACCATTTGTGTTGCGATCTTGGAGCGTGCGTAGCGCTTACGGTCGAAACGTACCCCGCAGTATTATACCC']    
scores = []
motifs = []

for x in range(0, 20):
    
    result = GibbsSampler(DNA2, 15, 20, 2000)
    score = Score(result)
    scores.append(score)
    motifs.append(result)
  
#print(motifs)    
#print(scores)
index = scores.index(min(scores))
print(motifs[index], scores[index])       
        