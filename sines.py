"""
 The main File of this project

 The specs of this project are as follows:

 1.  It will be a script which will parse some options
 2.  The script will plot some sine waves, variable number
 3.  Optionally, we can save the plot to a file of many formats
 4.  Script should check that the validity of the arguments
 5.  Add an argument for a legend (-l)

usage:

    python sines.py -n 3 -l -f file.png
"""

def check_args(options):
    """ 4. Return a Boolean check of the arguments"""
    pass

def sine_plot(n):
    """ 2. This plots the sine waves and returns an axis object"""
import matplotlib.pyplot as plt
import numpy as np
import random

x = np.linspace(0,10,50)
n = 8
S = []
Legend = []
color_cycles=['r','g','b','y','c','m','k', 'o']

for i in range(n):
    phi = random.random()*2*np.pi
    A = random.random()
    y = A*np.sin(x + phi)
    S.append(y)

for i in range(n):
    t = "-"+color_cycles[i]    
    plt.plot(x, S[i], t)
    name = 'sin' + str(i+1)
    Legend.append(name)
    
plt.legend(Legend)
plt.title('Sine waves with diffrent amplitudes')
plt.xlabel('X (pi)')
plt.xlim((0, 5))
plt.ylabel('Sine')
plt.ylim((-1, 1))
plt.rc('lines', linewidth=1)
plt.show()





#plt.savefig(os.path.join(plot_dir, 'plot_example1.png'))
    #pass



def main(options):
    """ The main function 

    3.  Plot to a file
    5.  Add a legend"""
    pass


if __name__ == '__main__':
    # 1. parse options
    main(options)

