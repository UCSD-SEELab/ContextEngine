import gdp
import json
# Input/output class. Identifies the gcl_name and parameter_name for each input or output.

# collectTrace: collects a trace of data in record number range (start, stop)
# from GDP log that is pointed to by gclHandle. The key ["data"][param] is
# extracted from the JSON entries, and returned.
def collectTrace(gclHandle, param, start, stop):
    # this is the actual subscribe call
    gclHandle.multiread(start, stop-start+1)

    # timeout
    t = {'tv_sec':0, 'tv_nsec':500*(10**6), 'tv_accuracy':0.0}
    data = []
    while True:
        # This could return a None, after the specified timeout
        event = gdp.GDP_GCL.get_next_event(t)
        if event is None or event["type"] == gdp.GDP_EVENT_EOS:
            break
        datum = event["datum"]
        handle = event["gcl_handle"]
        data.append(float(json.loads(datum['data'])[param]))
    return data

# Context Engine IO class: provides interface with sources and destinations
# of data.
# As of now, input interface is limited to GDP, while a summary of output
# can be printed out to the console, or the results can be published to
# a GDP log.
class ioClass(object):
    def __init__(self, nameStr = "", paramName = "", lagVal = 0, normMeth = 'none'):
        if nameStr == "":
            raise ValueError ("GCL name must be provided.")
        if paramName == "":
            raise ValueError ("JSON parameter name must be provided.")
        # Log name in GDP
        self.gclName = gdp.GDP_NAME(nameStr)
        # Assume that GCL already exists and create the GCL handle
        self.gclHandle = gdp.GDP_GCL(self.gclName, gdp.GDP_MODE_RO)
        # JSON parameter name to be used in each log record
        self.param = paramName
        # Lag from the current record. Can be used to implement time series functions.
        self.lag = lagVal
        # Normalization method for data:
        # 'none': no normalization
        # 'lin': linear normalization: mean-zeroed and divided by std
        self.norm = normMeth
        # Normalization parameters (i.e., avg, std etc.)
        self.normParam = {}

    def printTester(self):
        print self.gcl, self.param, self.lag
    # readLog: reads a GDP log in (start, stop) range.
    def readLog(self, start, stop): 
        param = self.param
        handle = self.gclHandle            
        lag = self.lag
        # Applying lag parameter.
        trace = collectTrace(handle, param, start - lag, stop - lag)
        return trace
    # subscribeLog: subscribe to log for receiving data updates. 
    # NOTE: This function is incomplete.
    def subscribeLog(self):
        self.gclHandle.subscribe(0, 0, None)

