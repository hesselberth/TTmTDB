#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 17:57:35 2025

@author: Marcel Hesselberth
"""


JD2000 = 2451545.0
REF2000 = 9.930573125973422e-05


def test_import():
    from ttmtdb import TTmTDB
    import ttmtdb


def test_1_arg():
    from  ttmtdb import TTmTDB
    dt2000 = TTmTDB(2451545.0)
    assert(abs((dt2000-REF2000) < 1e-20))


def test_2_args():
    from  ttmtdb import TTmTDB
    dt1 = TTmTDB(JD2000)
    dt2 = TTmTDB(JD2000, 0)
    dt3 = TTmTDB(JD2000, 1)
    assert(dt1 == dt2)
    assert(dt2 != dt3)
    assert(abs(dt2 - dt3) < 3e-5)


def test_inpop():
    from inpop import Inpop
    from  ttmtdb import TTmTDB
    import numpy as np
    ip = Inpop()
    for i in range(-36500, 36500):
        assert( abs(ip.TTmTDB(np.array([JD2000, 1])) - TTmTDB(JD2000, 1)) < 2e-7 )


from  ttmtdb import TTmTDB
dt1 = TTmTDB(JD2000, 1/12)
print(dt1)