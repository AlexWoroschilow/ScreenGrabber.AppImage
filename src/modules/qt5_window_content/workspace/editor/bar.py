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

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class ToolBarSpinBox(QtWidgets.QSpinBox):
    def __init__(self, parent=None):
        super(ToolBarSpinBox, self).__init__(parent)
        self.setSuffix(" pt")
        self.setValue(14)

    def event(self, QEvent):
        if QEvent.type() == QtCore.QEvent.Enter:
            effect = QtWidgets.QGraphicsDropShadowEffect()
            effect.setColor(QtGui.QColor('#6cccfc'))
            effect.setBlurRadius(10)
            effect.setOffset(0)

            self.setGraphicsEffect(effect)
        if QEvent.type() == QtCore.QEvent.Leave:
            self.setGraphicsEffect(None)

        if QEvent.type() == QtCore.QEvent.MouseButtonRelease:
            effect = QtWidgets.QGraphicsDropShadowEffect()
            effect.setColor(QtGui.QColor('#6cccfc'))
            effect.setBlurRadius(10)
            effect.setOffset(0)

        return super(ToolBarSpinBox, self).event(QEvent)


class ToolBarButton(QtWidgets.QPushButton):
    activate = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(ToolBarButton, self).__init__(parent)
        self.setFlat(True)

    def connected(self):
        try:
            receiversCount = self.receivers(self.clicked)
            return receiversCount > 0
        except (SyntaxError, RuntimeError) as err:
            return False

    def event(self, QEvent):
        if QEvent.type() == QtCore.QEvent.Enter:
            effect = QtWidgets.QGraphicsDropShadowEffect()
            effect.setColor(QtGui.QColor('#6cccfc'))
            effect.setBlurRadius(10)
            effect.setOffset(0)

            self.setGraphicsEffect(effect)
        if QEvent.type() == QtCore.QEvent.Leave:
            self.setGraphicsEffect(None)

        if QEvent.type() == QtCore.QEvent.MouseButtonRelease:
            effect = QtWidgets.QGraphicsDropShadowEffect()
            effect.setColor(QtGui.QColor('#6cccfc'))
            effect.setBlurRadius(10)
            effect.setOffset(0)

        return super(ToolBarButton, self).event(QEvent)


class ToolbarBase(QtWidgets.QToolBar):

    def __init__(self):
        super(ToolbarBase, self).__init__()


class ToolBarWidgetRight(ToolbarBase):

    def __init__(self):
        super(ToolBarWidgetRight, self).__init__()
        self.setObjectName('editorToolBarWidgetRight')
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.setOrientation(Qt.Vertical)
        self.setContentsMargins(0, 0, 0, 0)
        self.setMaximumWidth(35)

        self.font_bold = ToolBarButton()
        self.font_bold.setIcon(QtGui.QIcon("icons/bold"))
        self.font_bold.setToolTip("Bold")
        self.addWidget(self.font_bold)

        self.font_italic = ToolBarButton()
        self.font_italic.setIcon(QtGui.QIcon("icons/italic"))
        self.font_italic.setToolTip("Italic")
        self.addWidget(self.font_italic)

        self.font_under = ToolBarButton()
        self.font_under.setIcon(QtGui.QIcon("icons/underline"))
        self.font_under.setToolTip("Underline")
        self.addWidget(self.font_under)

        self.font_strike = ToolBarButton()
        self.font_strike.setIcon(QtGui.QIcon("icons/strike"))
        self.font_strike.setToolTip("Strike-out")
        self.addWidget(self.font_strike)

        self.font_super = ToolBarButton()
        self.font_super.setIcon(QtGui.QIcon("icons/superscript"))
        self.font_super.setToolTip("Superscript")
        self.addWidget(self.font_super)

        self.font_sub = ToolBarButton()
        self.font_sub.setIcon(QtGui.QIcon("icons/subscript"))
        self.font_sub.setToolTip("Subscript")
        self.addWidget(self.font_sub)

        self.font_color = ToolBarButton()
        self.font_color.setIcon(QtGui.QIcon("icons/font-color"))
        self.font_color.setToolTip("Change font color")
        self.addWidget(self.font_color)

        self.color_black = ToolBarButton()
        self.color_black.setIcon(QtGui.QIcon("icons/font-black.svg"))
        self.color_black.setToolTip("Change the text color to black")
        self.addWidget(self.color_black)

        self.color_blue = ToolBarButton()
        self.color_blue.setIcon(QtGui.QIcon("icons/font-blue.svg"))
        self.color_blue.setToolTip("Change the text color to blue")
        self.addWidget(self.color_blue)

        self.color_gray = ToolBarButton()
        self.color_gray.setIcon(QtGui.QIcon("icons/font-gray.svg"))
        self.color_gray.setToolTip("Change the text color to gray")
        self.addWidget(self.color_gray)

        self.color_green = ToolBarButton()
        self.color_green.setIcon(QtGui.QIcon("icons/font-green.svg"))
        self.color_green.setToolTip("Change the text color to green")
        self.addWidget(self.color_green)

        self.color_red = ToolBarButton()
        self.color_red.setIcon(QtGui.QIcon("icons/font-red.svg"))
        self.color_red.setToolTip("Change the text color to red")
        self.addWidget(self.color_red)

        self.color_back = ToolBarButton()
        self.color_back.setIcon(QtGui.QIcon("icons/highlight"))
        self.color_back.setToolTip("Font background color")
        self.addWidget(self.color_back)

        self.highlight_black = ToolBarButton()
        self.highlight_black.setIcon(QtGui.QIcon("icons/highlight-black"))
        self.highlight_black.setToolTip("Change background color to black")
        self.addWidget(self.highlight_black)

        self.highlight_blue = ToolBarButton()
        self.highlight_blue.setIcon(QtGui.QIcon("icons/highlight-blue"))
        self.highlight_blue.setToolTip("Change background color to blue")
        self.addWidget(self.highlight_blue)

        self.highlight_grey = ToolBarButton()
        self.highlight_grey.setIcon(QtGui.QIcon("icons/highlight-grey"))
        self.highlight_grey.setToolTip("Change background color to grey")
        self.addWidget(self.highlight_grey)

        self.highlight_green = ToolBarButton()
        self.highlight_green.setIcon(QtGui.QIcon("icons/highlight-green"))
        self.highlight_green.setToolTip("Change background color to green")
        self.addWidget(self.highlight_green)

        self.highlight_red = ToolBarButton()
        self.highlight_red.setIcon(QtGui.QIcon("icons/highlight-red"))
        self.highlight_red.setToolTip("Change background color to red")
        self.addWidget(self.highlight_red)


class FormatbarWidget(ToolbarBase):

    def __init__(self):
        super(FormatbarWidget, self).__init__()
        self.setContentsMargins(0, 0, 0, 0)
        self.setObjectName('editorFormatBarWidget')
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)

        self.fontSize = ToolBarSpinBox(self)

        self.bulletAction = ToolBarButton()
        self.bulletAction.setIcon(QtGui.QIcon("icons/bullet"))
        self.bulletAction.setToolTip("Insert bullet List")

        self.numberedAction = ToolBarButton()
        self.numberedAction.setIcon(QtGui.QIcon("icons/number"))
        self.numberedAction.setToolTip("Insert numbered List")

        self.imageAction = ToolBarButton()
        self.imageAction.setIcon(QtGui.QIcon("icons/image"))
        self.imageAction.setToolTip("Insert image")

        self.alignLeft = ToolBarButton()
        self.alignLeft.setIcon(QtGui.QIcon("icons/align-left"))
        self.alignLeft.setToolTip("Align left")

        self.alignCenter = ToolBarButton()
        self.alignCenter.setIcon(QtGui.QIcon("icons/align-center"))
        self.alignCenter.setToolTip("Align center")

        self.alignRight = ToolBarButton()
        self.alignRight.setIcon(QtGui.QIcon("icons/align-right"))
        self.alignRight.setToolTip("Align right")

        self.alignJustify = ToolBarButton()
        self.alignJustify.setIcon(QtGui.QIcon("icons/align-justify"))
        self.alignJustify.setToolTip("Align justify")

        self.indentAction = ToolBarButton()
        self.indentAction.setIcon(QtGui.QIcon("icons/indent"))
        self.indentAction.setToolTip("Indent Area")

        self.dedentAction = ToolBarButton()
        self.dedentAction.setIcon(QtGui.QIcon("icons/outdent"))
        self.dedentAction.setToolTip("Dedent Area")

        self.addWidget(self.fontSize)

        self.addWidget(self.alignLeft)
        self.addWidget(self.alignCenter)
        self.addWidget(self.alignRight)
        self.addWidget(self.alignJustify)

        self.addWidget(self.bulletAction)
        self.addWidget(self.numberedAction)

        self.addWidget(self.indentAction)
        self.addWidget(self.dedentAction)
        self.addWidget(self.imageAction)
