#! /usr/bin/env python


from ._cem import Cem

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
