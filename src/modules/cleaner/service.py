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


@hexdi.permanent('cleaner')
def _provider():
    @hexdi.inject('config')
    def clean(text=None, config=None):

        config_enabled = int(config.get('cleaner.enabled'))
        config_lowercase = int(config.get('cleaner.uppercase'))
        config_extrachars = int(config.get('cleaner.extrachars'))

        if not config_enabled: return text
        if config_lowercase: text = text.lower()
        if not config_extrachars: return text

        text = ''.join(e for e in text if (e.isalpha() or ' '))

        return text

    return clean
