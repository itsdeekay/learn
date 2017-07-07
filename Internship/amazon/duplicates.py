import numpy as np
import sklearn
import random
import math
from sklearn import tree   
from sklearn.externals.six import StringIO
from decimal import Decimal
import math
import string
from numpy import zeros, array
from math import sqrt, log
import operator
setitem = operator.setitem

langs = ["de","fr","jp","en"] 
product = ["books","dvd","music"]

for xxx in range (len(langs)):
    for yyy in range (len(product)):
                current_input_directory = '%s/%s' %(langs[xxx],product[yyy])
                input1 = '%s/Source_ld.txt' %(current_input_directory)
                input3 = '%s/Source_mean.txt' %(current_input_directory)
                tppf = open(current_input_directory + '/source_noDup_ld.csv','w')
                tppf1 = open(current_input_directory + '/source_noDup_mean.csv','w')
                c=[]
                e=[]
                with open(input1) as fp:
                        for line in fp:
                            a=[]
                            a=line.split('\n')
                            c.append(a[0])
                fp.close()
                
                with open(input3) as fp2:
                        for line2 in fp2:
                            g=[]
                            g=line2.split('\n')
                            g[0]=g[0].replace(',', '')
                            e.append(g[0])
                fp2.close()
                
                source_p=np.zeros((len(c),len(c[0].split(' '))))
                
                for k in range(0,len(c)):
                    ar1=c[k].split(" ")
                    for i in range(0,len(ar1)):
                        source_p[k][i]=float(ar1[i])
                        
                hasDupes=source_p
                noDupes_source={}
                [operator.setitem(noDupes_source,repr(i),i) for i in hasDupes if not noDupes_source.has_key(repr(i))]
                noDupes_source=noDupes_source.values()

                source=np.ndarray.tolist(source_p)

                for j in range(0,len(noDupes_source)):
                    noDupes_source[j]=np.ndarray.tolist(noDupes_source[j])
                        
                b=len(e[0].split(' '))	
                add_overall=np.zeros((1,b))

                for j in range(0,len(noDupes_source)):
                    add=np.zeros((1,b))
                    y=0;
                    for i in range(0,len(source)):
                        if(source[i]==noDupes_source[j]):
                            ar4=e[i].split(' ')
                            y=y+1;
                            for x in range(0,len(ar4)):
                                add[0][x] = add[0][x]+ float(ar4[x])	
                        for t in range(0,len(add[0])):
                            add_overall[0][t]=add[0][t]/y		
                    tppf.write(str(noDupes_source[j]).translate(string.maketrans('', ''), '[]\'').replace(',', '')+'\n')
                    tppf1.write(str(np.ndarray.tolist(add_overall[0])).translate(string.maketrans('', ''), '[]\'').replace(',', '')+'\n')
                tppf.close()			
                tppf1.close() 

                    
                for i in range(0,16):
                    input2 = '%s/Target/Target_ld_%d.txt' %(current_input_directory,i+1)
                    input4 = '%s/Target/Target_mean_%d.txt' %(current_input_directory,i+1)
                    tpdf = open(current_input_directory + '/Target/target_noDup_ld_%d.csv' %(i+1),'w')
                    tpdf1 = open(current_input_directory + '/Target/target_noDup_mean_%d.csv' %(i+1),'w')
                    d=[]
                    f=[]		
                    
                    with open(input2) as fp1:
                        for line1 in fp1:
                            b=[]
                            b=line1.split('\n')
                            d.append(b[0])
                    fp1.close()

                    with open(input4) as fp3:
                        for line3 in fp3:
                            h=[]
                            h=line3.split('\n')
                            h[0]=h[0].replace(',', '')
                            f.append(h[0])
                    fp3.close()		

                    source_t=np.zeros((len(d),len(d[0].split(' '))))        
                    for p in range(0,len(d)):
                        ar2=d[p].split(" ")
                        for i in range(0,len(ar2)):
                            source_t[p][i]=float(ar2[i])

                    
                    
                    target=np.ndarray.tolist(source_t)		
                    hasDupes=source_t
                    noDupes_target={}
                    [operator.setitem(noDupes_target,repr(i),i) for i in hasDupes if not noDupes_target.has_key(repr(i))]
                    noDupes_target=noDupes_target.values()

                    for j in range(0,len(noDupes_target)):
                        noDupes_target[j]=np.ndarray.tolist(noDupes_target[j])

                    d=len(f[0].split(' '))
                    add_overall1=np.zeros((1,d))

                    for j in range(0,len(noDupes_target)):
                        add=np.zeros((1,d))
                        y=0;
                        for i in range(0,len(target)):
                            if(target[i]==noDupes_target[j]):
                                ar5=f[i].split(' ')
                                y=y+1;	
                                for x in range(0,len(ar5)):
                                    add[0][x] = add[0][x]+ float(ar5[x])
                            for t in range(0,len(add[0])):
                                add_overall1[0][t]=add[0][t]/y
                            np.ndarray.tolist(add[0])
                        tpdf.write(str(noDupes_target[j]).translate(string.maketrans('', ''), '[]\'').replace(',', '')+'\n')
                        tpdf1.write(str(np.ndarray.tolist(add_overall1[0])).translate(string.maketrans('', ''), '[]\'').replace(',', '')+'\n')
                    tpdf.close()
                    tpdf1.close()

