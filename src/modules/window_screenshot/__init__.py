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

    def configure(self, binder, options=None, args=None):
        from .screenshot.screenshot import Screenshot
        binder.bind('screenshot', Screenshot)

    @inject.params(parent='window')
    def boot(self, options=None, args=None, parent=None):

        from modules import window
        from modules.window_screenshot import actions
        from modules.window_screenshot import signals

        shortcut = QtWidgets.QShortcut("Ctrl+G", parent)
        shortcut.activated.connect(actions.onScreenshot)

        @window.toolbar(name='Grabbed picture', focus=True, position=0)
        def window_toolbar(parent=None):
            from .toolbar.panel import ToolbarWidget
            widget = ToolbarWidget()

            if not widget.actionScreenshot: return widget
            widget.actionScreenshot.connect(actions.onScreenshot)

            if not parent.actionReload: return widget
            parent.actionReload.connect(widget.reload)

            return widget
