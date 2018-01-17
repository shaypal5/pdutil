"""Utilities for pandas."""

import pdutil.display
import pdutil.iter
import pdutil.transform

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

for name in ['get_versions', '_version', 'pdutil', 'name']:
    try:
        globals().pop(name)
    except KeyError:
        pass
