#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import editorDialog

modules ={u'aboutDialog': [0, '', u'aboutDialog.py'],
 u'dayWizardDialog': [0, '', u'dayWizardDialog.py'],
 u'editorDialog': [1, 'Main frame of Application', u'editorDialog.py'],
 u'hourWizardDialog': [0, '', u'hourWizardDialog.py'],
 u'minuteWizardDialog': [0, '', u'minuteWizardDialog.py'],
 u'monthWizardDialog': [0, '', u'monthWizardDialog.py'],
 u'taskDialog': [0, '', u'taskDialog.py'],
 u'weekdayWizardDialog': [0, '', u'weekdayWizardDialog.py']}

class BoaApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        self.main = editorDialog.create(None)
        # needed when running from Boa under Windows 9X
        self.SetTopWindow(self.main)
        self.main.Show();self.main.Hide();self.main.Show()
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
