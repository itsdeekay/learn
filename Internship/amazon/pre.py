import numpy as np
import random


if __name__ == "__main__":
    langs = ["de","fr","jp","en"] 
    product = ["books","dvd","music"]

    for p in range (len(langs)):
        for j in range (len(product)):
                current_input_directory = '%s/%s' %(langs[p],product[j])
                file = current_input_directory +'/train.processed_data.txt'
                data = np.loadtxt(file,delimiter=" ")
                size=data.size        #Number of elements
                col=data[0].size        #No. of columns
                row=size/col          #No. of rows
                class_s = data[:,col_s-1]
                unique_sc,counts = np.unique(class_s, return_counts = True)
                
                for i in range(16):
                    tppf_s = open(current_input_directory+'/Source/Source_%d.txt' %(i+1),'w')
                    tppf_t = open(current_input_directory+'/Target/Target_%d.txt' %(i+1),'w')
       
                    for j in range(len(unique_sc)):
                        if counts[j]<100:
                            continue
                        idx =  data[:,col-1]==unique_sc[j]
                        temp = data[idx,:]
                        rand = random.sample(range(0,len(temp)),100)
                        temp = temp[rand,:]
                        for each in temp:                        
                            temps = ' '.join([str(a1) for a1 in each])
                            tppf_s.write(temps+'\n')
                    
                    for j in range(len(unique_sc)):
                        if counts[j]<10:
                            continue
                        idx =  data[:,col-1]==unique_sc[j]
                        temp = data[idx,:]
                        rand = random.sample(range(0,len(temp)),10)
                        temp = temp[rand,:]
                        for each in temp:                        
                            temps = ' '.join([str(a1) for a1 in each])
                            tppf_t.write(temps+'\n')
                        
                    tppf_s.close()
                    tppf_t.close()