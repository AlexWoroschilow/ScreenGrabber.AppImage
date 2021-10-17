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

from modules.qt5_window_screenshot import signals
from . import actions
from .workspace import container


@hexdi.permanent('content.widget')
class ContentWidgetInstance(container.ContentWidget):
    def __init__(self):
        super().__init__()

        self.actionLoaded.connect(actions.onActionLoad)

        if not hasattr(signals, 'screenshot_created'): return None
        signals.screenshot_created.activated.connect(self.onActionImage)

        if not hasattr(signals, 'screenshot_text_created'): return None
        signals.screenshot_text_created.activated.connect(self.onActionText)
