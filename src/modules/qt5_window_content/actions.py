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
import os

import hexdi
from PyQt5 import QtWidgets

from modules.qt5_window_content import signals


@hexdi.inject('content.widget')
def onActionUndo(event=None, widget=None):
    return widget.undo()


@hexdi.inject('content.widget')
def onActionRedo(event=None, widget=None):
    return widget.redo()


@hexdi.inject('content.widget')
def onActionCleanup(event=None, widget=None):
    return widget.clear()


@hexdi.inject('config', 'content.widget')
def onActionLoad(parent=None, config=None, widget=None):
    config_file = config.get('content.file')
    if os.path.exists(config_file) and os.path.isfile(config_file):
        parent.setWindowTitle('Screen grabber - {}'.format(os.path.basename(config_file)))
        with open(config_file, 'r') as stream:
            widget.setText(stream.read())
            return stream.close()


@hexdi.inject('config', 'window', 'content.widget')
def onActionOpen(event=None, config=None, window=None, widget=None):
    selector = QtWidgets.QFileDialog()
    selector.setDirectory(os.path.expanduser('~'))
    selector.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
    if not selector.exec_(): return None

    for path in selector.selectedFiles():
        window.setWindowTitle('Screen grabber - {}'.format(os.path.basename(path)))
        config.set('content.file', path)
        with open(path, 'r') as stream:
            widget.setText(stream.read())
            return stream.close()


@hexdi.inject('config', 'window', 'content.widget')
def onActionSave(event=None, config=None, window=None, widget=None):
    config_file = config.get('content.file')
    if os.path.exists(config_file) and os.path.isfile(config_file):
        with open(config_file, 'w+') as stream:
            stream.write(widget.text())
            stream.close()

            if not hasattr(signals, 'actionExported'): return None
            return signals.actionSaved.activated.emit(config_file)

    selector = QtWidgets.QFileDialog()
    selector.setDirectory(os.path.expanduser('~'))
    selector.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen | QtWidgets.QFileDialog.AcceptSave)
    if not selector.exec_(): return None

    for path in selector.selectedFiles():
        window.setWindowTitle('Screen grabber - {}'.format(os.path.basename(path)))
        config.set('content.file', path)
        with open(path, 'w+') as stream:
            stream.write(widget.text())
            stream.close()

            if not hasattr(signals, 'actionSaved'): continue
            return signals.actionSaved.activated.emit(path)


@hexdi.inject('config', 'window', 'content.widget')
def onActionExport(event=None, config=None, window=None, widget=None):
    selector = QtWidgets.QFileDialog()
    selector.setDirectory(os.path.expanduser('~'))
    selector.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen | QtWidgets.QFileDialog.AcceptSave)
    if not selector.exec_(): return None

    for path in selector.selectedFiles():
        window.setWindowTitle('Screen grabber - {}'.format(os.path.basename(path)))
        config.set('content.file', path)
        with open(path, 'w+') as stream:
            stream.write(widget.text())
            stream.close()

            if not hasattr(signals, 'actionExported'): continue
            signals.actionExported.activated.emit(path)
