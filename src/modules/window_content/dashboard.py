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
import os

import inject
from PyQt5 import QtWidgets


class ContentWidget(QtWidgets.QTextEdit):
    @inject.params(config='config', window='window')
    def __init__(self, config=None, window=None):
        super(ContentWidget, self).__init__()

        config_file = config.get('content.file', '')
        if os.path.exists(config_file) and os.path.isfile(config_file):
            window.setWindowTitle('Screen grabber - {}'.format(os.path.basename(config_file)))
            with open(config_file, 'r') as stream:
                self.setText(stream.read())
                return stream.close()

    @inject.params(config='config', cleaner='cleaner')
    def onActionText(self, event, config, cleaner):
        if int(config.get('content.append', 1)):
            return self.append(cleaner(event))
        return self.setText(cleaner(event))

    def text(self):
        return self.toPlainText()
