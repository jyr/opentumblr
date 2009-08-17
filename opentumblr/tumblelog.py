#!/usr/bin/env python
# -*- coding: us-ascii -*-

import wx

from text import Text
from photo import Photo
from quote import Quote
from link import Link
from chat import Chat
from audio import Audio
from video import Video

class TumbleLog(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.parent = parent
        self.api = self.parent.api
        
        self.panel = wx.Panel(self, -1)

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetSize((310, 462))

    def __do_layout(self):
        self.s_tumblelog = wx.BoxSizer(wx.VERTICAL)
        self.s_tumblelog.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetSizer(self.s_tumblelog)

    def SwitchPanel(self, newpanel):
        self.s_tumblelog.Replace(self.panel, newpanel)
        self.panel.Destroy()
        self.panel = newpanel
        self.Layout()

    def SetPanel(self, paneltype):
        if paneltype == "TEXT":
            newpanel = Text(self, -1)
            self.SwitchPanel(newpanel)
        elif paneltype == "PHOTO":
            newpanel = Photo(self, -1)
            self.SwitchPanel(newpanel)
        elif paneltype == "QUOTE":
            newpanel = Quote(self, -1)
            self.SwitchPanel(newpanel)
        elif paneltype == "LINK":
            newpanel = Link(self, -1)
            self.SwitchPanel(newpanel)
        elif paneltype == "CHAT":
            newpanel = Chat(self, -1)
            self.SwitchPanel(newpanel)
        elif paneltype == "AUDIO":
            newpanel = Audio(self, -1)
            self.SwitchPanel(newpanel)
        elif paneltype == "VIDEO":
            newpanel = Video(self, -1)
            self.SwitchPanel(newpanel)
        elif not paneltype:
            newpanel = MyTumbleLog(self, -1)
            self.SwitchPanel(newpanel)
        else:
            pass

class MyTumbleLog(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.l_text = wx.StaticText(self, -1, "Dashboard")

