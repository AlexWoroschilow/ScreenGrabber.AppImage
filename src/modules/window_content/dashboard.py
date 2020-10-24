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
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5 import QtCore


class ContentTextWidget(QtWidgets.QTextEdit):

    def __init__(self):
        super(ContentTextWidget, self).__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    @inject.params(config='config', cleaner='cleaner')
    def onActionText(self, event, config, cleaner):
        if int(config.get('content.append', 1)):
            self.append(cleaner(event))
            maximum = self.verticalScrollBar().maximum()
            return self.verticalScrollBar().setValue(maximum)

        self.setText(cleaner(event))
        maximum = self.verticalScrollBar().maximum()
        return self.verticalScrollBar().setValue(maximum)


class ContentImageWidget(QtWidgets.QLabel):
    def __init__(self):
        super(ContentImageWidget, self).__init__()
        self.setAlignment(Qt.AlignTop)
        self.setMinimumWidth(400)

        self.hover_effect = QtWidgets.QGraphicsDropShadowEffect()
        self.hover_effect.setBlurRadius(10)
        self.hover_effect.setOffset(0, 0)
        self.setGraphicsEffect(self.hover_effect)
        self.original = None

    def resize(self, size):
        width = size.width()

        pixmap = self.original
        if not pixmap: return None

        self.setPixmap(pixmap.scaledToWidth(
            width / 3
        ))

    def setPreview(self, pixmap: QtGui.QPixmap):
        if not pixmap: return None
        self.original = pixmap

        width = self.width()
        if not width: return None

        pixmap = pixmap.scaledToWidth(width)
        if not pixmap: return None

        self.setPixmap(pixmap)


class ContentWidget(QtWidgets.QTextEdit):
    actionLoaded = QtCore.pyqtSignal(object)

    def __init__(self):
        super(ContentWidget, self).__init__()
        self.setAlignment(Qt.AlignTop)

        self.setLayout(QtWidgets.QGridLayout())
        self.layout().setAlignment(Qt.AlignTop)

        self.editor = ContentTextWidget()
        self.preview = ContentImageWidget()

        self.statistic = QtWidgets.QLabel()
        self.statistic.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.statistic.setAlignment(Qt.AlignCenter)
        self.statistic.setText('Loading...')

        self.layout().addWidget(self.preview, 0, 0, 1, 1)
        self.layout().addWidget(self.editor, 0, 1, 1, 2)
        self.layout().addWidget(self.statistic, 1, 0, 1, 3)

        self.actionLoaded.emit(())

    def resizeEvent(self, QResizeEvent):
        size = QResizeEvent.size()
        if not size: return None

        if not self.preview: return None
        self.preview.resize(size)

    def onActionImage(self, pixmap: QtGui.QPixmap):
        if not self.preview: return None
        self.preview.setPreview(pixmap)

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
