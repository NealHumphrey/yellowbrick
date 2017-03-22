
##########################################################################
## Imports
##########################################################################
import math
import numpy as np
import matplotlib.pyplot as plt

from yellowbrick.multivisualizer.base import MultiVisualizer
from yellowbrick.features.scatter import ScatterVisualizer


##########################################################################
## Quick Methods
##########################################################################

class MultiClassScatter(MultiVisualizer):
	def __init__(self, axarr = None, features = None, classes = None, 
				color = None, colormap = None, **kwargs):

		'''
		Note, WIP haven't sufficiently handled edge cases
		'''
		nrows = kwargs.pop('nrows',math.ceil(len(classes) / 2))
		ncols = kwargs.pop('ncols',2)

		if axarr == None:
			fig, axarr = plt.subplots(nrows, ncols, squeeze = False)

		self.features_ = features
		self.classes_ = classes
		self.color= color
		self.colormap= colormap

		visualizers = []
		for c in self.classes_:
			viz = ScatterVisualizer(ax=None,classes=[c],color=self.color,
				colormap=self.colormap, title = c)
			visualizers.append(viz)

		super(MultiClassScatter, self).__init__(visualizers=visualizers,
				axarr = axarr, nrows=nrows, ncols=ncols)

