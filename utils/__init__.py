import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chi2

from .CSVexplorer import CSVexplorer
from .functions import chisq, setAx, parseUnc, RMSD

# Some Re:0 colors, color blind proof.
# It works with gray scale, too.
# Also pretty cute :P
colors = [
    (143/255,  78/255, 180/255),#purple
    ( 71/255, 142/255, 219/255),#blue
    (208/255, 134/255, 188/255),#pink
    (218/255, 165/255,  93/255),#orange
]