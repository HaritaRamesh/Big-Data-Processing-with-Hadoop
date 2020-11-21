#!/usr/bin/env python3
import sys
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

neighbors = []
labels = []
truest_labels =[]

true_labels = pd.read_csv('y_pred.csv',encoding='unicode_escape')
true_labels_arr = true_labels.to_numpy()
for i in true_labels_arr:
    truest_labels.append(i[1])
print(truest_labels)

for line in sys.stdin:

        line = line.rstrip()
        #print(line)
        lst = line.split(" ")
        neighbors.append(lst)

#print(neighbors)
knn_dict = dict()

for neighbor in neighbors:
    if neighbor[0] in knn_dict:
        # append the new dict to the existing array at this slot
        knn_dict[neighbor[0]].append(dict({'distance':float(neighbor[1]), 'label':neighbor[2]}))
    else:
        # create a new array in this slot
        knn_dict[neighbor[0]] = [dict({'distance': float(neighbor[1]), 'label':neighbor[2]})]

#print(knn_dict)
out = {}
pred = []

#print(knn_dict.keys())
for key in knn_dict:
    train_samples = knn_dict[key]
    train_samples1 = sorted(train_samples, key = lambda k:k['distance'],reverse=True)[:5]
    #print(train_samples1)
    temp = []
    for t in train_samples1:
        temp.append(t['label'])
    #print(temp)
    label = int(max(set(temp), key=temp.count))
    out.update({key:label})
    print(key, label)
out1 = dict(sorted(out.items()))
for key,values in out1.items():
    pred.append(values)
print(pred)
print(accuracy_score(truest_labels,pred))














