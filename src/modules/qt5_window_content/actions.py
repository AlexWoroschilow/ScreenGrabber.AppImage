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

from . import signals


@hexdi.inject('content.widget')
def onActionCleanup(event=None, widget=None):
    return widget.setText(None)


@hexdi.inject('config', 'content.widget')
def onActionLoad(parent=None, config=None, widget=None):
    config_file = config.get('content.file', '')
    if os.path.exists(config_file) and os.path.isfile(config_file):
        parent.setWindowTitle('Screen grabber - {}'.format(os.path.basename(config_file)))
        with open(config_file, 'r') as stream:
            widget.setText(stream.read())
            return stream.close()


@hexdi.inject('content.widget', 'config', 'window')
def onActionOpen(event=None, widget=None, config=None, window=None):
    selector = QtWidgets.QFileDialog()
    selector.setDirectory(os.path.expanduser('~'))
    selector.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
    if not selector.exec_(): return None

    for path in selector.selectedFiles():
        if not os.path.exists(path):
            message = widget.tr("Are you sure you want to overwrite the file '%s' ?" % path)
            return QtWidgets.QMessageBox.question(widget, 'Are you sure?', message)

        window.setWindowTitle('Screen grabber - {}'.format(os.path.basename(path)))
        config.set('content.file', path)
        with open(path, 'r') as stream:
            widget.setText(stream.read())
            return stream.close()


@hexdi.inject('content.widget', 'config', 'window')
def onActionSave(event=None, widget=None, config=None, window=None):
    config_file = config.get('content.file', '')
    if os.path.exists(config_file) and os.path.isfile(config_file):
        with open(config_file, 'w+') as stream:
            stream.write(widget.text())
            stream.close()

            if not hasattr(signals, 'content_saved'): return None
            return signals.content_saved.activated.emit(config_file)

    selector = QtWidgets.QFileDialog()
    selector.setDirectory(os.path.expanduser('~'))
    selector.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen | QtWidgets.QFileDialog.AcceptSave)
    if not selector.exec_(): return None

    for path in selector.selectedFiles():
        if len(path) and os.path.exists(path):
            message = widget.tr("Are you sure you want to overwrite the file '%s' ?" % path)
            reply = QtWidgets.QMessageBox.question(widget, 'Are you sure?', message, QtWidgets.QMessageBox.Yes,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.No:
                break

        window.setWindowTitle('Screen grabber - {}'.format(os.path.basename(path)))
        config.set('content.file', path)
        with open(path, 'w+') as stream:
            stream.write(widget.text())
            stream.close()

            if not hasattr(signals, 'content_saved'): continue
            return signals.content_saved.activated.emit(path)


@hexdi.inject('content.widget', 'config', 'window')
def onActionExport(event=None, widget=None, config=None, window=None):
    selector = QtWidgets.QFileDialog()
    selector.setDirectory(os.path.expanduser('~'))
    selector.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen | QtWidgets.QFileDialog.AcceptSave)
    if not selector.exec_(): return None

    for path in selector.selectedFiles():
        if len(path) and os.path.exists(path):
            message = widget.tr("Are you sure you want to overwrite the file '%s' ?" % path)
            reply = QtWidgets.QMessageBox.question(widget, 'Are you sure?', message, QtWidgets.QMessageBox.Yes,
                                                   QtWidgets.QMessageBox.No)
            if reply == QtWidgets.QMessageBox.No:
                break

        window.setWindowTitle('Screen grabber - {}'.format(os.path.basename(path)))
        config.set('content.file', path)
        with open(path, 'w+') as stream:
            stream.write(widget.text())
            stream.close()

            if not hasattr(signals, 'content_exported'): continue
            signals.content_exported.activated.emit(path)
