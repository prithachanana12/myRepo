import sys
import re
seq=''
f1=open(sys.argv[1],'r')
for line in f1:
	if line.startswith(">"):
		pass
	else:
		seq+=line.rstrip('\n')
f1.close()
if re.search(r"[BDEFHIJKLMNOPQRSUVWXYZ]",seq):
	print "ERROR! Please enter a valid DNA sequence"
	sys.exit()
N=len(seq)
window=raw_input("Please enter a window size:")
j=int(window)
corr=0

for i in range(N-j):
	if seq[i]==seq[i+j]:
		corr+=1

#print corr
C=corr/float (N-j)
print "The periodicity of the input sequence is", '%.3f' %C	
