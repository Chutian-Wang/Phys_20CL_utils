from matplotlib.ticker import AutoMinorLocator
import numpy as np

def setAx(axs):
    if hasattr(axs, '__iter__'):
        for ax in axs:
            ax.xaxis.set_minor_locator(AutoMinorLocator())
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            ax.minorticks_on()
            ax.tick_params(which='major', length=4, width=1, direction='in')
            ax.tick_params(which='minor', length=2, width=1, direction='in')
    else:
        axs.xaxis.set_minor_locator(AutoMinorLocator())
        axs.yaxis.set_minor_locator(AutoMinorLocator())
        axs.minorticks_on()
        axs.tick_params(which='major', length=4, width=1, direction='in')
        axs.tick_params(which='minor', length=2, width=1, direction='in')
            
def chisq(exp, obs, err, dof = 1):
    return (((exp-obs)/ err) ** 2).sum() / (obs.size - dof)

def parseUnc(_str):
    val, unc = _str.split('±')
    return np.array([float(val), float(unc)])

def RMSD(data, exp = None):
    if exp == None:
        exp = data.mean()
    return ((data - exp)**2/data.size).sum()**0.5