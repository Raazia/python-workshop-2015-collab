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

def check_args(options):
    """ 4. Return a Boolean check of the arguments"""
    pass

def sine_plot(n):
    """ 2. This plots the sine waves and returns an axis object"""
    pass

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

def main(options):
    """ The main function 
    3.  Plot to a file
    5.  Add a legend"""
    pass


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

