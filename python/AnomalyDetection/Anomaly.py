# This is the python version of the S-H-ESD algorithm,
# origininally implemented by twitter in R. 
# Original implementation reports a list of most anomalous data.
# We have changed the functionality to fullfill our needs. We first
# perform the designated preprocessing on the training data (a batch),
# and then compute a threshold. This threshold is used to find anomalies
# in the next batch of data.
import csv
import numpy as np
import scipy
import math

# This function performs S-H-ESD preprocessing to remove seasonality.
# Afterwards, a threshold is defined that is used to find anomalies.
def AnomThresh(data):
    ares = [];
    i = 0;
    while(i < len(data)):
        ares.append(abs(data[i]))
        i = i+1;
    datasigma = np.median(ares);

    i = 0;
    while(i < len(data)):
        ares[i] = ares[i] / datasigma;
        i = i + 1;

    newSigma = np.median(ares)

    thresh = 3*newSigma 
    return thresh


