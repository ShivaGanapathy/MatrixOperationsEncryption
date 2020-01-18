#!/usr/bin/env python
# coding: utf-8

# In[5]:


#ShivaG
#01/19/2019

from MATHBOT import finalstring
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# message to matrix
message = finalstring
print(message)
finalstring=""
listone = []
tempvar = 0
templist = []

for x in range(len(message)):
    
    templist.append(message[x])
    tempvar +=1
    if tempvar == 3:
        listone.append(templist)
        tempvar = 0
        templist = []
    
print("# message to matrix")
print(listone)
print("------------")    


# Making the encoding chart
string = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-\",().?/\@%#$"
encoding_chart = {}
for x in range(len(string)):
        encoding_chart[string[x]] = x

        
        
        
# letter matrix to number matrix
for x in range(len(listone)):
    for y in range(3):
        listone[x][y] = encoding_chart[listone[x][y]]
dfone = pd.DataFrame(listone)

print("# letter matrix to number matrix")
print (dfone)
print("------------")    


#Matrix Muliplication

mainmatrix = np.matrix(dfone.T)
threebythreeinverse = np.matrix('1 11 14; 0 -1 -1; 0 -3 -4')
listone = (threebythreeinverse * mainmatrix).T.tolist()

print("#Matrix Muliplication")  
print(listone)
print("------------")    

#mod-ing
def mod(x):
    if x > 49:
        x -= 50
        return(mod(x))
        
    elif x < 0:
        x += 50
        return(mod(x))
        
    if x > -1 and x < 50:
        return x
        
        
for x in range(24):
    for y in range(3):
        if listone[x][y] > 49 or listone[x][y] < 0:
            listone[x][y] = mod(listone[x][y])
print("#mod-ing")            
print(listone)
print("------------")

# Back into Letter Matrix
encoding_chart = {}
for x in range(len(string)):
        encoding_chart[x] = string[x]
        
for x in range(len(listone)):
    for y in range(3):
        listone[x][y] = encoding_chart[listone[x][y]]
        
print("# Back into Letter Matrix")
print(listone)
print("------------")
      
# The Final Step Yay
finalstring = ""
for x in range(len(listone)):
    for y in range(3):
        finalstring +=(listone[x][y])
print(finalstring)


# In[ ]:




