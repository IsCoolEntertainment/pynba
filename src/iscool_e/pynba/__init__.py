# -*- coding: utf-8 -*-
"""
    IsCool-e Pynba
    ~~~~~~~~~~~~~~

    :copyright: (c) 2015 by IsCool Entertainment.
    :license: MIT, see LICENSE for more details.
"""

import warnings
from pynba.wsgi import monitor, pynba, PynbaMiddleware

warnings.warn('This package is deprecated, use http://pypi.python.org/pypi/pynba', DeprecationWarning)  # noqa

__version__ = '0.5.0'
__all__ = ['monitor', 'pynba', 'PynbaMiddleware']
