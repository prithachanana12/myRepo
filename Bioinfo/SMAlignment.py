import sys
import re
from numpy import *

seq1=''
seq2=''
f1=open(sys.argv[1],'r')
for line in f1:
	if line.startswith(">"):
		pass
	else:
		seq1=seq1+line
f2=open(sys.argv[2],'r')
for line in f2:
        if line.startswith(">"):
                pass
        else:
                seq2=seq2+line
f1.close()
f2.close()
if re.search(r"[BJOUXZ]",seq1):
	print "sequence1 ERROR-please enter a valid protein sequence"
	sys.exit()
if re.search(r"[BJOUXZ]",seq2):
	print "sequence2 ERROR-please enter a valid protein sequence"
	sys.exit()
m=len(seq1)-1
n=len(seq2)-1
#print m
#print n
gap=-2
match=2
mismatch=-1

local_matrix=zeros((m+1,n+1))
traceback=zeros((m+1,n+1))
max_score=0
for i in range(1,m+1):
    for j in range(1,n+1):
	score_up=local_matrix[i-1][j]+gap
	score_left=local_matrix[i][j-1]+gap
	if seq1[i-1]==seq2[j-1]:
		score_diagonal=local_matrix[i-1][j-1]+match	
	else:
		score_diagonal=local_matrix[i-1][j-1]+mismatch
	local_matrix[i][j]=max(0,score_up,score_left,score_diagonal)
	if local_matrix[i][j]==0:
		traceback[i][j]=0
	if local_matrix[i][j]==score_up:
		traceback[i][j]=1
	if local_matrix[i][j]==score_left:
		traceback[i][j]=2
	if local_matrix[i][j]==score_diagonal:
		traceback[i][j]=3
	if local_matrix[i][j]>max_score:
		maxi=i
		maxj=j
		max_score=local_matrix[i][j]
align_seq1=''
align_seq2=''
i=maxi
j=maxj
while traceback[i][j]!=0:
	if traceback[i][j]==3:
		align_seq1=align_seq1+seq1[i-1]
		align_seq2=align_seq2+seq2[j-1]
		i=i-1
		j=j-1
	elif traceback[i][j]==2:
		align_seq1=align_seq1+'-'
		align_seq2=align_seq2+seq2[j-1]
		j=j-1
	elif traceback[i][j]==1:
		align_seq1=align_seq1+seq1[i-1]
		align_seq2=align_seq2+'-'
		i=i-1

align_seq1=align_seq1[::-1]
align_seq2=align_seq2[::-1]
#print align_seq1
#print align_seq2
f3=open(sys.argv[3],'w')
f3.write(align_seq1)
f3.write("\n")
f3.write(align_seq2)
f3.close()
