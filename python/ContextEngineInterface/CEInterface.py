import gdp
from ioClass import ioClass
import numpy as np

# checkDictKeys: checks existance of all of the required keys
# to instantiate a GDP read or write.
def checkDictKeys(d):
    if 'gcl' in d and 'param' in d and 'lag' in d and 'norm' in d:
        return
    else:
        raise ValueError ('I/O dictionary does not contain required'\
                          ' keys: gclName, paramName, lag, norm')

# This class creates an interface instance for Context Engine.
# each input as well as output is defined with gcl log name, JSON 
# parameter in that log, their lag from current sample and 
# normalization model. For training and testing, a range of 
# record numbers is specified.
class ceInterface(object):
    def __init__(self, numInputs = None, inDicts = None, outDict = None):
        if numInputs is None:
            raise ValueError ('Number of inputs must be provided.')

        if inDicts is None:
            raise ValueError ('Input description dictionary list'\
                              ' must be provided.')
        elif len(inDicts) != numInputs:
            raise ValueError ('Length of input description dictionary'\
                              ' list and '\
                              'number of inputs mismatch: %d and %d'\
                              % (len(inTuples), numInputs))
        else:
            for d in inDicts:
                if isinstance(d, dict):
                    checkDictKeys(d)
                else:
                     raise ValueError ('Input description must be a'\
                                       ' dictionary object')

        if outDict is None:        
            raise ValueError ('Output description dictionary'\
                              ' must be provided.')
        elif isinstance(outDict, dict):
            checkDictKeys(outDict)
        else:
             raise ValueError ('Output description must be a'\
                               ' dictionary object')

        # Create an array of ioClass objects for input, and single ioClass
        # for output. Each ioClass will be used later on with their gdcHandle
        # to access GDP data.
        self.inObjs = []
        for d in inDicts:
            self.inObjs.append(ioClass(d['gcl'], d['param'], d['lag'], d['norm']))
        self.outObj = ioClass(outDict['gcl'], outDict['param'],
                              outDict['lag'], outDict['norm'])
    # collectData: Collect (training) data for all inputs and output objects.
    def collectData(self, start, stop):
        inData = []
        for inObj in self.inObjs:
            trace = inObj.readLog(start, stop)
            inData.append(trace)
        outData = self.outObj.readLog(start, stop)
        return np.array(inData).T, np.array(outData)
    # This function is used to initalize subscription to GDP logs.
    # NOTE: this function is incomplete.
    def streamInputInit (self, idx):
        if idx == -1:
            raise ValueError ('Subscription is not defined for output.')
        if idx >= self.numInputs:
            raise ValueError ('Subscription index out of bound (idx > numInputs).')
        self.inObjs[idx].subscribeLog()
        return
