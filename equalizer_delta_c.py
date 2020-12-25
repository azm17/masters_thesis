# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

TE,RE,PE,SE=1.5,1.0,0.0,-0.5
eta_c = (RE - PE) / (TE + RE - PE - SE)
eta_list = [eta for eta in np.linspace(0, eta_c, 100)]

delta_c1 = lambda eta: (TE - RE) / ((1 - eta) * (RE - PE) - eta * (TE - SE) + TE - RE)
delta_c2 = lambda eta: (TE - RE) / ((1 - eta) * (RE - PE) - eta * (TE - SE) + TE - RE)

delta_c_list = [max(delta_c1(eta), delta_c2(eta)) for eta in eta_list]


plt.rcParams["xtick.direction"] = "in"  
plt.rcParams["ytick.direction"] = "in"  
plt.ylim(0, 1)
plt.xlim(0, 0.5)
plt.xlabel('$\eta = \epsilon+\\xi$', fontsize = 18)
plt.ylabel('$\delta_c$', fontsize = 18)
plt.plot(eta_list, delta_c_list, '-', color = '#1f77b4', markersize = 1)

plt.savefig('./figure/equalizer_delta_c.pdf')