# Copyright: Damien Elmes <anki@ichi2.net>
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

# imports are all in this file to make moving to pyside easier in the future
# fixme: make sure not to optimize imports on this file

import sip
import os

from anki.utils import isWin, isMac

sip.setapi('QString', 2)
sip.setapi('QVariant', 2)
sip.setapi('QUrl', 2)
try:
    sip.setdestroyonexit(False)
except:
    # missing in older versions
    pass
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebKit import QWebSettings
from PyQt5.QtWebKitWidgets import QWebPage, QWebView
from PyQt5.QtNetwork import QLocalServer, QLocalSocket


def debug():
  from PyQt5.QtCore import pyqtRemoveInputHook
  from pdb import set_trace
  pyqtRemoveInputHook()
  set_trace()

import sys, traceback

if os.environ.get("DEBUG"):
    def info(type, value, tb):
        from PyQt5.QtCore import pyqtRemoveInputHook
        for line in traceback.format_exception(type, value, tb):
            sys.stdout.write(line)
        pyqtRemoveInputHook()
        from pdb import pm
        pm()
    sys.excepthook = info

qtmajor = (QT_VERSION & 0xff0000) >> 16
qtminor = (QT_VERSION & 0x00ff00) >> 8

# qt4.6 doesn't support ruby tags
if qtmajor <= 4 and qtminor <= 6:
  import anki.template.furigana
  anki.template.furigana.ruby = r'<span style="display: inline-block; text-align: center; line-height: 1; white-space: nowrap; vertical-align: baseline; margin: 0; padding: 0"><span style="display: block; text-decoration: none; line-height: 1.2; font-weight: normal; font-size: 0.64em">\2</span>\1</span>'

