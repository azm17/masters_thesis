# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

TE,RE,PE,SE=1.5,1.0,0.0,-0.5
eta_c = (RE - PE) / (TE + RE - PE - SE)
eta_list_max = [eta for eta in np.linspace(0, eta_c, 1000)]
delta_list = [1.0, 0.9, 0.8, 0.7, 0.6 ,0.5]

chi_c1 = lambda eta, delta: 1 + (1-delta+2*delta*eta)*(TE-SE) / (delta*((1-eta)*(RE-PE)-eta*(TE-SE))-(1-delta)*(TE-RE))
chi_c2 = lambda eta, delta: 1 + (1-delta+2*delta*eta)*(TE-SE) / (delta*((1-eta)*(RE-PE)-eta*(TE-SE))-(1-delta)*(PE-SE))

delta_c1 = lambda eta: (TE - RE) / ((1 - eta) * (RE - PE) - eta * (TE - SE) + TE - RE)
delta_c2 = lambda eta: (TE - RE) / ((1 - eta) * (RE - PE) - eta * (TE - SE) + TE - RE)

chi_c_list =[]
eta_list = []
for delta in delta_list:
    tmp_chi_list = []
    tmp_eta_list = []
    for eta in eta_list_max:
        if max(delta_c1(eta), delta_c2(eta)) < delta:
            tmp_chi_list.append(max(chi_c1(eta, delta), chi_c2(eta, delta)))
            tmp_eta_list.append(eta)
    eta_list.append(tmp_eta_list)
    chi_c_list.append(tmp_chi_list)

plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.ylim(0, 20)
plt.xlim(0, 0.5)
plt.xlabel('$\eta = \epsilon+\\xi$', fontsize = 18)
plt.ylabel('$\chi_c$', fontsize = 18)

for i, chi_c in enumerate(chi_c_list): 
    plt.plot(eta_list[i], chi_c, '-', markersize = 1, label='{}'.format(delta_list[i]))

plt.legend(fontsize=12,title='$\delta$',).get_title().set_fontsize(12)

plt.savefig('./figure/pcZD_chi_c.pdf')