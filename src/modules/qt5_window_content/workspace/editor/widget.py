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
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from .bar import FormatbarWidget
from .bar import ToolBarWidgetRight
from .text import ContentTextWidget


class TextEditorWidget(QtWidgets.QFrame):

    def __init__(self):
        super(TextEditorWidget, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)

        self.writer = ContentTextWidget(self)
        self.writer.cursorPositionChanged.connect(self.cursorPosition)

        self.statusbar = QtWidgets.QLabel()
        self.statusbar.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        self.statusbar.setAlignment(Qt.AlignCenter)

        self.formatbar = FormatbarWidget()
        self.formatbar.bulletAction.clicked.connect(self.writer.bulletAction.emit)
        self.formatbar.numberedAction.clicked.connect(self.writer.numberedAction.emit)
        self.formatbar.alignLeft.clicked.connect(self.writer.alignLeftAction.emit)
        self.formatbar.alignCenter.clicked.connect(self.writer.alignCenterAction.emit)
        self.formatbar.alignRight.clicked.connect(self.writer.alignRightAction.emit)
        self.formatbar.alignJustify.clicked.connect(self.writer.alignJustifyAction.emit)
        self.formatbar.indentAction.clicked.connect(self.writer.indentAction.emit)
        self.formatbar.dedentAction.clicked.connect(self.writer.dedentAction.emit)
        self.formatbar.imageAction.clicked.connect(self.writer.imageAction.emit)
        self.formatbar.fontSize.valueChanged.connect(self.writer.fontSizeAction.emit)

        self.rightbar = ToolBarWidgetRight()
        self.rightbar.font_italic.clicked.connect(self.writer.italicAction.emit)
        self.rightbar.font_super.clicked.connect(self.writer.superAction.emit)
        self.rightbar.font_under.clicked.connect(self.writer.underlAction.emit)
        self.rightbar.font_strike.clicked.connect(self.writer.strikeAction.emit)
        self.rightbar.font_color.clicked.connect(self.writer.fontColorAction.emit)
        self.rightbar.font_sub.clicked.connect(self.writer.subAction.emit)
        self.rightbar.font_bold.clicked.connect(self.writer.boldAction.emit)
        self.rightbar.color_back.clicked.connect(self.writer.backColorAction.emit)

        self.rightbar.color_black.clicked.connect(self.writer.color_black.emit)
        self.rightbar.color_blue.clicked.connect(self.writer.color_blue.emit)
        self.rightbar.color_gray.clicked.connect(self.writer.color_gray.emit)
        self.rightbar.color_green.clicked.connect(self.writer.color_green.emit)
        self.rightbar.color_red.clicked.connect(self.writer.color_red.emit)

        self.rightbar.highlight_black.clicked.connect(self.writer.highlight_black.emit)
        self.rightbar.highlight_blue.clicked.connect(self.writer.highlight_blue.emit)
        self.rightbar.highlight_grey.clicked.connect(self.writer.highlight_grey.emit)
        self.rightbar.highlight_green.clicked.connect(self.writer.highlight_green.emit)
        self.rightbar.highlight_red.clicked.connect(self.writer.highlight_red.emit)

        self.setLayout(QtWidgets.QGridLayout())

        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().addWidget(self.formatbar, 0, 0, 1, 4)
        self.layout().addWidget(self.rightbar, 1, 3, 1, 1)
        self.layout().addWidget(self.writer, 1, 0, 1, 3)
        self.layout().addWidget(self.statusbar, 4, 0, 1, 4)

    def cursorPosition(self):
        cursor = self.writer.textCursor()
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()
        self.statusbar.setText("Line: {}, Column: {}".format(line, col))

    def onActionText(self, event):
        if not self.writer: return None
        self.writer.onActionText(event)

        document = self.writer.document()
        if not document: return None

        if not self.statusbar: return None
        self.statusbar.setText("Lines: {}, Characters:  {}".format(
            document.lineCount(), document.characterCount()
        ))

    def setText(self, text=None):
        if not self.writer: return None
        self.writer.setHtml(text)

        document = self.writer.document()
        if not document: return None

        if not self.statusbar: return None
        self.statusbar.setText("Lines: {}, Characters:  {}".format(
            document.lineCount(), document.characterCount()
        ))

    def text(self):
        if not self.writer: return None
        return self.writer.toHtml()

    def close(self):
        super().deleteLater()
        return super().close()
