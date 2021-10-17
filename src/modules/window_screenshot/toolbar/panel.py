# -*- coding: utf-8 -*-
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

from .button import ToolbarButton
from .language.container import ToolbarLanguageContainerWidget


class ToolbarWidget(QtWidgets.QScrollArea):
    actionScreenshot = QtCore.pyqtSignal(object)

    def __init__(self):
        super(ToolbarWidget, self).__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.setWidgetResizable(True)

        self.setContentsMargins(0, 0, 0, 0)

        self.container = QtWidgets.QWidget()
        self.container.setLayout(QtWidgets.QHBoxLayout())
        self.container.layout().setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.setWidget(self.container)

        self.grabber = ToolbarButton(self, "Grab text", QtGui.QIcon('icons/screenshot'))
        self.grabber.clicked.connect(self.actionScreenshot.emit)
        self.container.layout().addWidget(self.grabber)

        self.languages = ToolbarLanguageContainerWidget()
        self.container.layout().addWidget(self.languages)

    def reload(self, event=None):
        self.languages.reload()
