# Copyright (c) 2017- Uber Technologies, Inc.
# Copyright (c) 2020- AI-CPS@UniTS
# Copyright (c) 2020- Emanuele Ballarin <emanuele@ballarin.cc>
# SPDX-License-Identifier: Apache-2.0

from pyro.optim.optim import PyroOptim
from pyromaniac.optim.torch import AdamWCD as pt_AdamWCD


def AdamWCD(optim_args):
    """
    Wraps :class:`pyromaniac.optim.adamwcd.AdamWCD` with :class:`~pyro.optim.optim.PyroOptim`.
    """
    return PyroOptim(pt_AdamWCD, optim_args)
