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
import functools

import hexdi
from PyQt5 import QtWidgets

from modules import qt5_window
from modules.qt5_window_screenshot import actions

shortcut = QtWidgets.QShortcut("Ctrl+G", hexdi.resolve('window'))
shortcut.activated.connect(functools.partial(actions.onScreenshot, None))


@qt5_window.toolbar(name='Screenshot', focus=True, position=0)
def window_toolbar(parent=None):
    from .toolbar.panel import ToolbarWidget
    widget = ToolbarWidget()

    if not widget.actionScreenshot: return widget
    widget.actionScreenshot.connect(actions.onScreenshot)

    if not parent.actionReload: return widget
    parent.actionReload.connect(widget.reload)

    return widget
