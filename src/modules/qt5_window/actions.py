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


class ModuleActions(object):

    @hexdi.inject('config')
    def resizeActionEvent(self, event=None, config=None):
        config.set('window.width', int(event.size().width()))
        config.set('window.height', int(event.size().height()))
        return event.accept()

    @hexdi.inject('config')
    def on_window_resize(self, event=None, config=None):
        config.set('window.width', int(event.size().width()))
        config.set('window.height', int(event.size().height()))
        return event.accept()
