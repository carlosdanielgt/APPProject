import os
import sys
import glob
from os.path import basename, isfile, join

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# dynamically import all strategies
strategiesdir = join(parent, 'strategies')
modules = glob.glob(join(strategiesdir, "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f)
           and not f.endswith('__init__.py')]
