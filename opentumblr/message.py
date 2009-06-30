#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx

class Message():
    def __init__(self, message):
                
        self.message = message
        self.ShowMessage(self.message)

        
    def ShowMessage(self, message):
        dlg  = wx.MessageDialog(None, self.message, 'Error', wx.OK | wx.ICON_ERROR)
        #dlg  = wx.MessageBox(self.message, 'Error')
        dlg.ShowModal()