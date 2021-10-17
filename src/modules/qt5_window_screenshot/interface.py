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
from PyQt5 import QtWidgets

from modules import qt5_window
from . import actions
from .toolbar.panel import ToolbarWidget


@qt5_window.toolbar(name='Grabbed picture', focus=True, position=0)
def window_toolbar(parent=None):
    widget = ToolbarWidget()

    if not widget.screenshot: return widget
    widget.screenshot.connect(actions.onScreenshot)

    if not parent.actionReload: return widget
    parent.actionReload.connect(widget.reload)

    shortcut = QtWidgets.QShortcut("Ctrl+G", parent)
    shortcut.activated.connect(lambda x=None: print(x))

    return widget
