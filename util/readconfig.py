"""
Created on March 29, 2018

@author: Rajnikant Rakesh
This function read config file specified in parameter.
It reads file from default location of config directory in this project.
file name without path needs to be passed as argument.
Returns a dictionary of type propertyname:value
"""
import ConfigParser
import argparse
import logging
import os


def readconfig(configfile, sec):
    configdict = {}
    cwd = os.path.dirname(os.path.abspath(__file__))
    try:
        #Check Windows Path
        if cwd.find("\\") > 0:
            folderup = cwd.rfind("\\")
            configfilewithpath = cwd[:folderup]+"\\config\\"+configfile
        #Else go with linux path
        else:
            folderup = cwd.rfind("/")
            configfilewithpath = cwd[:folderup]+"/config/"+configfile
        
        config = ConfigParser.RawConfigParser()
        config.read(configfilewithpath)
        options = config.options(sec)
    except:
        logging.error("Error reading config file {}".format(configfilewithpath))
        raise
    for option in options:
        try:
            configdict[option] = config.get(sec, option)
        except:
            print 'Exception!! could not find value for {}'.format(option)
            configdict[option] = None
    return configdict
