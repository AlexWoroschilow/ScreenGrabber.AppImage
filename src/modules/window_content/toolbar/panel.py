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
import inject
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class ToolbarWidget(QtWidgets.QWidget):
    actionCleanup = QtCore.pyqtSignal(object)
    actionScreenshot = QtCore.pyqtSignal(object)
    actionExport = QtCore.pyqtSignal(object)
    actionSave = QtCore.pyqtSignal(object)
    actionOpen = QtCore.pyqtSignal(object)

    @inject.params(config='config')
    def __init__(self, config=None):
        super(ToolbarWidget, self).__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.setContentsMargins(0, 0, 0, 0)

        from .button import ToolbarButton

        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setAlignment(Qt.AlignLeft)

        self.open = ToolbarButton(self, "Open file", QtGui.QIcon('icons/open'))
        self.open.clicked.connect(self.actionOpen.emit)
        self.open.clicked.connect(self.reload)
        self.layout().addWidget(self.open, -1)

        self.save = ToolbarButton(self, "Save", QtGui.QIcon('icons/save'))
        self.save.clicked.connect(self.actionSave.emit)
        self.save.clicked.connect(self.reload)
        self.layout().addWidget(self.save, -1)

        self.export = ToolbarButton(self, "Save as", QtGui.QIcon('icons/export'))
        self.export.clicked.connect(self.actionExport.emit)
        self.export.clicked.connect(self.reload)
        self.layout().addWidget(self.export, -1)

        self.mode = ToolbarButton(self, "...", QtGui.QIcon('icons/append'))
        self.mode.clicked.connect(self.onToggleMode)
        self.mode.clicked.connect(self.reload)
        self.layout().addWidget(self.mode, -1)

        self.cleaner = ToolbarButton(self, "Letters only", QtGui.QIcon('icons/letters'))
        self.cleaner.clicked.connect(self.onToggleCleaner)
        self.cleaner.clicked.connect(self.reload)
        self.layout().addWidget(self.cleaner, -1)

        self.lowercase = ToolbarButton(self, "Lowercase", QtGui.QIcon('icons/lowercase'))
        self.lowercase.clicked.connect(self.onToggleLowercase)
        self.lowercase.clicked.connect(self.reload)
        self.layout().addWidget(self.lowercase, -1)

        self.cleanup = ToolbarButton(self, "Cleanup", QtGui.QIcon('icons/trash'))
        self.cleanup.clicked.connect(self.actionCleanup.emit)
        self.cleanup.clicked.connect(self.reload)
        self.layout().addWidget(self.cleanup, -1)

        self.reload()

    @inject.params(config='config')
    def reload(self, event=None, config=None):
        self.mode.setChecked(int(config.get('content.append', 1)))
        self.lowercase.setChecked(int(config.get('cleaner.uppercase', 0)))
        self.cleaner.setChecked(int(config.get('cleaner.extrachars', 0)))
        self.open.setChecked(False)
        self.save.setChecked(False)
        self.cleanup.setChecked(False)
        self.export.setChecked(False)

        self.mode.setText('Append text' if self.mode.isChecked() else 'Replace text')
        self.mode.setIcon(QtGui.QIcon('icons/append') if self.mode.isChecked() else QtGui.QIcon('icons/replace'))

    @inject.params(config='config')
    def onToggleCleaner(self, event, config=None):
        config.set('cleaner.extrachars', int(event))

    @inject.params(config='config')
    def onToggleLowercase(self, event, config=None):
        config.set('cleaner.uppercase', int(event))

    @inject.params(config='config')
    def onToggleMode(self, event, config=None):
        config.set('content.append', int(event))
