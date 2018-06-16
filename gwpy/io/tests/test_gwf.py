# -*- coding: utf-8 -*-
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

"""Unit tests for :mod:`gwpy.io.gwf`
"""

import pytest

from ...tests.utils import (TEST_GWF_FILE, skip_missing_dependency)
from ...tests.mocks import mock
from .. import gwf as io_gwf

__author__ = 'Duncan Macleod <duncan.macleod@ligo.org>'

TEST_CHANNELS = [
    'H1:LDAS-STRAIN', 'L1:LDAS-STRAIN', 'V1:h_16384Hz',
]


def mock_call(*args, **kwargs):
    raise OSError("")


def test_identify_gwf():
    assert io_gwf.identify_gwf('read', TEST_GWF_FILE, None) is True
    with open(TEST_GWF_FILE, 'rb') as gwff:
        assert io_gwf.identify_gwf('read', None, gwff) is True
    assert not io_gwf.identify_gwf('read', None, None)


@skip_missing_dependency('lalframe')
def test_iter_channel_names():
    # maybe need something better?
    from types import GeneratorType
    names = io_gwf.iter_channel_names(TEST_GWF_FILE)
    assert isinstance(names, GeneratorType)
    assert list(names) == TEST_CHANNELS
    with mock.patch('gwpy.utils.shell.call', mock_call):
        names = io_gwf.iter_channel_names(TEST_GWF_FILE)
        assert isinstance(names, GeneratorType)
        assert list(names) == TEST_CHANNELS


@skip_missing_dependency('lalframe')
def test_get_channel_names():
    assert io_gwf.get_channel_names(TEST_GWF_FILE) == TEST_CHANNELS


@skip_missing_dependency('lalframe')
def test_num_channels():
    assert io_gwf.num_channels(TEST_GWF_FILE) == 3


@skip_missing_dependency('lalframe')
def test_get_channel_type():
    assert io_gwf.get_channel_type('L1:LDAS-STRAIN',
                                   TEST_GWF_FILE) == 'proc'
    with pytest.raises(ValueError) as exc:
        io_gwf.get_channel_type('X1:NOT-IN_FRAME', TEST_GWF_FILE)
    assert str(exc.value) == ('X1:NOT-IN_FRAME not found in '
                              'table-of-contents for %s' % TEST_GWF_FILE)


@skip_missing_dependency('lalframe')
def test_channel_in_frame():
    assert io_gwf.channel_in_frame('L1:LDAS-STRAIN', TEST_GWF_FILE) is True
    assert io_gwf.channel_in_frame('X1:NOT-IN_FRAME',
                                   TEST_GWF_FILE) is False
