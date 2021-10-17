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

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


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
