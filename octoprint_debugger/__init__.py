# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import octoprint.plugin

class DebuggerPlugin(octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin):
    def on_after_startup(self):
        self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")

    def get_template_vars(self):
        return dict(url=self._settings.get(["url"]))

__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = DebuggerPlugin()
