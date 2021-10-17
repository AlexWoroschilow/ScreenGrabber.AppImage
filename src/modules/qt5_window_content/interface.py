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
from PyQt5 import QtWidgets

from modules import qt5_window
from . import actions


@qt5_window.toolbar(name='Grabbed text', focus=False, position=1)
def window_toolbar(parent=None):
    from .toolbar.panel import ToolbarWidget
    widget = ToolbarWidget()

    if not hasattr(widget, 'actionCleanup'): return widget
    widget.actionCleanup.connect(actions.onActionCleanup)

    if not hasattr(widget, 'actionSave'): return widget
    widget.actionSave.connect(actions.onActionSave)

    if not hasattr(widget, 'actionExport'): return widget
    widget.actionExport.connect(actions.onActionExport)

    if not hasattr(widget, 'actionOpen'): return widget
    widget.actionOpen.connect(actions.onActionOpen)

    if not hasattr(parent, 'actionReload'): return widget
    parent.actionReload.connect(widget.reload)

    return widget


@qt5_window.workspace(name='Grab the screen area to get the text', focus=True, position=0)
@hexdi.inject('content.widget')
def window_dashboard(parent=None, widget=None):
    widget.actionLoaded.emit(parent)

    shortcut = QtWidgets.QShortcut("Ctrl+S", parent)
    shortcut.activated.connect(actions.onActionSave)

    shortcut = QtWidgets.QShortcut("Ctrl+E", parent)
    shortcut.activated.connect(actions.onActionExport)

    shortcut = QtWidgets.QShortcut("Ctrl+O", parent)
    shortcut.activated.connect(actions.onActionOpen)

    return widget
