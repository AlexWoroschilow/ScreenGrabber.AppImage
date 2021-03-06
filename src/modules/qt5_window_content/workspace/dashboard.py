# Copyright 2020 Alex Woroschilow (alex.woroschilow@gmail.com)
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
import hexdi
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class ContentTextWidget(QtWidgets.QTextEdit):

    def __init__(self):
        super(ContentTextWidget, self).__init__()
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

    @hexdi.inject('config', 'cleaner')
    def onActionText(self, event, config, cleaner):
        if int(config.get('content.append', 1)):
            self.append(cleaner(event))
            maximum = self.verticalScrollBar().maximum()
            return self.verticalScrollBar().setValue(maximum)

        self.setText(cleaner(event))

        maximum = self.verticalScrollBar().maximum()
        return self.verticalScrollBar().setValue(maximum)

    def setText(self, text):
        document = self.document()
        if not document: return None

        cursor = QtGui.QTextCursor(document.firstBlock())
        cursor.select(QtGui.QTextCursor.Document)
        cursor.insertText(text)
        return cursor.deleteChar()

    def clear(self):
        document = self.document()
        if not document: return None

        cursor = QtGui.QTextCursor(document.firstBlock())
        cursor.select(QtGui.QTextCursor.Document)
        cursor.removeSelectedText()
        return cursor.deleteChar()


class ContentImageWidget(QtWidgets.QLabel):
    def __init__(self):
        super(ContentImageWidget, self).__init__()
        self.setAlignment(Qt.AlignTop)

        self.hover_effect = QtWidgets.QGraphicsDropShadowEffect()
        self.hover_effect.setBlurRadius(10)
        self.hover_effect.setOffset(0, 0)
        self.setGraphicsEffect(self.hover_effect)
        self.original = None

    def resize(self, size):
        proportion = 297.0 / 210.0

        height = size.height()
        width = size.width() / 2

        width_new = width
        height_new = width * proportion
        if not height_new or height_new >= height:
            height_new = height - 20
            width_new = height_new / proportion

        self.setFixedHeight(height_new)
        self.setFixedWidth(width_new)

        pixmap = self.original
        if not pixmap: return None

        self.setPixmap(pixmap.scaledToWidth(width_new))

    def setPreview(self, pixmap: QtGui.QPixmap):
        if not pixmap: return None
        self.original = pixmap

        width = self.width()
        if not width: return None

        pixmap = pixmap.scaledToWidth(width)
        if not pixmap: return None

        self.setPixmap(pixmap)


class ContentWidget(QtWidgets.QWidget):
    actionLoaded = QtCore.pyqtSignal(object)

    def __init__(self):
        super(ContentWidget, self).__init__()
        # self.setAlignment(Qt.AlignTop)
        self.setContentsMargins(0, 0, 0, 0)

        self.setLayout(QtWidgets.QGridLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.editor = ContentTextWidget()
        self.preview = ContentImageWidget()

        self.statistic = QtWidgets.QLabel()
        self.statistic.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.statistic.setAlignment(Qt.AlignCenter)
        self.statistic.setText('Loading...')

        self.layout().addWidget(self.preview, 0, 0, 1, 1)
        self.layout().addWidget(self.editor, 0, 1, 1, 1)
        self.layout().addWidget(self.statistic, 1, 0, 1, 2)

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

    def clear(self):
        document = self.editor.document()
        if not document: return None

        cursor = QtGui.QTextCursor(document.firstBlock())
        cursor.select(QtGui.QTextCursor.Document)
        cursor.removeSelectedText()
        return cursor.deleteChar()

    def undo(self):
        document = self.editor.document()
        if not document: return None

        return document.undo()

    def redo(self):
        document = self.editor.document()
        if not document: return None

        return document.redo()

    def text(self):
        if not self.editor: return None
        return self.editor.toPlainText()
