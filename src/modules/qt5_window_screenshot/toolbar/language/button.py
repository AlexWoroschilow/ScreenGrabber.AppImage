# Copyright 2015 Alex Woroschilow (alex.woroschilow@gmail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class ToolbarLanguageButton(QtWidgets.QToolButton):
    def __init__(self, parent=None, text=None, icon=None, code=None):
        super(ToolbarLanguageButton, self).__init__(parent)
        assert (text is not None)
        assert (icon is not None)
        assert (code is not None)

        self.code = code

        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setIconSize(QtCore.QSize(20, 20))
        self.setIcon(QtGui.QIcon(icon))
        self.setMinimumWidth(28)
        self.setMaximumHeight(24)
        self.setCheckable(True)
        self.setToolTip(text)
