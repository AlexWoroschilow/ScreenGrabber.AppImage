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
from PyQt5 import QtWidgets

from modules import qt5_window
from . import actions
from .toolbar.panel import ToolbarWidget


@qt5_window.workspace(name='Content')
@hexdi.inject('content.widget')
def window_dashboard(parent=None, widget=None):
    widget.actionLoaded.emit(parent)

    shortcut = QtWidgets.QShortcut("Ctrl+S", parent)
    shortcut.activated.connect(actions.onActionSave)

    shortcut = QtWidgets.QShortcut("Ctrl+E", parent)
    shortcut.activated.connect(actions.onActionExport)

    shortcut = QtWidgets.QShortcut("Ctrl+O", parent)
    shortcut.activated.connect(actions.onActionOpen)

    shortcut = QtWidgets.QShortcut("Ctrl+Z", parent)
    shortcut.activated.connect(actions.onActionUndo)

    shortcut = QtWidgets.QShortcut("Ctrl+Y", parent)
    shortcut.activated.connect(actions.onActionRedo)

    return widget


@qt5_window.toolbar(name='Content', focus=False, position=1)
@hexdi.inject('content.widget')
def window_toolbar(parent=None, content=None):
    widget = ToolbarWidget()

    if not hasattr(widget, 'actionCleanup'): return widget
    widget.actionCleanup.connect(actions.onActionCleanup)

    if not hasattr(widget, 'actionSave'): return widget
    widget.actionSave.connect(actions.onActionSave)

    if not hasattr(widget, 'actionExport'): return widget
    widget.actionExport.connect(actions.onActionExport)

    if not hasattr(widget, 'actionOpen'): return widget
    widget.actionOpen.connect(actions.onActionOpen)

    if not hasattr(widget, 'actionUndo'): return widget
    widget.actionUndo.connect(actions.onActionUndo)

    if not hasattr(widget, 'actionRedo'): return widget
    widget.actionRedo.connect(actions.onActionRedo)

    if not hasattr(parent, 'actionReload'): return widget
    parent.actionReload.connect(widget.reload)

    return widget
