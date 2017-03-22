'''
Implements functionality to combine multiple visualizers
into a single layout, either as a basis for small 
multiples or as a dashboard of unrelated visualizers
'''

##########################################################################
## Imports
##########################################################################

## Hoist visualizers into the multivisualizer namespace
from .base import *
from .multiscatter import *
