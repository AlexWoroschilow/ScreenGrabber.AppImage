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
import functools

import hexdi
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class ToolbarWidget(QtWidgets.QScrollArea):
    actionScreenshot = QtCore.pyqtSignal(object)

    @hexdi.inject('config')
    def __init__(self, config=None):
        super(ToolbarWidget, self).__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.setWidgetResizable(True)

        self.setContentsMargins(0, 0, 0, 0)

        from .button import ToolbarButton

        self.container = QtWidgets.QWidget()
        self.container.setLayout(QtWidgets.QHBoxLayout())
        self.container.layout().setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.setWidget(self.container)

        self.grabber = ToolbarButton(self, "Grab text", QtGui.QIcon('icons/screenshot'))
        self.grabber.clicked.connect(self.actionScreenshot.emit)
        self.grabber.setCheckable(False)
        self.addWidget(self.grabber)

        self.english = ToolbarButton(self, "English", QtGui.QIcon('icons/english'))
        self.english.clicked.connect(functools.partial(self.onLanguageChanged, 'eng'))
        self.english.clicked.connect(self.reload)
        self.addWidget(self.english)

        self.german = ToolbarButton(self, "German", QtGui.QIcon('icons/german'))
        self.german.clicked.connect(functools.partial(self.onLanguageChanged, 'deu'))
        self.german.clicked.connect(self.reload)
        self.addWidget(self.german)

        self.spanish = ToolbarButton(self, "Spanish", QtGui.QIcon('icons/spanish'))
        self.spanish.clicked.connect(functools.partial(self.onLanguageChanged, 'spa'))
        self.spanish.clicked.connect(self.reload)
        self.addWidget(self.spanish)

        self.russian = ToolbarButton(self, "Russian", QtGui.QIcon('icons/russian'))
        self.russian.clicked.connect(functools.partial(self.onLanguageChanged, 'rus'))
        self.russian.clicked.connect(self.reload)
        self.addWidget(self.russian)

        self.ukrainian = ToolbarButton(self, "Ukrainian", QtGui.QIcon('icons/ukrainian'))
        self.ukrainian.clicked.connect(functools.partial(self.onLanguageChanged, 'ukr'))
        self.ukrainian.clicked.connect(self.reload)
        self.addWidget(self.ukrainian)

        self.belarusian = ToolbarButton(self, "Belarusian", QtGui.QIcon('icons/belarusian'))
        self.belarusian.clicked.connect(self.reload)
        self.belarusian.clicked.connect(functools.partial(self.onLanguageChanged, 'bel'))
        self.addWidget(self.belarusian)

        self.reload(None)

    def addWidget(self, widget):
        self.container.layout().addWidget(widget, -1)

    @hexdi.inject('config')
    def reload(self, event=None, config=None):
        self.english.setChecked(config.get('screenshot.language') == 'eng')
        self.german.setChecked(config.get('screenshot.language') == 'deu')
        self.spanish.setChecked(config.get('screenshot.language') == 'spa')
        self.russian.setChecked(config.get('screenshot.language') == 'rus')
        self.ukrainian.setChecked(config.get('screenshot.language') == 'ukr')
        self.belarusian.setChecked(config.get('screenshot.language') == 'bel')

    @hexdi.inject('config')
    def onLanguageChanged(self, lang, event, config):
        config.set('screenshot.language', lang)
        self.reload(None)
