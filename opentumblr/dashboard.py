#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Sun Mar 15 17:47:22 2009

import wx

from distutils.sysconfig import get_python_lib
from text import Text
from photo import Photo
from quote import Quote
from link import Link
from chat import Chat
from audio import Audio
from video import Video
# begin wxGlade: extracode
# end wxGlade

#zodman import
import os, sys

class Dashboard(wx.Panel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Dashboard.__init__
        self.api = args[1]
        wx.Panel.__init__(self, args[0], **kwds)
        self.path_images = '/usr/share/pixmaps/opentumblr/dashboard/'
        if not os.path.isdir(self.path_images):
            os.mkdir(self.path_images)
        
        self.p_botones = wx.Panel(self, -1)
        self.s_dashboard_staticbox = wx.StaticBox(self, -1, "")
        self.s_botones_staticbox = wx.StaticBox(self.p_botones, -1, "")
        self.l_dashboard = wx.StaticText(self, -1, "Dashboard", style=wx.ALIGN_CENTRE)
        self.sl_dashboard = wx.StaticLine(self, -1)
        self.bmap_text = wx.BitmapButton(self.p_botones, -1, wx.Bitmap(self.path_images+"text.png", wx.BITMAP_TYPE_ANY))
        self.bmap_photo = wx.BitmapButton(self.p_botones, -1, wx.Bitmap(self.path_images+"photo.png", wx.BITMAP_TYPE_ANY))
        self.bmap_quote = wx.BitmapButton(self.p_botones, -1, wx.Bitmap(self.path_images+"quote.png", wx.BITMAP_TYPE_ANY))
        self.bmap_link = wx.BitmapButton(self.p_botones, -1, wx.Bitmap(self.path_images+"link.png", wx.BITMAP_TYPE_ANY))
        self.bmap_chat = wx.BitmapButton(self.p_botones, -1, wx.Bitmap(self.path_images+"chat.png", wx.BITMAP_TYPE_ANY))
        self.bmap_audio = wx.BitmapButton(self.p_botones, -1, wx.Bitmap(self.path_images+"audio.png", wx.BITMAP_TYPE_ANY))
        self.bmap_video = wx.BitmapButton(self.p_botones, -1, wx.Bitmap(self.path_images+"video.png", wx.BITMAP_TYPE_ANY))
        self.sl_botones = wx.StaticLine(self.p_botones, -1)
        self.b_logout = wx.Button(self.p_botones, -1, "Log out")
        
        self.Bind(wx.EVT_BUTTON, self.OnText, id = self.bmap_text.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnPhoto, id = self.bmap_photo.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnQuote, id = self.bmap_quote.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnLink, id = self.bmap_link.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnChat, id = self.bmap_chat.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnAudio, id = self.bmap_audio.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnVideo, id = self.bmap_video.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnLogout, id = self.b_logout.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Dashboard.__set_properties
        self.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.l_dashboard.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.l_dashboard.SetForegroundColour(wx.Colour(255, 255, 255))
        self.l_dashboard.SetFont(wx.Font(20, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, "Sans"))
        self.bmap_text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_text.SetSize(self.bmap_text.GetBestSize())
        self.bmap_photo.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_photo.SetSize(self.bmap_photo.GetBestSize())
        self.bmap_quote.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_quote.SetSize(self.bmap_quote.GetBestSize())
        self.bmap_link.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_link.SetSize(self.bmap_link.GetBestSize())
        self.bmap_chat.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_chat.SetSize(self.bmap_chat.GetBestSize())
        self.bmap_audio.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_audio.SetSize(self.bmap_audio.GetBestSize())
        self.bmap_video.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.bmap_video.SetSize(self.bmap_video.GetBestSize())
        self.p_botones.SetBackgroundColour(wx.Colour(255, 255, 255))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Dashboard.__do_layout
        s_dashboard = wx.StaticBoxSizer(self.s_dashboard_staticbox, wx.VERTICAL)
        s_botones = wx.StaticBoxSizer(self.s_botones_staticbox, wx.VERTICAL)
        gs_dashboard = wx.GridSizer(4, 3, 0, 0)
        s_dashboard.Add(self.l_dashboard, 0, wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 15)
        s_dashboard.Add(self.sl_dashboard, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 10)
        gs_dashboard.Add(self.bmap_text, 0, wx.ALL|wx.EXPAND, 5)
        gs_dashboard.Add(self.bmap_photo, 0, wx.ALL|wx.EXPAND, 5)
        gs_dashboard.Add(self.bmap_quote, 0, wx.ALL|wx.EXPAND, 5)
        gs_dashboard.Add(self.bmap_link, 0, wx.ALL|wx.EXPAND, 5)
        gs_dashboard.Add(self.bmap_chat, 0, wx.ALL|wx.EXPAND, 5)
        gs_dashboard.Add(self.bmap_audio, 0, wx.ALL|wx.EXPAND, 5)
        gs_dashboard.Add((20, 20), 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        gs_dashboard.Add(self.bmap_video, 0, wx.ALL|wx.EXPAND, 5)
        gs_dashboard.Add((20, 20), 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 5)
        s_botones.Add(gs_dashboard, 1, wx.ALL|wx.EXPAND, 1)
        s_botones.Add(self.sl_botones, 0, wx.ALL|wx.EXPAND, 10)
        s_botones.Add(self.b_logout, 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 10)
        self.p_botones.SetSizer(s_botones)
        s_dashboard.Add(self.p_botones, 1, wx.ALL|wx.EXPAND, 25)
        s_dashboard.Add((80, 80), 0, wx.ALL|wx.EXPAND|wx.ADJUST_MINSIZE, 20)
        self.SetSizer(s_dashboard)
        s_dashboard.Fit(self)
        # end wxGlade

# end of class Dashboard
    def OnText(self, evt):
		self.text = Text(self, self.api)
		self.text.Show()
	
    def	OnPhoto(self, evt):
    	self.photo = Photo(self, self.api)
    	self.photo.Show()

    def OnQuote(self, evt):
		self.quote = Quote(self, self.api)
		self.quote.Show()
		
    def OnLink(self, evt):
    	self.link = Link(self, self.api)
    	self.link.Show()
    	
    def OnChat(self, evt):
    	self.chat = Chat(self, self.api)
    	self.chat.Show()

    def OnAudio(self, evt):
    	self.audio = Audio(self, self.api)
    	self.audio.Show()
    	
    def OnVideo(self, evt):
    	self.video = Video(self, self.api)
    	self.video.Show()
    
    def OnLogout(self, evt):
    	self.Close()
