# Copyright (C) Duncan Macleod (2013)
#
# This file is part of GWpy.
#
# GWpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GWpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GWpy.  If not, see <http://www.gnu.org/licenses/>.

"""Module providing classes for reading, writing and manipulating
time-series and spectrum data.
"""

from .. import version
__author__ = "Duncan Macleod <duncan.macleod@ligo.org>"
__version__ = version.version

from .nddata import *
from .array import *
from .array2d import *
from .series import *
from glue.lal import (Cache, CacheEntry)

__all__ = ['Array', 'Array2D', 'Series', 'Cache', 'CacheEntry']

