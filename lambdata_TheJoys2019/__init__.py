#!/usr/bin/env python

"""
lambdata - a collection of Data Science helper functions
"""

import pandas as pd
import numpy as np
import example_module
import null_doctor
import datetime_doctor

Y = example_module.increment(example_module.x)
TEST = pd.DataFrame(np.ones(10))