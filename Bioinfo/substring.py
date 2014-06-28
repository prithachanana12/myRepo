'''
Created on May 15, 2014

@author: Pritha
'''
#import re

with open('rosalind_subs.txt','r') as f1:
    dna=f1.readline()
    motif=f1.readline()
f1.close()

a=[str(pos+1) for pos in range(len(dna.strip('\n'))) if dna.strip('\n').startswith(motif.strip('\n'),pos)]
print ' '.join(a)