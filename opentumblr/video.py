#!/usr/bin/env python
# -*- coding: us-ascii -*-

import wx
import string

from options import AdvancedOptions
from message import Message

try:
    from opentumblr.tumblr import Api
except ImportError:
    from tumblr import Api

class Video(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.parent = parent
        self.api = self.parent.api
        self.tags = None
        self.date = None
        self.private = 0

        self.p_main = wx.Panel(self, -1)
        self.s_video_staticbox = wx.StaticBox(self.p_main, -1, "")
        self.b_options = wx.Button(self.p_main, -1, "Advanced  options")
        self.l_addvideo = wx.StaticText(self.p_main, -1, "Add a Video")
        self.l_embed = wx.StaticText(self.p_main, -1, "Embed a Video")
        self.label_1 = wx.StaticText(self.p_main, -1, "This can be a URL from video sites like YouTube or Vimeo, \nor the raw Embed-tag from any video/flash site. \n(ie. http://youtube.com/watch?v=oCmAD-z7-mA)")
        self.tc_embed = wx.TextCtrl(self.p_main, -1, "")
        self.l_caption = wx.StaticText(self.p_main, -1, "Caption (optional)")
        self.tc_caption = wx.TextCtrl(self.p_main, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_main, -1, "Create post")
        self.b_cancel = wx.Button(self.p_main, -1, "Cancel")
        
        self.Bind(wx.EVT_BUTTON, self.AdvancedOptions, id = self.b_options.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCreateVideo, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_addvideo.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_embed.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.label_1.SetForegroundColour(wx.Colour(35, 142, 107))
        self.label_1.SetFont(wx.Font(9, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.tc_embed.SetMinSize((250, 117))
        self.l_caption.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_caption.SetMinSize((250, 118))
        self.p_main.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
	    s_main = wx.BoxSizer(wx.VERTICAL)
	    s_video = wx.StaticBoxSizer(self.s_video_staticbox, wx.VERTICAL)
	    s_buttons = wx.BoxSizer(wx.HORIZONTAL)
	    s_video.Add(self.b_options, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 2)
	    s_video.Add(self.l_addvideo, 0, wx.ALL, 2)
	    s_video.Add(self.l_embed, 0, wx.ALL, 2)
	    s_video.Add(self.label_1, 0, wx.ALL, 2)
	    s_video.Add(self.tc_embed, 0, wx.ALL|wx.EXPAND, 2)
	    s_video.Add(self.l_caption, 0, wx.ALL, 2)
	    s_video.Add(self.tc_caption, 0, wx.ALL|wx.EXPAND, 2)
	    s_buttons.Add(self.b_create, 1, wx.LEFT|wx.EXPAND, 2)
	    s_buttons.Add(self.b_cancel, 1, wx.LEFT|wx.EXPAND, 2)
	    s_video.Add(s_buttons, 0, wx.ALL|wx.EXPAND, 2)
	    self.p_main.SetSizer(s_video)
	    s_main.Add(self.p_main, 1, wx.ALL|wx.EXPAND, 10)
	    self.SetSizer(s_main)
	    s_main.Fit(self)
        #self.SetSizer(s_video)
        #s_video.Fit(self)

    def AdvancedOptions(self, evt):
        self.options = AdvancedOptions(self, -1)
        self.options.Center()
        if self.options.ShowModal() == wx.ID_OK:
            self.tags = self.options.tc_tag.GetValue().encode('utf-8')
            self.tags = string.replace(self.tags,' ', ',')
            self.date = self.options.tc_date.GetValue().encode('utf-8')

            if self.options.cb_publishing.GetValue() == 'private':
                self.private = 1
            else:
                self.private = 0

            if self.options.cb_publishing.GetValue() == 'add to queue':
                self.date = 'on.2'
        self.options.Destroy()
    
    def OnCreateVideo(self, evt):
    	self.embed = self.tc_embed.GetValue()
    	self.caption = self.tc_caption.GetValue().encode('utf-8')

        if self.embed:
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_video(self.embed, self.caption)
            except:
                print "posteado en el blog primario"
            self.OnCancel(self)
        else:
            Message('Embed a video is required')
            
    def OnCancel(self, evt):
	    """ Sirve para cancel y cerrar la opcion de text """
	    self.parent.SetPanel(None)