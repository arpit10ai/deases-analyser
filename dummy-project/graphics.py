# Load libraries
import numpy as np
from numpy import genfromtxt
from sklearn import linear_model
# Load dataset
file=(genfromtxt("Book2.csv",delimiter=',',dtype='str'))  


dic={}
count=0
for val in file:
    if val[5] not in dic:
        dic[val[5]]=count
        count+=1

print(dic)

for val in file:
    val[5]=dic[val[5]]


trainingset=file[:28]
testingset=file[28:]

trainingx=trainingset[:,[0,1,2,3,4]]
trainingx=trainingx.astype(float)
trainingy=trainingset[:,[5]]

testingx=testingset[:,[0,1,2,3,4]]
testingx=trainingx.astype(float)
testingy=testingset[:,[5]]


lr=linear_model.LogisticRegression()
lr.fit(trainingx,trainingy)

x=[56,34,123,87,65]

print("predicted value is" + str(lr.predict([x])))
print("real value is"+str([x]))

#lr.score(testingx,testingy)*100



