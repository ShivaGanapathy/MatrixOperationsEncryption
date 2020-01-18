#!/usr/bin/env python
# coding: utf-8

# In[66]:


#ShivaG
#01/19/2019
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# example message to matrix: 
message = "\"WHEN PLAN A FAILS, REMEMBER THERE ARE 25 OTHER LETTERS IN THE ALPHABET\"."
print("The initial message:")
print(message)
print(" ")
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
    
        


dfone = pd.DataFrame(listone)






# letter matrix to number matrix
string = " ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-\",().?/\@%#$"
encoding_chart = {}
for x in range(len(string)):
        encoding_chart[string[x]] = x
        
        
        

for x in range(len(listone)):
    for y in range(3):
        listone[x][y] = encoding_chart[listone[x][y]]
        
#print(listone)
dfone = pd.DataFrame(listone)


# Matrix Multiplication



threebythree = np.matrix('1 2 3; 0 -4 1; 0 3 -1')
mainmatrix = np.matrix(dfone.T)
#print(threebythree)
#print(mainmatrix)
listone = (threebythree * mainmatrix).T.tolist()
#print(listone)

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
            
#print(listone)

# Back into Letter Matrix
encoding_chart = {}
for x in range(len(string)):
        encoding_chart[x] = string[x]
        
for x in range(len(listone)):
    for y in range(3):
        listone[x][y] = encoding_chart[listone[x][y]]
        
#print(listone)

# The Final Step Yay
finalstring = ""
for x in range(len(listone)):
    for y in range(3):
        finalstring +=(listone[x][y])
print("The Encrypted Message After Matrix Operations and Encoding:")
print(finalstring)


# In[ ]:




