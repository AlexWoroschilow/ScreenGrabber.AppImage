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
import logging

import hexdi
import pytesseract
from PIL import Image
from PyQt5 import QtGui

from . import signals


@hexdi.inject('config', 'screenshot')
def onScreenshot(event=None, config=None, screenshot=None):
    logger = logging.getLogger('screenshot')
    logger.info('processing...')

    pixmap: QtGui.QPixmap = screenshot.take_screenshot()
    logger.info('processing pixmap...'.format(pixmap))
    if not pixmap: return None

    language = config.get('screenshot.language', 'eng')
    logger.info('processing pixmap with language: {}...'.format(language))
    if not language: return None

    image = Image.fromqpixmap(pixmap)
    if not image: return None

    string = pytesseract.image_to_string(image, lang=language)
    logger.info('ocr: {}'.format(string))
    if not string: return None

    if not hasattr(signals, 'screenshot_created'): return None
    signals.screenshot_created.activated.emit(pixmap)

    if not hasattr(signals, 'screenshot_text_created'): return None
    signals.screenshot_text_created.activated.emit(string)
