#!/usr/bin/env python
from __future__ import absolute_import

import os
import sys
import cell2mol

if __package__ == "":
    path = os.path.dirname(os.path.dirname(__file__))
    sys.path.insert(0, path)


from cell2mol import c2m_driver


if __name__ == "__main__":
    sys.exit()
