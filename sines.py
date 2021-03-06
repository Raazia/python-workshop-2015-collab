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
import argparse
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import random

def check_args(options):
    """ 4. Return a Boolean check of the arguments"""
    
    #check if the number of variables is an integer        
    try:
        num = int(options.num)
    except: 
        print "number of arguments must be a whole number"
        return False

    if num < 0:   
        print "the number of arguments must be a positive number"        
        return False
    if num > 10:   
        print "too many sines, must be fewer than 10"
        return False
        
    #check to see if the file exists
    if options.file and os.path.exists(options.file):
        print "File exists"
        return False
    
    return True


def sine_plot(n):
    """ 2. This plots the sine waves and returns an axis object"""
    x = np.linspace(0,10,50)
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
        
    #plt.legend(Legend)
    plt.title('Sine waves with diffrent amplitudes')
    plt.xlabel('X (pi)')
    plt.xlim((0, 5))
    plt.ylabel('Sine')
    plt.ylim((-1, 1))
    plt.rc('lines', linewidth=1)
    #plt.show()
    return Legend

def create_parser():
    """ Create a parser to use"""
    parser = argparse.ArgumentParser(prog="Program Script")    
    parser.add_argument('-n', dest="num", 
                        help="number of sines plotted")
    parser.add_argument('-f', dest="file",
                        help="save as file")
    parser.add_argument('-l', dest="legend", action="store_true",
                        help="legend")
    
    return parser


def print_name():
    print ("my name is .....")

def main(options):
    """ The main function 
    3.  Plot to a file
    5.  Add a legend"""

    if not check_args(options):
        print "Arg Errors. Exiting"
        sys.exit(1)

    legend = sine_plot(int(options.num))

    if options.file:
        plt.savefig(options.file)
        print "Has the figure been saved? {}".format(os.path.exists(options.file))

    if options.legend:
        plt.legend(legend)

    plt.show()

if __name__ == '__main__':   
    
    parser = create_parser()
    """
        Now we have defined what arguments the script takes, parse the arguments provided
        this defaults to sys.argv.  This returns a Namespace object, which is a simple object
        with the arguments as attributes
    """
    options = parser.parse_args()  
    
    """
        Now do whatever the script needs to do
    """
    main(options)
    

