# Copyright (c) 2020- AI-CPS@UniTS
# Copyright (c) 2020- Emanuele Ballarin <emanuele@ballarin.cc>
# SPDX-License-Identifier: Apache-2.0

import numpy as np


def sched_sss(start_lr: float, stop_lr: float, nr_decays):
    r"""Obtain the canonical scheduling parametrization from the start/stop/step one.

    Arguments:
        start_lr (float): initial learning rate
        stop_lr (float): final learning rate
        nr_decays: number of learning rate decay steps
    """

    return (start_lr), (np.power((stop_lr / start_lr), (1.0 / nr_decays)).item())


def sched_ssse(start_lr: float, stop_lr: float, nr_decays, epochs: int):
    r"""Obtain the canonical scheduling parametrization from the start/stop/step one, with explicit epoch specification.

    Arguments:
        start_lr (float): initial learning rate
        stop_lr (float): final learning rate
        nr_decays: number of learning rate decay steps
        epochs (int): number of total learning epochs
    """

    return (sched_sss(start_lr, stop_lr, nr_decays)), int(epochs // nr_decays)
