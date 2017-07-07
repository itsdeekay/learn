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

houses = [102,118,120]

for w in range (len(houses)):
		for s in range (len(houses)):
			if(w!=s):
				current_input_directory = 'datasets/hh%d/hh%d_hh%d' %(houses[w],houses[w],houses[s])
				input1 = '%s/noDup_prob_source.csv' %(current_input_directory)
				input2 = '%s/noDup_tree_path_vectors_source.csv' %(current_input_directory)
				input3 = '%s/noDup_prob_target.csv' %(current_input_directory)
				input4 = '%s/noDup_tree_path_vectors_target.csv' %(current_input_directory)
				tppf = open(current_input_directory + 'source_final.csv','w+')
				tppf2 = open(current_input_directory + 'source_distributions.csv','w+')

				tppf1 = open(current_input_directory + 'target_final.csv','w+')
				tppf3 = open(current_input_directory + 'target_distributions.csv','w+')

				c=[]
				e=[]

				d=[]
				f=[]		


				with open(input1,'r') as fp:
					for line in fp:
						a=[]
						a=line.split('\n')
						a[0]=a[0].replace(',', ' ')
						c.append(a[0])


				with open(input3,'r') as fp1:
					for line1 in fp1:
						b=[]
						b=line1.split('\n')
						b[0]=b[0].replace(',', ' ')
						d.append(b[0])
						
						
				with open(input2,'r') as fp2:
					for line2 in fp2:
						g=[]
						g=line2.split('\n')
						e.append(g[0])


				with open(input4,'r') as fp3:
					for line3 in fp3:
						h=[]
						h=line3.split('\n')
						f.append(h[0])

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
					print k
					ar1=c[k].split(' ')
					for i in range(0,len(ar1)):
						ar2[0][i]=float(ar1[i])
					for j in range(0,len(d)):
						ar3=d[j].split(' ')
						for l in range(0,len(ar3)):
							ar4[0][l]=float(ar3[l])						
						if(J.Jensen_Shannon_divergence(ar2[0], ar4[0])==1.0):
							print "hello found"
							tppf.write(' '.join(map(str,e[k])) + "\n")
							tppf1.write(' '.join(map(str,f[j])) + "\n")
							print str(ar2[0])
							print str(ar4[0])
							tppf2.write(' '.join(map(str,ar2[0])) + "\n")
							tppf3.write(' '.join(map(str,ar4[0])) + "\n")


				tppf.close()
				tppf1.close()
				tppf2.close()
				tppf3.close()


