import numpy as np
import sklearn
import random
import math
from sklearn import tree   
from sklearn.externals.six import StringIO
#import pydot
from decimal import Decimal
import math
from numpy import zeros, array
from math import sqrt, log

langs = ["de","fr","jp","en"] 
product = ["books","dvd","music"]

#for xxx in range (len(langs)):
for yyy in range (len(product)):
        current_input_directory = '%s/%s' %(langs[3],product[yyy])
        input1 = '%s/source_noDup_ld.csv' %(current_input_directory)
        input2 = '%s/source_noDup_mean.csv' %(current_input_directory)
        #for w in range(len(langs)):
        #    if langs[xxx]!=langs[w]:                    
        current_input_directory1 = '%s/%s' %(langs[1],product[yyy])
        for t in range(0,16):
            input3 = '%s/Target/target_noDup_ld_%d.csv' %(current_input_directory1,t+1)
            input4 = '%s/Target/target_noDup_mean_%d.csv' %(current_input_directory1,t+1)
            tppf = open(current_input_directory + '/Identical/source_final_%s_%s_%d.csv' %(langs[3],langs[1],t+1),'w+')
            tppf2 = open(current_input_directory + '/Identical/source_distributions_%s_%s_%d.csv' %(langs[3],langs[1],t+1),'w+')

            tppf1 = open(current_input_directory + '/Identical/target_final_%s_%s_%d.csv' %(langs[3],langs[1],t+1),'w+')
            tppf3 = open(current_input_directory + '/Identical/target_distributions_%s_%s_%d.csv' %(langs[3],langs[1],t+1),'w+')

            c=[]
            e=[]

            d=[]
            f=[]		
            with open(input1,'r') as fp:
                for line in fp:
                    c.append(line.strip())

            with open(input3,'r') as fp1:
                for line1 in fp1:
                    d.append(line1.strip())
                    
                    
            with open(input2,'r') as fp2:
                for line2 in fp2:
                    e.append(line2.strip())


            with open(input4,'r') as fp3:
                for line3 in fp3:
                    f.append(line3.strip())

            fp.close()
            fp1.close()
            fp2.close()
            fp3.close()


            class JSD(object):
                def __init__(self):
                    self.log2 = log(2)


                def KL_divergence(self, p, q):
                    """ Compute KL divergence of two vectors, K(p || q)."""
                    return sum(p[x] * log((p[x]) / (q[x])) for x in range(len(p)) if p[x]!= 0)

                def Jensen_Shannon_divergence(self, p, q):
                    """ Returns the Jensen-Shannon divergence. """
                    self.JSD = 0.0
                    weight = 0.5
                    average = zeros(len(p)) #Average
                    for x in range(len(p)):
                        average[x] = weight * p[x] + (1 - weight) * q[x]
                        self.JSD = (weight * self.KL_divergence(array(p), average)) + ((1 - weight) * self.KL_divergence(array(q), average))
                    return 1-(self.JSD/sqrt(2 * self.log2))

            J=JSD()
            v=len(c[0].split(' '))
            ar2=np.zeros((1,v))
            v=len(d[0].split(' '))
            ar4=np.zeros((1,v))


            for k in range(0,len(c)):
                #print k
                ar1=c[k].split(' ')
                for i in range(0,len(ar1)):
                    ar2[0][i]=float(ar1[i])
                for j in range(0,len(d)):
                    ar3=d[j].split(' ')
                    for l in range(0,len(ar3)):
                        ar4[0][l]=float(ar3[l])						
                    if(J.Jensen_Shannon_divergence(ar2[0], ar4[0])>=1):
                        #print "hello found"
                        tppf.write(' '.join(map(str,e[k].split(" "))) + "\n")
                        tppf1.write(' '.join(map(str,f[j].split(" "))) + "\n")
                        #print str(ar2[0])
                        #print str(ar4[0])
                        tppf2.write(' '.join(map(str,ar2[0])) + "\n")
                        tppf3.write(' '.join(map(str,ar4[0])) + "\n")


            tppf.close()
            tppf1.close()
            tppf2.close()
            tppf3.close()

