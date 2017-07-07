import numpy as np
import random


if __name__ == "__main__":
    houses = [102,113,118]

    for p in range (len(houses)):
        for j in range (len(houses)):
            if(p!=j):
            
                current_input_directory = 'deepak/hh%d/hh%d_hh%d' %(houses[p],houses[p],houses[j])
                source_adj = '%s/Source_sampled_100.csv' %(current_input_directory)
                target_adj = '%s/Target_sampled_10.csv' %(current_input_directory)
                data_s = np.loadtxt(source_adj,delimiter=",")
                data_t = np.loadtxt(target_adj,delimiter=",")
                size_s=data_s.size
                size_t = data_t.size        #Number of elements
                col_s=data_s[0].size        #No. of columns
                col_t=data_t[0].size
                row_s=size_s/col_s          #No. of rows
                row_t = size_t/col_t
                class_s = data_s[:,col_s-1]
                class_t = data_t[:,col_t-1]
                unique_sc = np.unique(class_s)
                unique_tc = np.unique(class_t)
                
                for i in range(16):
                    tppf_s = open(current_input_directory+'/Source_%d.txt' %(i+1),'w')
                    tppf_t = open(current_input_directory+'/Target_%d.txt' %(i+1),'w')
       
                    for j in range(len(unique_sc)):
                        idx =  data_s[:,col_s-1]==unique_sc[j]
                        temp = data_s[idx,:]
                        rand = random.sample(range(0,len(temp)),100)
                        temp = temp[rand,:]
                        for each in temp:                        
                            temps = ' '.join([str(a1) for a1 in each])
                            tppf_s.write(temps+'\n')
                    
                    for j in range(len(unique_tc)):
                        idx =  data_t[:,col_t-1]==unique_tc[j]
                        temp = data_t[idx,:]
                        rand = random.sample(range(0,len(temp)),10)
                        temp = temp[rand,:]
                        for each in temp:                        
                            temps = ' '.join([str(a1) for a1 in each])
                            tppf_t.write(temps+'\n')
                        
                tppf_s.close()
                tppf_t.close()