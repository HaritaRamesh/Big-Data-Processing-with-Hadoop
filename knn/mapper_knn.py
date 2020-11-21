# !/usr/bin/env python3
import sys
import pandas as pd
import numpy as np
import csv
import sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

with open('train.csv', 'w') as file:
    for line in sys.stdin:
        file.write(line)

#train = pd.read_csv('train.csv', encoding='unicode_escape')
#test = pd.read_csv('Test.csv', encoding='unicode_escape')

#X_train = train.iloc[:, :48]
#Y_train = train.iloc[:, 48:]

#X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size=0.2)

train = pd.read_csv('train.csv',encoding='unicode_escape')
test = pd.read_csv('test_norm.csv',encoding='unicode_escape')
#train = pd.read_csv('Train.csv',encoding='unicode_escape')
train1 = train.head(40941)
#train1 = train.head(20)
#test = train.tail(15)
X_train = train1.iloc[:, 1:49]
Y_train = train1.iloc[:, 49:]
#print(Y_train)
Y_train = Y_train.astype({'48':'int32'})
#print(Y_train)
test = test.iloc[:, 1:49]
#print(Y_train.typ)
#X_test = test.iloc[:, 1:49]
#Y_test = test.iloc[:, 49:]
#Y_test = Y_test.astype({'48':'int32'})
#Y_test.to_csv('y_pred.csv',encoding='utf-8')

# x_train = []
# y_train = []
# x_test = []
# for line in sys.stdin:
#    line = line.rstrip()
#    list_of_elements = line.split(',')
#    list_of_elements = list(map(float,list_of_elements))
#    if len(list_of_elements) == 49:
#        x_train.append(list_of_elements[:47])
#        y_train.append(list_of_elements[48])
#        if len(list_of_elements) == 48:
#            x_test.append(list_of_elements[:47])
#        X_train = np.array(x_train)
#        Y_train = np.array(y_train)
#        X_test = np.array(x_test)
#        Y_train = Y_train.reshape(Y_train.shape[0],1)

X_train = X_train.to_numpy()
Y_train = Y_train.to_numpy()


# X_test = test.to_numpy()


# function that calculates euclidean distance using tile
def euclidean(X_test, center):
    z = pd.np.tile(center, (len(X_test), 1))
    ans = np.subtract(X_test, z)
    ans = pow(ans, 2)
    ans = np.sum(ans, axis=1)
    ans = np.sqrt(ans)
    return ans


def normalize(X):
    scaler = MinMaxScaler()
    scaler.fit(X)
    norm_X = scaler.transform(X)
    return norm_X


# K-NEAREST NEIGHBOR FUNCTION
def KNN(X_train, X_test, Y_train):
    """
  :type X_train: numpy.ndarray
  :type X_test: numpy.ndarray
  :type Y_train: numpy.ndarray

  :rtype: numpy.ndarray
  """
    #X_train = normalize(X_train)
    #X_test = normalize(X_test)
    i = 0
    out = []
    labels = []
    for train_sample in X_train:
        ans = euclidean(X_test, train_sample)
        out.append(ans)
        labels.append(Y_train[i][0])
        i += 1
    out1 = np.array(out).transpose()
    #print(out1.shape)
    #print(len(labels))
    #print(len(out1))
    #print(len(out1[0]))
    for i in range(len(out1)):
        for j in range(len(out1[0])):
            #print(i,j)
            #print("%s,%s,%s"%(str(i), out1[i,j],str(labels[j])))
            print(str(i), out1[i,j], str(labels[j]))

        #t = " ".join(str(a) for a in ans)
        #print(t + " " + str(Y_train[i][0]))



KNN(X_train, test, Y_train)
