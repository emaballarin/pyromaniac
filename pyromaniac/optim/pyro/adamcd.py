# Copyright (c) 2017- Uber Technologies, Inc.
# Copyright (c) 2020- AI-CPS@UniTS
# Copyright (c) 2020- Emanuele Ballarin <emanuele@ballarin.cc>
# SPDX-License-Identifier: Apache-2.0

from pyro.optim.optim import PyroOptim
from pyromaniac.optim.torch import AdamCD as pt_AdamCD


def AdamCD(optim_args):
    """
    Wraps :class:`pyromaniac.optim.adamwcd.AdamCD` with :class:`~pyro.optim.optim.PyroOptim`.
    """
    return PyroOptim(pt_AdamCD, optim_args)
