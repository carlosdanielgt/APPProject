import os
import sys
from os.path import join

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
strategiesdir = join(parent, 'strategies')
sys.path.append(strategiesdir)
