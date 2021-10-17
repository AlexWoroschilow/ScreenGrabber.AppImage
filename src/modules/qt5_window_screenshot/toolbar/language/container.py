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
import math

import hexdi
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from .button import ToolbarLanguageButton


class ToolbarLanguageContainerWidget(QtWidgets.QFrame):
    config = {
        'eng': {'name': 'English', 'icon': 'icons/eng'},
        'spa': {'name': 'Spanish', 'icon': 'icons/spa'},
        'rus': {'name': 'Russian', 'icon': 'icons/rus'},
        'deu': {'name': 'German', 'icon': 'icons/deu'},
        'fra': {'name': 'French', 'icon': 'icons/fra'},
        'hin': {'name': 'Hindi', 'icon': 'icons/hin'},

        'chi-sim': {'name': 'Chinese', 'icon': 'icons/chi-sim'},
        'chi-tra': {'name': 'Chinese', 'icon': 'icons/chi-tra'},

        'ukr': {'name': 'Ukrainian', 'icon': 'icons/ukr'},
        'bel': {'name': 'Belarusian', 'icon': 'icons/bel'},
        'ita': {'name': 'Italian', 'icon': 'icons/ita'},
        'fin': {'name': 'Finnish', 'icon': 'icons/fin'},
        'dan': {'name': 'Danmark', 'icon': 'icons/dan'},
        'ell': {'name': 'Greece', 'icon': 'icons/ell'},
        'est': {'name': 'Estonia', 'icon': 'icons/est'},
        'heb': {'name': 'Hebrew', 'icon': 'icons/heb'},
        'hrv': {'name': 'Croatia', 'icon': 'icons/hrv'},
        'hun': {'name': 'Hungary', 'icon': 'icons/hun'},
        'isl': {'name': 'Iceland', 'icon': 'icons/isl'},
        'lav': {'name': 'Latvia', 'icon': 'icons/lav'},
        'lit': {'name': 'Litauen', 'icon': 'icons/lit'},
        'nld': {'name': 'Dutch', 'icon': 'icons/nld'},
        'nor': {'name': 'Norway', 'icon': 'icons/nor'},
        'pol': {'name': 'Poland', 'icon': 'icons/pol'},
        'por': {'name': 'Portugal', 'icon': 'icons/por'},
        'slk': {'name': 'Slovakia', 'icon': 'icons/slk'},
        'slv': {'name': 'Slovenia', 'icon': 'icons/slv'},
        'sqi': {'name': 'Albania', 'icon': 'icons/sqi'},
        'srp': {'name': 'Serbia', 'icon': 'icons/srp'},
        'swe': {'name': 'Sweden', 'icon': 'icons/swe'},
        'jpn': {'name': 'Japan', 'icon': 'icons/jpn'},
        'ara': {'name': 'Arabic', 'icon': 'icons/ara'},
    }

    @hexdi.inject('config')
    def __init__(self, config=None):
        super(ToolbarLanguageContainerWidget, self).__init__()

        self.setLayout(QtWidgets.QGridLayout())

        self.languages = []

        language = config.get('screenshot.language', 'eng')

        for key in self.config:
            config = self.config.get(key)
            if not config: continue

            button_language = ToolbarLanguageButton(self, config.get('name'), QtGui.QIcon(config.get('icon')), key)
            button_language.clicked.connect(functools.partial(self.onLanguageChanged, lang=key))
            button_language.clicked.connect(self.reload)
            button_language.setChecked(language == key)
            self.languages.append(button_language)

        row = 0
        col = 0
        total = len(self.config)
        for button in self.languages:
            self.layout().addWidget(button, row, col)
            col += 1
            if col > math.ceil(total / 2):
                row += 1
                col = 0

    @hexdi.inject('config')
    def reload(self, event=None, config=None):
        language = config.get('screenshot.language', 'eng')
        for button in self.languages:
            enabled = language == button.code
            button.setChecked(enabled)

    @hexdi.inject('config')
    def onLanguageChanged(self, event=None, lang=None, config=None):
        config.set('screenshot.language', lang)
        self.reload(None)

    @hexdi.inject('config')
    def onToggleScreenshot(self, event=None, config=None):
        config.set('screenshot.enabled', int(event))
