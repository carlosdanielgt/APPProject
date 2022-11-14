from importlib import import_module
from pkgutil import iter_modules
from inspect import isclass
import os
import sys
import glob
from os.path import basename, isfile, join

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
# dynamically import all strategies
strategiesdir = join(parent, 'strategies')
sys.path.append(strategiesdir)

modules = glob.glob(join(strategiesdir, "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f)
           and not f.endswith('__init__.py')]
all_strategies = __all__


# iterate through the modules in the current package
package_dir = strategiesdir
for (_, module_name, _) in iter_modules([package_dir]):

    # import the module and iterate through its attributes
    module = import_module(f"strategies.{module_name}")
    for attribute_name in dir(module):
        attribute = getattr(module, attribute_name)

        if isclass(attribute):
            # Add the class to this package's variables
            globals()[attribute_name] = attribute
