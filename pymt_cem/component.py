from __future__ import absolute_import

from pymt.framework.bmi_bridge import bmi_factory

from .bmi import Cem, Waves

Cem = bmi_factory(Cem)
Waves = bmi_factory(Waves)

del bmi_factory
