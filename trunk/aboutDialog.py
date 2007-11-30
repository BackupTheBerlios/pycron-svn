#Boa:Dialog:AboutDialog

import sys, os
import wx
from wx.html import HtmlWindow

def create(parent):
    return AboutDialog(parent)

[wxID_ABOUTDIALOG, wxID_ABOUTDIALOGABOUTHTMLWINDOW, wxID_ABOUTDIALOGOKBUTTON,
] = map(lambda _init_ctrls: wx.NewId(), range(3))

class AboutDialog(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ABOUTDIALOG, name=u'AboutDialog',
              parent=prnt, pos=wx.Point(120, 93), size=wx.Size(304, 344),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'About crontab.txt Editor')
        self.SetClientSize(wx.Size(296, 317))

        self.OKButton = wx.Button(id=wxID_ABOUTDIALOGOKBUTTON, label=u'&OK',
              name=u'OKButton', parent=self, pos=wx.Point(108, 280),
              size=wx.Size(80, 24), style=0)
        wx.EVT_BUTTON(self.OKButton, wxID_ABOUTDIALOGOKBUTTON,
              self.OnOkbuttonButton)

        self.aboutHtmlWindow = HtmlWindow(id=wxID_ABOUTDIALOGABOUTHTMLWINDOW,
              name=u'aboutHtmlWindow', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(280, 256))

    def __init__(self, parent):
        self._init_ctrls(parent)
        prgpath = os.path.dirname(os.path.abspath(sys.argv[0]))
        fileName = prgpath + os.sep + "about.html"
        self.aboutHtmlWindow.LoadFile(fileName)

    def OnOkbuttonButton(self, event):
        self.Close()
