# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import View

class BotControl(View):
    template_name = "bot_control.html"

class BotCommands(View):
    template_name = "bot_commands.html"