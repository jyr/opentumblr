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

class Text(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.parent = parent
        self.api = self.parent.api
        self.tags = None
        self.date = None
        self.private = 0
        self.p_main = wx.Panel(self, -1)

        self.s_text_staticbox = wx.StaticBox(self.p_main, -1, "")
        self.b_options = wx.Button(self.p_main, -1, "Advanced  options")
        self.l_text = wx.StaticText(self.p_main, -1, "Add a Text Post")
        self.l_title = wx.StaticText(self.p_main, -1, "Title (optional)")
        self.tc_title = wx.TextCtrl(self.p_main, -1, "")
        self.l_post = wx.StaticText(self.p_main, -1, "Post")
        self.tc_post = wx.TextCtrl(self.p_main, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_main, -1, "Create post")
        self.b_cancel = wx.Button(self.p_main, -1, "Cancel")
        
        self.Bind(wx.EVT_BUTTON, self.AdvancedOptions, id = self.b_options.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCreatePost, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.l_text.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_title.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_post.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        #self.tc_post.SetMinSize((250, 250))
        #self.b_create.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.p_main.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
	    s_main = wx.BoxSizer(wx.VERTICAL)
	    s_text = wx.StaticBoxSizer(self.s_text_staticbox, wx.VERTICAL)
	    s_buttons = wx.BoxSizer(wx.HORIZONTAL)
	    s_text.Add(self.b_options, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 2)
	    s_text.Add(self.l_text, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
	    s_text.Add(self.l_title, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
	    s_text.Add(self.tc_title, 0, wx.ALL|wx.EXPAND, 2)
	    s_text.Add(self.l_post, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
	    s_text.Add(self.tc_post, 1, wx.ALL|wx.EXPAND, 2)
	    s_buttons.Add(self.b_create, 1, wx.LEFT|wx.EXPAND, 2)
	    s_buttons.Add(self.b_cancel, 1, wx.LEFT|wx.EXPAND, 2)
	    s_text.Add(s_buttons, 0, wx.ALL|wx.EXPAND, 2)
	    self.p_main.SetSizer(s_text)
	    s_main.Add(self.p_main, 1, wx.ALL|wx.EXPAND, 10)
	    self.SetSizer(s_main)
	    s_main.Fit(self)
        #self.SetSizer(s_text)
        #s_text.Fit(self)

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
                
    def OnCreatePost(self, evt):
    	self.title = self.tc_title.GetValue().encode('utf-8')
    	self.body = self.tc_post.GetValue().encode('utf-8')
            
        if self.body:
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_regular(self.title, self.body)
            except:
                print "Posteado en blog primario"
            self.OnCancel(self)
        else:
            Message("Post is required")

    def OnCancel(self, evt):
        """ Sirve para cancel y cerrar la opcion de text """
        self.parent.SetPanel(None)
