from __future__ import absolute_import

from pymt.framework.bmi_bridge import bmi_factory

from .bmi import Cem

Cem = bmi_factory(Cem)

del bmi_factory
