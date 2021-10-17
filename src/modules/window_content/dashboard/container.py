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

from .editor.widget import TextEditorWidget
from .image import ContentImageWidget


class ContentWidget(QtWidgets.QTextEdit):
    actionLoaded = QtCore.pyqtSignal(object)

    def __init__(self):
        super(ContentWidget, self).__init__()
        self.setAlignment(Qt.AlignTop)
        self.setContentsMargins(0, 0, 0, 0)

        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)
        self.layout().setContentsMargins(0, 0, 0, 0)

        self.editor = TextEditorWidget()
        self.preview = ContentImageWidget()

        self.layout().addWidget(self.preview)
        self.layout().addWidget(self.editor)

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

    def setText(self, text=None):
        if not self.editor: return None
        self.editor.setText(text)

    def text(self):
        if not self.editor: return None
        return self.editor.text()
