# -*- coding: utf-8 -*-

import numpy.linalg as LA
import matplotlib.pyplot as plt
import random

def D(p,q,f,epsilon,xi,delta):
    tau, mu, eta = 1-2*epsilon-xi, 1-epsilon-xi, epsilon+xi
    
    M_prime= [[delta*(tau*p[1]*q[1]+epsilon*p[1]*q[2]+epsilon*p[2]*q[1]+xi*p[2]*q[2])-1+(1-delta)*p[0]*q[0],
               delta*(mu*p[1]+eta*p[2])-1+(1-delta)*p[0],
               delta*(mu*q[1]+eta*q[2])-1+(1-delta)*q[0],
               f[0]],
    
              [delta*(epsilon*p[1]*q[3]+xi*p[1]*q[4]+tau*p[2]*q[3]+epsilon*p[2]*q[4])+(1-delta)*p[0]*q[0],
               delta*(eta*p[1]+mu*p[2])-1+(1-delta)*p[0],
               delta*(mu*q[3]+eta*q[4])  +(1-delta)*q[0],
               f[1]],
              
              [delta*(epsilon*p[3]*q[1]+tau*p[3]*q[2]+xi*p[4]*q[1]+epsilon*p[4]*q[2])+(1-delta)*p[0]*q[0],
               delta*(mu*p[3]+eta*p[4])  +(1-delta)*p[0],
               delta*(eta*q[1]+mu*q[2])-1+(1-delta)*q[0],
               f[2]],
              
              [delta*(xi*p[3]*q[3]+epsilon*p[3]*q[4]+epsilon*p[4]*q[3]+tau*p[4]*q[4])+(1-delta)*p[0]*q[0],
               delta*(eta*p[3]+mu*p[4])+(1-delta)*p[0],
               delta*(eta*q[3]+mu*q[4])+(1-delta)*q[0],
               f[3]]]
    
    return LA.det(M_prime)

def create_Fig():
    TE, RE, PE, SE = 1.5, 1.0, 0.0, -0.5 # payoff
    Sx, Sy = [RE,SE,TE,PE],[RE,TE,SE,PE] # payoff vector
    xi = 0                       # error rate
    epsilon_list = [0, 0.1, 0.2] # error rate
    v1 = [1,1,1,1]               # one vector
    
    # strategies setting
    WSLS = [[1,1,0,0,1], [1,1,0,0,1], [1,1,0,0,1]]
    ALLD = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    # contingentExtortion1  = [[0,0.86,0.77,0.09,0], [0,0.65575, 0.31825, 0.34575, 0.00825]] # chi=15
    # contingentExtortion09 = [[0,0.955556,0.855556,0.1,0], [0.0825, 0.719444, 0.344444, 0.375, 0]]# chi=15
    contingentExtortion1  = [[0,0.73,0.535,0.195,0], [0,0.781375, 0.537625, 0.246375, 0.002625], [0,0.876, 0.551, 0.341, 0.016]] # chi=10
    contingentExtortion09 = [[0, 0.811111, 0.594444, 0.216667, 0], [0,0.868194,0.597361,0.27375,0.00291667], [0,0.973333, 0.612222, 0.378889, 0.0177778]] # chi=10
    equalizer1  = [[1,2/3,1/3,2/3,1/3], [0.5,2.5/3,0.595238,0.404762,0.5/3],[0.5,2.5/3,0.416667,0.583333,0.5/3]]
    equalizer09 = [[1/2,2/3,0.277778,0.722222,1/3], [0.5,2.5/3,0.515873,0.484127,0.5/3], [0.5,2.5/3,0.277778,0.722222,0.5/3]]
    
    # playerX's strategies
    p_list_all = [WSLS, contingentExtortion1, equalizer1, ALLD, WSLS, contingentExtortion09, equalizer09, ALLD]
    # playerY's strategies
    q_list = [[random.random(), random.random(), random.random(), random.random(), random.random()] for i in range(1000)]
    
    # calculate payoff
    sx_list_all =[]; sy_list_all =[]
    sx_list_all_alld =[]; sy_list_all_alld =[]
    sx_list_all_allc =[]; sy_list_all_allc =[]
    for i, p_list in enumerate(p_list_all):
        if i in [0, 1, 2, 3]: delta = 1
        else: delta = 0.9
        sx_list =[]; sy_list =[]
        sx_list_alld =[]; sy_list_alld =[]
        sx_list_allc =[]; sy_list_allc =[]
        for j, p in enumerate(p_list):
            sx = []; sy = []
            epsilon = epsilon_list[j]
            for q in q_list:
                vdot1 = D(p,q,v1,epsilon,xi,delta)
                sx.append(D(p,q,Sx,epsilon,xi,delta)/vdot1)
                sy.append(D(p,q,Sy,epsilon,xi,delta)/vdot1)
            vdot1_allc = D(p,[1,1,1,1,1],v1,epsilon,xi,delta)
            vdot1_alld = D(p,[0,0,0,0,0],v1,epsilon,xi,delta)
            sx_list.append(sx)
            sy_list.append(sy)
            sx_list_alld.append(D(p,[0,0,0,0,0],Sx,epsilon,xi,delta)/vdot1_alld)
            sy_list_alld.append(D(p,[0,0,0,0,0],Sy,epsilon,xi,delta)/vdot1_alld)
            sx_list_allc.append(D(p,[1,1,1,1,1],Sx,epsilon,xi,delta)/vdot1_allc)
            sy_list_allc.append(D(p,[1,1,1,1,1],Sy,epsilon,xi,delta)/vdot1_allc)
        
        sx_list_all.append(sx_list)
        sy_list_all.append(sy_list)
        sx_list_all_alld.append(sx_list_alld)
        sy_list_all_alld.append(sy_list_alld)
        sx_list_all_allc.append(sx_list_allc)
        sy_list_all_allc.append(sy_list_allc)
    
    # generate figure
    fig = plt.figure(figsize=(12, 6.5))
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    gs  = fig.add_gridspec(2, 4)
    axs = []
    for i in range(2):
        for j in range(4):
            axs.append(fig.add_subplot(gs[i, j:j+1]))
    
    text_list  = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    strategy_list = ['WSLS', 'Contingent Extortion', 'Equalizer', 'ALLD',
                     'WSLS', 'Contingent Extortion', 'Equalizer', 'ALLD']
    
    # plot
    for i in range(8):
        axs[i].set_aspect('equal')
        axs[i].set_ylim([-0.6, 1.6])
        axs[i].set_xlim([-0.6, 1.6])
        axs[i].set_ylabel(f'Payoff of {strategy_list[i]}')
        axs[i].text(-0.7, 1.8, '{}'.format(text_list[i]), fontsize=20)
        axs[i].plot([RE, TE, PE, SE, RE], [RE, SE, PE, TE, RE], color = "grey", alpha=0.5, zorder=1)
        axs[i].plot([RE, PE], [RE, PE], color = "grey", alpha=0.5, linestyle='dashed', zorder=1)
        axs[i].set_xticks([-0.5, 0.0, 0.5, 1.0, 1.5])
        axs[i].set_yticks([-0.5, 0.0, 0.5, 1.0, 1.5])
        axs[i].set_xlabel('Payoff of Opponent')
        # vs 1000 strategies
        if i in [2,3,6,7]:
            axs[i].scatter(sy_list_all[i][0], sx_list_all[i][0], s=10, c='k', zorder=2)
        else:
            axs[i].scatter(sy_list_all[i][0], sx_list_all[i][0], s=1, c='k', zorder=2)
        if i in [2,3,6,7]:
            axs[i].scatter(sy_list_all[i][1], sx_list_all[i][1], s=5, c='limegreen', zorder=2)
        else:
            axs[i].scatter(sy_list_all[i][1], sx_list_all[i][1], s=1, c='limegreen', zorder=2)
        axs[i].scatter(sy_list_all[i][2], sx_list_all[i][2], s=1, c='c', zorder=2)
        # vs ALLC ALLD
        for j in range(3):
            axs[i].scatter(sy_list_all_allc[i][j], sx_list_all_allc[i][j], s=3, c='b', zorder=2)
            axs[i].scatter(sy_list_all_alld[i][j], sx_list_all_alld[i][j], s=3, c='r', zorder=2)
    
    # figure setting
    axs[0].tick_params(labelbottom=False, right=True, top=True)
    axs[1].tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False, right=True, top=True)
    axs[2].tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False, right=True, top=True)
    axs[3].tick_params(labelbottom=False, labelleft=False, labelright=False, labeltop=False,right=True, top=True)
    axs[4].tick_params(right=True, top=True)
    axs[5].tick_params(labelleft=False, labelright=False, labeltop=False, right=True, top=True)
    axs[6].tick_params(labelleft=False, labelright=False, labeltop=False, right=True, top=True)
    axs[7].tick_params(labelleft=False, labelright=False, labeltop=False, right=True, top=True)
    
    # save figure
    fig.savefig('./figure/figure.pdf', bbox_inches='tight',pad_inches=0.05) 

if __name__ == "__main__":
    create_Fig()
    