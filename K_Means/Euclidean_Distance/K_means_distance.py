import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random



class k_means():
    def __init__(self):
        '''
        This class implements K-means algoritm.
        
        To train the model call fit() function.
        
        To Predict call predict() function.
        
        '''
        pass
        
    
    def Search_Rnk(self,learn_data,shp,first = 0):
        
        if first==0:
            self.Rnk = []
            self.centroid = np.empty((self.k,shp[-1]))
            for i in range(self.k):
                for j in range(shp[-1]):
                    self.centroid[i,j] = random.randrange(int(min(learn_data[:,j])),int(max(learn_data[:,j])))

        
        
        for i in range(shp[0]):
            dist = np.sum(np.square(self.centroid-np.array([learn_data[i,:]]*self.k)),axis=-1)
            
            if np.shape(self.Rnk)[0]!=shp[0]:
                self.Rnk.append(np.where(dist==min(dist))[0][0])
            else:
                self.Rnk[i] = np.where(dist==min(dist))[0][0]

        self.Rnk = np.reshape(self.Rnk,(-1,1))
    
    def Find_Centroids(self,learn_data):
        
        for j in range(self.k):
    
            idx = np.where(self.Rnk == j)[0]
    
            self.centroid[j,:] = np.sum(learn_data[idx,:],axis= 0)/np.shape(idx)[0]
    
    def fit(self,X,k,iteration):
        
        self.k = k
        self.made_cluster = 1
        
        for i in range(iteration):
            
            self.Search_Rnk(learn_data=X,shp = np.shape(X),first = i)
            
            self.Find_Centroids(learn_data=X)
            
    def predict(self,data):
        
        try:
            test = self.made_cluster
        except:
            print('You need to train the model first..........')
        else:
            
            pred_Rnk = []
            
            shp = np.shape(data)
            
            for i in range(shp[0]):
                dist = np.sum(np.square(self.centroid-np.array([data[i,:]]*self.k)),axis=-1)
            
                pred_Rnk.append(np.where(dist==min(dist))[0][0])

            pred_Rnk = np.reshape(pred_Rnk,(-1,1))
            
            return pred_Rnk
            
            
            

