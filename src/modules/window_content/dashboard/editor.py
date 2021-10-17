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

from .label import ContendEditorStatusWidget


class ContentTextWidget(QtWidgets.QTextEdit):

    def __init__(self):
        super(ContentTextWidget, self).__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    @inject.params(config='config', cleaner='cleaner')
    def onActionText(self, event, config, cleaner):
        if int(config.get('content.append', 1)):
            self.append(cleaner(event))
            maximum = self.verticalScrollBar().maximum()
            return self.verticalScrollBar().setValue(maximum)

        self.setText(cleaner(event))
        maximum = self.verticalScrollBar().maximum()
        return self.verticalScrollBar().setValue(maximum)


class ContentTextContainerWidget(QtWidgets.QFrame):
    def __init__(self):
        super(ContentTextContainerWidget, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)

        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.editor = ContentTextWidget()
        self.statistic = ContendEditorStatusWidget()

        self.layout().addWidget(self.editor)
        self.layout().addWidget(self.statistic)

    def onActionText(self, event):
        if not self.editor: return None
        self.editor.onActionText(event)

        document = self.editor.document()
        if not document: return None

        if not self.statistic: return None
        self.statistic.setText("Lines: {}, Characters:  {}".format(
            document.lineCount(), document.characterCount()
        ))

    def setText(self, text=None):
        if not self.editor: return None
        self.editor.setText(text)

        document = self.editor.document()
        if not document: return None

        if not self.statistic: return None
        self.statistic.setText("Lines: {}, Characters:  {}".format(
            document.lineCount(), document.characterCount()
        ))

    def text(self):
        if not self.editor: return None
        return self.editor.toPlainText()
