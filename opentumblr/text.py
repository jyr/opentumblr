#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon May  4 00:11:15 2009

import wx
import string
try:
    from opentumblr.tumblr import Api
except ImportError:
    from tumblr import Api
# begin wxGlade: extracode
# end wxGlade



class Text(wx.Dialog):
    def __init__(self, parent, id):
        # begin wxGlade: Text.__init__
        self.parent = parent
        self.api = self.parent.api
        wx.Dialog.__init__(self, parent, id, style = wx.DEFAULT_DIALOG_STYLE)
        #print self.api.url
        #assert False, dir(self.api.email)
        self.panel = wx.Panel(self, -1)
        self.p_options = wx.Panel(self.panel, -1)
        self.p_text = wx.Panel(self.panel, -1)
        self.s_options_staticbox = wx.StaticBox(self.p_options, -1, "")
        self.s_text_staticbox = wx.StaticBox(self.p_text, -1, "")
        self.l_text = wx.StaticText(self.p_text, -1, "Add a Text Post")
        self.l_title = wx.StaticText(self.p_text, -1, "Title (optional)")
        self.tc_title = wx.TextCtrl(self.p_text, -1, "")
        self.l_post = wx.StaticText(self.p_text, -1, "Post")
        self.tc_post = wx.TextCtrl(self.p_text, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_text, -1, "Create post")
        
        """
        Not supported in the tumblr api at this time
        self.b_preview = wx.Button(self.p_text, -1, "Preview")
        """
        
        self.b_cancel = wx.Button(self.p_text, -1, "Cancel")
        self.b_options = wx.Button(self.p_options, -1, "Advanced  options")
        self.l_publishing = wx.StaticText(self.p_options, -1, "Publishing options")
        
        """
        Not supported in the tumblr api at this time
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "add to queue", "publish on...", "save as draft", "private"], style=wx.CB_DROPDOWN)        
        """
        
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "publish on...", "save as draft"], style=wx.CB_DROPDOWN)
        self.l_date = wx.StaticText(self.p_options, -1, "Date this post")
        self.tc_date = wx.TextCtrl(self.p_options, -1, "")
        self.l_tag = wx.StaticText(self.p_options, -1, "Tag this post")
        self.tc_tag = wx.TextCtrl(self.p_options, -1, "", style=wx.TE_MULTILINE)

        """"
        Not supported in the tumlr api at this time
        self.l_url = wx.StaticText(self.p_options, -1, "Set a custom post URL")
        self.tc_url = wx.TextCtrl(self.p_options, -1, "/post/123456/")
        """

        self.Bind(wx.EVT_BUTTON, self.OnCreatePost, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())
        self.Bind(wx.EVT_COMBOBOX, self.GetParent().OnPublishingOptions, id = self.cb_publishing.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Text.__set_properties
        self.SetTitle("Add Text Post")
        self.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.l_text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_text.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_title.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_title.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_title.SetMinSize((623, 50))
        self.tc_title.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_post.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_post.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_post.SetMinSize((633, 350))
        self.tc_post.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.b_create.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        #self.b_preview.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.b_cancel.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.p_text.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.b_options.SetMinSize((141, 30))
        self.l_publishing.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cb_publishing.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.cb_publishing.SetSelection(0)
        self.l_date.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_date.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_tag.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_tag.SetMinSize((201, 80))
        self.tc_tag.SetBackgroundColour(wx.Colour(255, 255, 255))
        #self.l_url.SetBackgroundColour(wx.Colour(255, 255, 255))
        #self.tc_url.SetBackgroundColour(wx.Colour(221, 221, 221))
        #self.tc_url.SetForegroundColour(wx.Colour(192, 192, 192))
        #self.tc_url.SetFont(wx.Font(13, wx.DECORATIVE, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.p_options.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.panel.SetBackgroundColour(wx.Colour(55, 85, 113))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Text.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        gs_text = wx.FlexGridSizer(1, 2, 0, 0)
        s_options = wx.StaticBoxSizer(self.s_options_staticbox, wx.VERTICAL)
        s_text = wx.StaticBoxSizer(self.s_text_staticbox, wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.HORIZONTAL)
        s_text.Add(self.l_text, 0, wx.ALL, 2)
        s_text.Add(self.l_title, 0, wx.ALL, 2)
        s_text.Add(self.tc_title, 0, wx.ALL|wx.EXPAND, 2)
        s_text.Add(self.l_post, 0, wx.ALL|wx.EXPAND, 2)
        s_text.Add(self.tc_post, 0, wx.ALL|wx.EXPAND, 2)
        s_buttons.Add(self.b_create, 0, wx.LEFT|wx.RIGHT, 2)
        #s_buttons.Add(self.b_preview, 0, wx.LEFT|wx.RIGHT, 2)
        s_buttons.Add(self.b_cancel, 0, wx.LEFT|wx.ALIGN_RIGHT, 380)
        s_text.Add(s_buttons, 1, wx.ALL|wx.EXPAND, 10)
        self.p_text.SetSizer(s_text)
        gs_text.Add(self.p_text, 1, wx.ALL|wx.EXPAND, 20)
        s_options.Add(self.b_options, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 30)
        s_options.Add(self.l_publishing, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.cb_publishing, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.l_date, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.tc_date, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.l_tag, 0, wx.ALL|wx.EXPAND, 5)
        s_options.Add(self.tc_tag, 0, wx.ALL|wx.EXPAND, 5)
        #s_options.Add(self.l_url, 0, wx.ALL|wx.EXPAND, 5)
        #s_options.Add(self.tc_url, 0, wx.ALL|wx.EXPAND, 5)
        self.p_options.SetSizer(s_options)
        gs_text.Add(self.p_options, 1, wx.ALL|wx.EXPAND, 20)
        self.panel.SetSizer(gs_text)
        sizer.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Text
            
    def OnCreatePost(self, evt):
    	self.title = self.tc_title.GetValue().encode('utf-8')
    	self.body = self.tc_post.GetValue().encode('utf-8')
        self.tags = self.tc_tag.GetValue().encode('utf-8')
        self.tags = string.replace(self.tags,' ', ',')
        self.date = self.tc_date.GetValue().encode('utf-8')

        if self.cb_publishing.GetValue() == 'private':
            self.private = 1
        else:
        	self.private = 0
        #print self.cb_publishing.GetValue()
        if self.cb_publishing.GetValue() == 'add to queue':
            self.date = 'on.2'


        #self.format = None
        self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
    	try:
    		self.post = self.api.write_regular(self.title, self.body)
    	except:
    		print "Posteado en blog primario"	
    	#print "Posteado en " % self.post
    	#assert False,dir(self.post.values)
    	self.Close()

    def OnCancel(self, evt):
	    self.Close()

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    d_text = Text(None, -1, "")
    app.SetTopWindow(d_text)
    d_text.Show()
    app.MainLoop()
