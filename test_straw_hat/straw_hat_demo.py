import numpy as np
from ebo_core.ebo import ebo
from test_straw_hat.straw_hat import StrawHat
import numpy.matlib as nm
import time

## define test function ##
f = StrawHat()
dx = 2
x_range = nm.repmat([[-15.],[15.]], 1, dx)
print(x_range)
# run ebo
options = {'x_range':x_range, # input domain
           'dx':x_range.shape[1], # input dimension
           'max_value':f.f_value, # target value
           'T':10, # number of iterations
           'B':10, # number of candidates to be evaluated
           'dim_limit':3, # max dimension of the input for each additive function component
           'isplot':1, # 1 if plotting the result; otherwise 0. 
           'z':None, 'k':None, # group assignment and number of cuts in the Gibbs sampling subroutine
           'alpha':1., # hyperparameter of the Gibbs sampling subroutine
           'beta':np.array([5.,2.]), 
           'opt_n':1000, # points randomly sampled to start continuous optimization of acfun
           'pid':'test3', # process ID for Azure
           'datadir':'tmp_data/', # temporary data directory for Azure
           'gibbs_iter':10, # number of iterations for the Gibbs sampling subroutine
           'useAzure':False, # set to True if use Azure for batch evaluation
           'func_cheap':True, # if func cheap, we do not use Azure to test functions
           'n_add':None, # this should always be None. it makes dim_limit complicated if not None.
           'nlayers': 100, # number of the layers of tiles
           'gp_type':'l1', # other choices are l1, sk, sf, dk, df
           'gp_sigma':0.1, # noise standard deviation
           'n_bo':10, # min number of points selected for each partition
           'n_bo_top_percent': 0.5, # percentage of top in bo selections
           'n_top':10, # how many points to look ahead when doing choose Xnew
           'min_leaf_size':10, # min number of samples in each leaf
           'max_n_leaves':10, # max number of leaves
           'thresAzure':1, # if batch size > thresAzure, we use Azure
           'save_file_name': 'tmp/tmp.pk',
           }

e = ebo(f, options)
start = time.time()
e.run()
print("elapsed time: ", time.time() - start)
