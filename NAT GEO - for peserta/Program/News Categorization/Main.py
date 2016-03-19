# from __future__ import division
from NaiveBayes import NaiveBayes
import Preprocessing

__author__ = 'undeed'

inputDataTrain = 'Data Train.xlsx'
inputDataTest = 'Data Test.xlsx'

preprocessedData = "dataset_preprocessing.xlsx"
model = "model_classification.xlsx"
outputResult = "RESULT CLASS.xlsx"


# print "preprocess file"
# Preprocessing.preprocessFile(inputDataTrain, preprocessedData)
#
nb = NaiveBayes(model)
#
# print "start learning"
# nb.learning(inputDataTrain, preprocessedData)
# print "stop learning"

print "start testing"
nb.testing(inputDataTest, outputResult)



