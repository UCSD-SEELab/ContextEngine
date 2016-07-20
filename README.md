# ContextEngine
Context Engine implementation in Python 2.7
# Add a brief description

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


# Describe how to test, different test vectors. Make a test case that accepts sys.argv


