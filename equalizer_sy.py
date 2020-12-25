# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

TE,RE,PE,SE=1.5,1.0,0.0,-0.5
eta_c = (RE - PE) / (TE + RE - PE - SE)
eta_list = [eta for eta in np.linspace(0, eta_c, 100)]

sY1 = lambda eta: ((1-eta)*PE-eta*SE)/(1-eta-eta)
sY2 = lambda eta: ((1-eta)*RE-eta*TE)/(1-eta-eta)

sY1_list = [sY1(eta) for eta in eta_list]
sY2_list = [sY2(eta) for eta in eta_list]

plt.rcParams["xtick.direction"] = "in"  
plt.rcParams["ytick.direction"] = "in"  
plt.ylim(0, 1)
plt.xlim(0, 0.5)
plt.xlabel('$\eta = \epsilon+\\xi$', fontsize = 18)
plt.ylabel('$s_Y$', fontsize = 18)
plt.plot(eta_list, sY1_list, '-', color = '#1f77b4', markersize = 1)
plt.plot(eta_list, sY2_list, '-', color = '#1f77b4', markersize = 1)

plt.savefig('./figure/equalizer_sy.pdf')