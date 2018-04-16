#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial

In this example, we create a simple
window in PyQt5.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':

    APP = QApplication(sys.argv)

    W = QWidget()
    W.resize(500, 500)
    W.move(500, 300)
    W.setWindowTitle('Ganadería')
    W.show()

    sys.exit(APP.exec_())
