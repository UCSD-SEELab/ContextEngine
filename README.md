# ContextEngine
Context Engine implementation in Python 2.7
# Introduction
Context Engine is a middleware tool that creates a unified interface for 
different Internet of Things (IoT) applications. This goal is mainly 
accomplished by accommodating machine learning algorithms in proximity of data 
generation (i.e., on embedded devices and sensors). These low end devices 
create several challenges, as they have limited memory, processing capability, 
communication bandwidth, and availability. Furthermore, a huge number of these 
devices are required in several modern day IoT applications, which creates 
other challenges in scalability. Context Engine tackles this problem by 
breaking down large applications into smaller multi-input-single-output 
components, and using general purpose machine learning algorithms to implement 
functionality of each element. This can help by breaking large application 
specific blocks into multiple blocks that produce intermediate variables that 
can be used by other applications as well.

# Dependencies and Required Libraries prior to use
In this section we list the libraries that are required prior to using Context Engine.
Except from general libraries such as numpy and scipy, we are using KMeans implementation
from sklearn to provide input and output clustering.

To provide interface with GDP, we are using the python gdp API that is created by 
SwarmLab at UC Berkeley. This library and its dependencies are therefore required to
provide GDP interface.

In case other algorithms are goind to be used within the Context Engine platform,
the dependencies of them should also be met.

Libraries:
1. numpy
2. scipy
3. sklearn (for KMeans in ContextEngineBase.py)
4. gdp
   -Please contact SwarmLab at UC Berkeley to access GDP implementation.
   -All of the gdp dependencies must be met prior to accessing GDP data
	using Context Engine's GDP interface. 


# Testing and sample applications
Testing scripts are provided in the "test" directory.

-baseTest_GDP_Historic.py
	This script provides general purpose testing for different 
	algorithms. Timestamps are saved during the running of the script
	to give a report of running time of each part in the end.

	interfaceDict:
	Each input or output is define by a dictionary which
	containg the log name, parameter name, lag value, and normalization
	method. This information is saved in interfaceDict, which is used
	in Context Engine initialization.
	
	ceDict: 
	contains all of the parameters (including interfaceDict) that should 
	be passed to the Context Engine.
	
	algorithmTest:
	This is an object of the algorithm class that we are testing.
	Number of inputs and ceDict, as well as whether each I/O is 
	discrete is required to initalize the Context Engine Object.
	Classifier values that are set to 0 show a continues I/O, while
	any other positive number shows the number of predifined states
	for that port. KMeans is used on training data to find these
	states.
	
	trainRecStart, trainRecStop, testRecStart, testRecStop:
	These values set the bounds for training set and test set.
	The values are provided as record numbers.
	In the future time should be incorporated instead of record
	numbers.

-gdpAnomalyHistoric.py
	This script is similar to previous one in structure.
	In this script the output is a dummy variable, as anomaly
	detection is performed unsupervised. 

	batchSize:
	Training is performed on a dataset of last batchSize data records.
	After this, the next batch of data is evaluated using the threshold
	that was computed from previous batch. 

	Some of the induced anomalies that are detectable with this script:
	-Heating immersion room back BLEE:
		- param: temperature_celcius
		- norm: lin
		- continous input and output
		- trainRecStart = 1041000
		- trainRecStop = 1057300
		- batchSize = 1500


	

	

