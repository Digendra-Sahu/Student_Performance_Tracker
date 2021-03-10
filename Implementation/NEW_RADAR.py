''' this module will be used for plotting radar chart '''
from cosolidated_data import *
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

my_data = data_for_graph()
first_ps = list(my_data.keys())[0]
topper = top_performer()
bottom = bottom_performer()
