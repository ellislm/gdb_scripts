import gdb

import sys
import os
sys.path.insert(1, os.path.expanduser("~") + '/.gdb.d')
sys.path.insert(1, os.path.expanduser("~") + '/.gdb.d/Boost-Pretty-Printer')

from eigen_printer import register_eigen_printers
import boost
register_eigen_printers (None)
boost.register_printers()
