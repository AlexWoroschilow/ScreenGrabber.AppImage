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

import inject
from PyQt5 import QtWidgets


class Loader(object):

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def _constructor(self):
        from modules.window_screenshot import signals
        from modules.window_content.dashboard import container
        from modules.window_content import actions

        widget = container.ContentWidget()
        widget.actionLoaded.connect(actions.onActionLoad)

        if not hasattr(signals, 'actionText'): return widget
        signals.actionScreenshot.activated.connect(widget.onActionImage)
        signals.actionText.activated.connect(widget.onActionText)

        return widget

    def configure(self, binder: inject.Binder, options=None, args=None):
        binder.bind_to_constructor('content.widget', self._constructor)

    def boot(self, options=None, args=None):
        from modules import window
        from modules.window_content import actions

        @window.workspace(name='Grab the screen area to get the text')
        @inject.params(widget='content.widget')
        def window_dashboard(parent=None, widget=None):

            widget.actionLoaded.emit(parent)

            shortcut = QtWidgets.QShortcut("Ctrl+S", parent)
            shortcut.activated.connect(actions.onActionSave)

            shortcut = QtWidgets.QShortcut("Ctrl+E", parent)
            shortcut.activated.connect(actions.onActionExport)

            shortcut = QtWidgets.QShortcut("Ctrl+O", parent)
            shortcut.activated.connect(actions.onActionOpen)

            return widget

        @window.toolbar(name='Content', focus=False, position=1)
        @inject.params(content='content.widget')
        def window_toolbar(parent=None, content=None):

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
