# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 18:45:55 2020

@author: foobe
"""

#%
import os
def set_path():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

set_path()

#%%
import random 

def write_test(size = 150, n = 25):
    f = open("knaptest3.txt", "w")
    f.write(str(size) + " " + str(n) + "\n")
    for i in range(100):
        val = random.randint(1, 1000)
        weight = random.randint(1, size)
        f.write(str(val) + " " + str(weight) + "\n")

write_test()