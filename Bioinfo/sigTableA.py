'''
Created on Apr 14, 2014

@author: Pritha
'''
import re
import os
import sys

def getCols():
    global result
    result=[]
    a={}
    with open('E:\e-Books\capstone\countstable.txt','r') as f1:
        colHeads=f1.readline()
        colHeads=colHeads.split()[1:]
        for c in colHeads:
            cL=re.split('_+C$|_+E|_C3|_E5|_E24|_E1|_E3|_E7',c)
            if cL[0] not in result: result.append(cL[0])
    for col in result:
        a[col]="" 
    return a

#colDict=getCols()
#print colDict

def getData(mainDict):
    os.chdir("E:\e-Books\capstone\sigFDR1")
    this = os.getcwd()
    files = os.listdir(this)
    for fh in files:
        with open (fh,'r') as csvfile:
            p=os.path.basename(fh).strip('_E.txt')
            print "Processing file: ",p+"_E.txt"
            sys.stdout.flush()
            m=re.search('.+_C.?_(.+$)',p)
            for line in csvfile:
                if line.startswith('id'):
                    pass
                elif 'NA' not in line:
                    w=re.split('\t',line.strip('\n'))
                    if w[0] not in mainDict.keys():
                        mainDict[w[0]]=getCols()
                        mainDict[w[0]][m.group(1)]=w[5]
                    else:
                        mainDict[w[0]][m.group(1)]=w[5]
                              
    return mainDict


mainDict={}
with open('E:\e-Books\capstone\countstable.txt','r') as f2:
    for lines in f2:
        if lines.startswith('gene'):
            pass
        else:
            mainDict[lines.split()[0]]=getCols()
            print "Reading into dictionary"
            sys.stdout.flush()
#print len(mainDict.keys())

       
resultDict = getData(mainDict)
a=['cellLines']+result
os.chdir("E:\e-Books\capstone")
with open ("try.txt","w+") as f1:
    f1.write("\t".join(a))
    f1.write("\n")
    for item in resultDict.keys():
        f1.write(item+"\t")
        for col in result:
            f1.write(resultDict[item][col]+"\t")
        f1.write("\n") 
f1.close()
f2.close()
