#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) Stefan Countryman (2018)
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
#

"""Transfer Function Plot
"""

try:
    from matplotlib.cm import plasma as DEFAULT_CMAP
except ImportError:
    DEFAULT_CMAP = None

from .spectrogram import Spectrogram

__author__ = 'Stefan Countryman <stefan.countryman@ligo.org>'

class Transfergram(Spectrogram):
    """Plot a transfer function spectrogram between two timeseries.
    """
    MIN_DATASETS = 2
    MAX_DATASETS = 2
    action = 'transfergram'

    def _finalize_arguments(self, args):
        if args.color_scale is None:
            args.color_scale = 'linear'
        if args.color_scale == 'linear':
            if args.imin is None:
                args.imin = 0.
            if args.imax is None:
                args.imax = 1.
        if args.cmap is None and DEFAULT_CMAP is not None:
            args.cmap = DEFAULT_CMAP.name
        return super(Transfergram, self)._finalize_arguments(args)

    def get_ylabel(self):
        """Text for y-axis label
        """
        return 'Frequency (Hz)'

    def get_suptitle(self):
        """Start of default super title; includes channel names being compared.
        """
        return ("Transfer Function Spectrogram: "
                "{0} vs {1}").format(*self.chan_list)

    def get_color_label(self):
        if self.args.norm:
            return 'Normalized to {}'.format(self.args.norm)
        return 'Magnitude'

    def get_spectrogram(self):
        args = self.args
        fftlength = float(args.secpfft)
        overlap = args.overlap  # fractional overlap
        stride = self.get_stride()
        self.log(2, "Calculating transfer function spectrogram, "
                    "secpfft: {}, overlap: {}".format(fftlength, overlap))

        if overlap is not None:  # overlap in seconds
            overlap *= fftlength

        return self.timeseries[0].transfer_spectrogram(
            self.timeseries[1],
            stride,
            fftlength=fftlength,
            overlap=overlap,
            window=args.window
        )