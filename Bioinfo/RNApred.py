import sys
import re
from numpy import *
seq=''
f1=open(sys.argv[1],'r')
for line in f1:
	if line.startswith(">"):
		pass
	else:
		seq+=line.rstrip('\n')
f1.close()
if re.search("[BDEFHIJKLMNOPQRSTVWXYZ]",seq):
	print "ERROR!ENTER A VALID RNA SEQUENCE"
else:
	pass
def complementary(m,n):
	if m=='A' and n=='U':
		value=1
	elif m=='U' and n=='A':
		value=1
	elif m=='G' and n=='C':
		value=1
	elif m=='C' and n=='G':
		value=1
	elif m=='G' and n=='U':
		value=1
	elif m=='U' and n=='G':
		value=1
	else:
		value=0
	return value
L=len(seq)
#print m
s=zeros((L,L))
#print s
for x in range(1,L):
	for j in range(x,L):
		i=j-x
		score1=s[i+1][j]
		score2=s[i][j-1]
		score3=s[i+1][j-1]+complementary(seq[i],seq[j])
		if i+3<=j:
			score4=0
			k=i+1
			while k<j:
				temp=s[i][k]+s[k+1][j]
				if temp>score4:
					score4=temp
				k+=1
			s[i][j]=max(score1,score2,score3,score4)
		else:
			s[i][j]=max(score1,score2,score3)

print "The maximum number of internal pairings: " '%.0f' %s[1][L-1]

