"""
one function lists all books
one function lists one book

if name == __main__
run locally = easy way

import bookdb.py to VM, run it = much harder
run it in wsgi-ref (easier, but with 8080 suffix)
mod-wsgi is harder (has to do with sys.path) but doesn't have suffix (will look for python modules to import, sys.path can help with this)
"""