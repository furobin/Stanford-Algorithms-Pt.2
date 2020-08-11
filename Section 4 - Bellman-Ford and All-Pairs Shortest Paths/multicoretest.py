# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:17:01 2020

@author: foobe
"""

#%
import os
def set_path():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

set_path()

#%% Multi-core processing
import time
import multiprocessing


def somefunc(x):
    if x % 2 == 0:
        return 'even'
    else:
        return 'damn'
    
def multiprocessing_func(x): 
    print (f'{x} squared reseults in a/an {somefunc(x**2)} number')
    
def otherfunc(x):
    print(x, " + ", x, "=", x + x)
    return 'x + x =' + str(x + x)
    
if __name__ == '__main__':
    
    startime = time.time()
    processes = []
    for i in range(50):
        p = multiprocessing.Process(target = otherfunc, args = [i, i**5,])
        processes.append(p)
        p.start()
        
    for process in processes: #makes sure process finishes before moving on in script
        process.join()
        
    print('Processor method took {} seconds'.format(time.time() - startime))
    
#%% Pool Method

import concurrent.futures 

def test(x):
    return x + x

with concurrent.futures.ProcessPoolExecutor() as executor:
    results = executor.map(test, [1,2,3]) #schedules func to be exectured, returns future obj
    for result in results:
        print(result)
        
