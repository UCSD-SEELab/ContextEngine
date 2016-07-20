import numpy as np
import math
import scipy
import Anomaly
import sys
sys.path.append("..")
from ContextEngineBase import *



class Anom(ContextEngineBase):
    Thresh = 0
        
    def __init__(self, numInputs, outputClassifier, inputClassifiers, appFieldsDict):
        ContextEngineBase.__init__(self, numInputs, outputClassifier, inputClassifiers, appFieldsDict)
        

    #  Add a set of training observations, with the newInputObsMatrix being a
    #  matrix of doubles, where the row magnitude must match the number of inputs,
    #  and the column magnitude must match the number of observations.
    #  and newOutputVector being a column vector of doubles
    def addBatchObservations(self, newInputObsMatrix, newOutputVector):
        if(len(newInputObsMatrix.shape) == 2 and newInputObsMatrix.shape[1] == self.numInputs
            and newOutputVector.shape[0] == newInputObsMatrix.shape[0]):
            newOutputVector = newOutputVector.ravel();
            i = 0;
            for newInputVector in newInputObsMatrix:
                newOutputValue = newOutputVector[i];
                self.addSingleObservation(newInputVector, newOutputValue);
                i += 1;
        else:
            print("Wrong dimensions!");

    # Train function computes the anomaly detection threshold.
    def train(self):
        if(self.numObservations > 0):
            print("Training Started");
            # Use module from Anomaly detection
            self.Thresh = Anomaly.AnomThresh(self.observationMatrix);
            # remove the data, so that new data can be added (next cycle)
            del self.observationMatrix
            self.numObservations = 0
            return True;
        else:
            print("Not enough observations to train");
            return False;
    # Execute: reports anomaly by returning 1, if the input is larger than 
    # the threshold that was computed during training.
    def execute(self,inputObsVector):
        if inputObsVector > self.Thresh:
            return 1
        return 0



