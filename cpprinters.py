import sys
import os
#sys.path.insert(0, '<path_to_libcxx-pp_src_dir>')
CPPRINTERS_FILE = os.path.abspath(os.path.expanduser(__file__))
while os.path.islink(CPPRINTERS_FILE):
         PEDAFILE = os.path.abspath(os.path.join(os.path.dirname(CPPRINTERS_FILE), os.path.expanduser(os.readlink(CPPRINTERS_FILE))))

#print("{}".format(CPPRINTERS_FILE))
sys.path.insert(0, os.path.join(os.path.dirname(CPPRINTERS_FILE), 'src'))
from libcxx.v1.printers import register_libcxx_printers
register_libcxx_printers (None)
