importos,sys
fromscipyimportstats
importnumpyasnp

f=open('deepak/hh102/hh102_hh113source_final_1.csv','r').readlines()
N=len(f)-1
#foriinrange(0,N):
w=f[0].split()
printw

l1=w[1:8]
l2=w[8:]
try:
,list1=[float(x)forxinl1]
,list2=[float(x)forxinl2]
exceptValueError,e:
,print"error",e,"online",i
result=stats.ttest_ind(list1,list2)
printresult[1]
