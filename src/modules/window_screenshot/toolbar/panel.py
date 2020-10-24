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

import inject
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class ToolbarWidget(QtWidgets.QScrollArea):
    actionScreenshot = QtCore.pyqtSignal(object)

    @inject.params(config='config')
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
        self.english.clicked.connect(functools.partial(self.onLanguageChanged, lang='eng'))
        self.english.clicked.connect(self.reload)
        self.addWidget(self.english)

        self.german = ToolbarButton(self, "German", QtGui.QIcon('icons/german'))
        self.german.clicked.connect(functools.partial(self.onLanguageChanged, lang='deu'))
        self.german.clicked.connect(self.reload)
        self.addWidget(self.german)

        self.spanish = ToolbarButton(self, "Spanish", QtGui.QIcon('icons/spanish'))
        self.spanish.clicked.connect(functools.partial(self.onLanguageChanged, lang='spa'))
        self.spanish.clicked.connect(self.reload)
        self.addWidget(self.spanish)

        self.russian = ToolbarButton(self, "Russian", QtGui.QIcon('icons/russian'))
        self.russian.clicked.connect(functools.partial(self.onLanguageChanged, lang='rus'))
        self.russian.clicked.connect(self.reload)
        self.addWidget(self.russian)

        self.ukrainian = ToolbarButton(self, "Ukrainian", QtGui.QIcon('icons/ukrainian'))
        self.ukrainian.clicked.connect(functools.partial(self.onLanguageChanged, lang='ukr'))
        self.ukrainian.clicked.connect(self.reload)
        self.addWidget(self.ukrainian)

        self.belarusian = ToolbarButton(self, "Belarusian", QtGui.QIcon('icons/belarusian'))
        self.belarusian.clicked.connect(self.reload)
        self.belarusian.clicked.connect(functools.partial(self.onLanguageChanged, lang='bel'))
        self.addWidget(self.belarusian)

        self.reload()

    def addWidget(self, widget):
        self.container.layout().addWidget(widget, -1)

    @inject.params(config='config')
    def reload(self, event=None, config=None):
        self.english.setChecked(config.get('screenshot.language', 'eng') == 'eng')
        self.german.setChecked(config.get('screenshot.language', 'eng') == 'deu')
        self.spanish.setChecked(config.get('screenshot.language', 'eng') == 'spa')
        self.russian.setChecked(config.get('screenshot.language', 'eng') == 'rus')
        self.ukrainian.setChecked(config.get('screenshot.language', 'eng') == 'ukr')
        self.belarusian.setChecked(config.get('screenshot.language', 'eng') == 'bel')

    @inject.params(config='config')
    def onLanguageChanged(self, event=None, lang=None, config=None):
        config.set('screenshot.language', lang)
        self.reload()

    @inject.params(config='config')
    def onToggleScreenshot(self, event=None, config=None):
        config.set('screenshot.enabled', int(event))
