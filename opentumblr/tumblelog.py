#!/usr/bin/env python
# -*- coding: us-ascii -*-

import wx
#import  wx.lib.scrolledpanel as scrolled
#import wx.html as html

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
	    self.path_images = self.parent.path_images

	    self.bitmap_1 = wx.StaticBitmap(self.panel, -1, wx.Bitmap(self.path_images + "opentumblr.png", wx.BITMAP_TYPE_ANY))
	    self.__set_properties()
	    self.__do_layout()


    def __set_properties(self):
        #self.SetSize((310, 462))
        self.SetBackgroundColour(wx.Colour(47, 47, 47))

    def __do_layout(self):
        self.s_tumblelog = wx.BoxSizer(wx.VERTICAL)
        self.s_tumblelog.Add(self.panel, 1, wx.EXPAND, 0)
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.bitmap_1, 0, wx.TOP|wx.ALIGN_CENTER_HORIZONTAL, 150)
        self.panel.SetSizer(sizer_1)
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
            newpanel = TumbleLog(self, -1)
            self.SwitchPanel(newpanel)
#        else:
#            pass

"""
class MyTumbleLog(scrolled.ScrolledPanel):
    def __init__(self, parent, id):
        scrolled.ScrolledPanel.__init__(self, parent, id)
        self.parent = parent
        #self.api = self.parent.api
        self.html1 = html.HtmlWindow(self, id, size=(280,570), pos = (5,70))
        
        self.l_tumblelog = wx.StaticText(self, -1, "Tumble Log")
        self.label_1 = wx.StaticText(self, -1, "label_1")
        
        #self.__get_mytumblelog()
        self.__get_dashboard()
        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetBackgroundColour(wx.Colour(100, 100, 100))
        self.l_tumblelog.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.label_1.SetMinSize((314, 254))

    def __do_layout(self):
        s_mytumblelog = wx.BoxSizer(wx.VERTICAL)
        s_mytumblelog.Add(self.l_tumblelog, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_mytumblelog.Add(self.label_1, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(s_mytumblelog)
        self.SetupScrolling()
        s_mytumblelog.Fit(self)
    
    def __get_mytumblelog(self):
        html = ''
        self.title = []
        self.body = []

        self.html1.SetStandardFonts()
        
        lists = self.api.read(start = 0, max = 5)
        #assert False,lists
        for post in lists:
            #print post
            if post['type'] == 'regular':
                self.title = '<p bgcolor=\'#fff\'><br /><b>' + post['regular-title'] + '</b><br />'
                body = self.title + post['regular-body'] + '<br />' + post['date'] + '</p><br />'
                self.body.append(body)
            if post['type'] == 'photo':
                self.title = '<p background=\'#000\'><br /><br />'
                body = self.title + post['photo-url-250'] + '<br />' + post['date'] + '</p><br />'
                self.body.append(body)
            if post['type'] == 'conversation':
                self.title = '<p bgcolor=\'#fff\'><br /><b>' + post['conversation-title'] + '</b><br />'
                body = self.title + post['conversation-text'] + '<br />' + post['date'] + '</p><br />'
                self.body.append(body)
            if post['type'] == 'link':
                self.title = '<p bgcolor=\'#fff\'><br /><b>' + post['link-text'] + '</b><br />'
                body = self.title + post['link-url'] + '<br />' + post['date'] + '</p<br />'
                self.body.append(body)
            if post['type'] == 'quote':
                self.title = '<p bgcolor=\'#fff\'><br /><br />'
                body = self.title + post['quote-text'] + '<br />' + post['date'] + '</p><br />'
                self.body.append(body)
            if post['type'] == 'audio':
                self.title = '<p bgcolor=\'#fff\'><br /><br />'
                body = self.title + post['audio-player'] + '<br />' + post['date'] + '</p><br />'
                self.body.append(body)
            if post['type'] == 'video':
                self.title = '<p bgcolor=\'#fff\'><br /><br />'
                body = self.title + post['video-player'] + '<br />' + post['date'] + '</p><br />'
                self.body.append(body)

        for value in self.body:
            html += value + '<br />'

        self.html1.SetPage(html)
    
    def __get_dashboard(self):
        self.html1.SetStandardFonts()
        
        lists = self.api.dashboard()
        self.html1.SetPage(lists)
"""
