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

import hexdi
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class ContentTextWidget(QtWidgets.QTextEdit):
    fontSizeAction = QtCore.pyqtSignal(object)
    bulletAction = QtCore.pyqtSignal(object)
    numberedAction = QtCore.pyqtSignal(object)
    alignLeftAction = QtCore.pyqtSignal(object)
    alignCenterAction = QtCore.pyqtSignal(object)
    alignRightAction = QtCore.pyqtSignal(object)
    alignJustifyAction = QtCore.pyqtSignal(object)
    indentAction = QtCore.pyqtSignal(object)
    dedentAction = QtCore.pyqtSignal(object)
    imageAction = QtCore.pyqtSignal(object)
    italicAction = QtCore.pyqtSignal(object)
    superAction = QtCore.pyqtSignal(object)
    strikeAction = QtCore.pyqtSignal(object)
    fontColorAction = QtCore.pyqtSignal(object)
    backColorAction = QtCore.pyqtSignal(object)
    subAction = QtCore.pyqtSignal(object)
    boldAction = QtCore.pyqtSignal(object)
    underlAction = QtCore.pyqtSignal(object)
    color_black = QtCore.pyqtSignal(object)
    color_blue = QtCore.pyqtSignal(object)
    color_gray = QtCore.pyqtSignal(object)
    color_green = QtCore.pyqtSignal(object)
    color_red = QtCore.pyqtSignal(object)

    highlight_black = QtCore.pyqtSignal(object)
    highlight_blue = QtCore.pyqtSignal(object)
    highlight_grey = QtCore.pyqtSignal(object)
    highlight_green = QtCore.pyqtSignal(object)
    highlight_red = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(ContentTextWidget, self).__init__(parent)
        self.setWordWrapMode(QtGui.QTextOption.WordWrap)
        self.setContentsMargins(0, 0, 0, 0)

        self.setAcceptRichText(True)
        self.setAcceptDrops(True)

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.bulletAction.connect(self.bullet_list_action)
        self.numberedAction.connect(self.number_list_action)
        self.alignLeftAction.connect(self.align_left_action)
        self.alignCenterAction.connect(self.align_center_action)
        self.alignRightAction.connect(self.align_right_action)
        self.alignJustifyAction.connect(self.align_justify_action)
        self.indentAction.connect(self.indent_action)
        self.dedentAction.connect(self.dedent_action)
        self.fontSizeAction.connect(self.setFontPointSize)

        self.italicAction.connect(self.italic_action)
        self.superAction.connect(self.super_script_action)
        self.strikeAction.connect(self.strike_action)
        self.fontColorAction.connect(self.font_color_action)
        self.backColorAction.connect(self.highlight_action)
        self.subAction.connect(self.subscript_action)
        self.boldAction.connect(self.bold_action)
        self.underlAction.connect(self.underline_action)

        self.color_black.connect(self.color_black_action)
        self.color_blue.connect(self.color_blue_action)
        self.color_gray.connect(self.color_gray_action)
        self.color_green.connect(self.color_green_action)
        self.color_red.connect(self.color_red_action)

        self.highlight_black.connect(self.highlight_black_action)
        self.highlight_blue.connect(self.highlight_blue_action)
        self.highlight_grey.connect(self.highlight_grey_action)
        self.highlight_green.connect(self.highlight_green_action)
        self.highlight_red.connect(self.highlight_red_action)

    @hexdi.inject('config', 'cleaner')
    def onActionText(self, event, config, cleaner):
        if int(config.get('content.append', 1)):
            self.append(cleaner(event))
            maximum = self.verticalScrollBar().maximum()
            return self.verticalScrollBar().setValue(maximum)

        self.setText(cleaner(event))
        maximum = self.verticalScrollBar().maximum()
        return self.verticalScrollBar().setValue(maximum)

    def font_color_action(self):
        self.setTextColor(QtWidgets.QColorDialog.getColor())

    def highlight_action(self):
        color = QtWidgets.QColorDialog.getColor()
        self.setTextBackgroundColor(color)

    def bold_action(self):
        if self.fontWeight() == QtGui.QFont.Bold:
            return self.setFontWeight(QtGui.QFont.Normal)
        return self.setFontWeight(QtGui.QFont.Bold)

    def italic_action(self):
        state = self.fontItalic()
        self.setFontItalic(not state)

    def underline_action(self):
        state = self.fontUnderline()
        self.setFontUnderline(not state)

    def strike_action(self):
        fmt = self.currentCharFormat()
        fmt.setFontStrikeOut(not fmt.fontStrikeOut())
        self.setCurrentCharFormat(fmt)

    def super_script_action(self):
        fmt = self.currentCharFormat()
        align = fmt.verticalAlignment()
        if align == QtGui.QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSuperScript)
        else:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
        self.setCurrentCharFormat(fmt)

    def subscript_action(self):
        fmt = self.currentCharFormat()
        align = fmt.verticalAlignment()
        if align == QtGui.QTextCharFormat.AlignNormal:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignSubScript)
        else:
            fmt.setVerticalAlignment(QtGui.QTextCharFormat.AlignNormal)
        self.setCurrentCharFormat(fmt)

    def indent_action(self):
        cursor = self.textCursor()
        if cursor.hasSelection():
            temp = cursor.blockNumber()
            cursor.setPosition(cursor.anchor())
            diff = cursor.blockNumber() - temp
            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down
            for n in range(abs(diff) + 1):
                cursor.movePosition(QtGui.QTextCursor.StartOfLine)
                cursor.insertText("\t")
                cursor.movePosition(direction)
        else:
            cursor.insertText("\t")

    def handleDedent(self, cursor):
        cursor.movePosition(QtGui.QTextCursor.StartOfLine)
        line = cursor.block().text()
        if line.startswith("\t"):
            cursor.deleteChar()
        else:
            for char in line[:8]:
                if char != " ":
                    break
                cursor.deleteChar()

    def dedent_action(self):
        cursor = self.textCursor()
        if cursor.hasSelection():
            temp = cursor.blockNumber()
            cursor.setPosition(cursor.anchor())
            diff = cursor.blockNumber() - temp
            direction = QtGui.QTextCursor.Up if diff > 0 else QtGui.QTextCursor.Down
            for n in range(abs(diff) + 1):
                self.handleDedent(cursor)
                cursor.movePosition(direction)
        else:
            self.handleDedent(cursor)

    def align_left_action(self):
        self.setAlignment(Qt.AlignLeft)

    def align_right_action(self):
        self.setAlignment(Qt.AlignRight)

    def align_center_action(self):
        self.setAlignment(Qt.AlignCenter)

    def align_justify_action(self):
        self.setAlignment(Qt.AlignJustify)

    def bullet_list_action(self):
        cursor = self.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def number_list_action(self):
        cursor = self.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

    def color_black_action(self, event=None):
        self.setTextColor(QtGui.QColor.fromRgb(0, 0, 0))

    def color_blue_action(self, event=None):
        self.setTextColor(QtGui.QColor.fromRgb(0, 0, 127))

    def color_gray_action(self, event=None):
        self.setTextColor(QtGui.QColor.fromRgb(127, 127, 127))

    def color_green_action(self, event=None):
        self.setTextColor(QtGui.QColor.fromRgb(0, 127, 0))

    def color_red_action(self, event=None):
        self.setTextColor(QtGui.QColor.fromRgb(127, 0, 0))

    def highlight_black_action(self):
        self.setTextBackgroundColor(QtGui.QColor.fromRgb(0, 0, 0))

    def highlight_blue_action(self):
        self.setTextBackgroundColor(QtGui.QColor.fromRgb(0, 0, 127))

    def highlight_green_action(self):
        self.setTextBackgroundColor(QtGui.QColor.fromRgb(0, 127, 0))

    def highlight_grey_action(self):
        self.setTextBackgroundColor(QtGui.QColor.fromRgb(127, 127, 127))

    def highlight_red_action(self):
        self.setTextBackgroundColor(QtGui.QColor.fromRgb(127, 0, 0))
