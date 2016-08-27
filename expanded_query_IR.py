#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# @author     : SRvSaha
# Filename    : expanded_query_IR.py
# Timestamp   : 16:00 27-August-2016 (Saturday)
# Description : SCRIPT to extact all the expanded queries from IR Query
# Requirement : Python 3, Word2vec, Gensim
#

import logging
import sys
import os
import heapq
import time
import threading
import re
import numpy
import scipy.spatial.distance 
from numpy import linalg as LA
from sklearn.cluster import KMeans

try: 
    from queue import Queue
except ImportError:
    from Queue import Queue

from numpy import exp, dot, zeros, outer, random, dtype, get_include, float32 as REAL,\
    uint32, seterr, array, uint8, vstack, argsort, fromstring, sqrt, newaxis, ndarray, empty

logger = logging.getLogger("gensim.models.word2vec")

from gensim import utils, matutils  # utility fnc for pickling, common scipy operations etc
from six import iteritems, itervalues, string_types
from six.moves import xrange
from gensim.models.word2vec import Word2Vec  

if __name__ == "__main__":

    # check and process cmdline input
    program = os.path.basename(sys.argv[0])
    
   
    seterr(all='raise')  # don't ignore numpy errors
    try:    
        filename = sys.argv[1]
	if len(sys.argv)<2:
	    raise
    except:
	print "Argument Missing. Pass filename as argument"
	sys.exit(1)
    try:
    	inputfile = open(filename).read()
    except Exception:
	print "Could not open file, invalid filename"
	sys.exit(1)
    testSet = inputfile.split("\n") # For getting all lines in a list testSet
    model = Word2Vec.load_word2vec_format('/home/workstation/Mizo_vectors.bin', binary=True)
    
    fout = open("./similarity_output.txt",'w')   
    count = 1
    for testString in testSet[:-1]: # For reading each line from testSet
	testString = testString.split('\t')[1] # Since there will be query number and the query tab separeted, so we need take the query part only
	for word in testString.split(' '): # Each words in query separated by space are taken
	    fout.write(str(count)+"\t"+word+"\n")
	    similarity = model.most_similar(positive=[word], topn=3) # Finding the most similar top 3 results. This will be a list
	    for result in similarity: # For writing the result in required format in a string
		result = str(result) # Since it will be a tuple, we need to convert it to string
		out = str(count)+"\t"+(result.split(', ')[0])[3:-1]+"\t"+(result.split(', ')[1])[:-1]+"\n" # Getting values from tupples. Stripping is done to remove useless u annd () and '
		#print out
		fout.write(out) # Writing to the output file
	count += 1
    fout.close() # closing the file and releasing the resources
    print "Operation Successful :)"
		    
 
