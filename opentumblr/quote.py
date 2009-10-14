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

class Quote(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.parent = parent
        self.api = self.parent.api
        self.tags = None
        self.date = None
        self.private = 0

        self.p_main = wx.Panel(self, -1)
        self.s_quote_staticbox = wx.StaticBox(self.p_main, -1, "")
        self.b_options = wx.Button(self.p_main, -1, "Advanced  options")
        self.l_addquote = wx.StaticText(self.p_main, -1, "Add a Quote")
        self.l_quote = wx.StaticText(self.p_main, -1, "Quote")
        self.tc_quote = wx.TextCtrl(self.p_main, -1, "")
        self.l_source = wx.StaticText(self.p_main, -1, "Source ( optional )")
        self.tc_source = wx.TextCtrl(self.p_main, -1, "")
        self.b_create = wx.Button(self.p_main, -1, "Create post")
        self.b_cancel = wx.Button(self.p_main, -1, "Cancel")
        
        self.Bind(wx.EVT_BUTTON, self.AdvancedOptions, id = self.b_options.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCreateQuote, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.l_addquote.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_quote.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        #self.tc_quote.SetMinSize((250, 130))
        self.l_source.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        #self.tc_source.SetMinSize((250, 130))
        self.p_main.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
	    s_main = wx.BoxSizer(wx.VERTICAL)
	    s_quote = wx.StaticBoxSizer(self.s_quote_staticbox, wx.VERTICAL)
	    s_buttons = wx.BoxSizer(wx.HORIZONTAL)
	    s_quote.Add(self.b_options, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 2)
	    s_quote.Add(self.l_addquote, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
	    s_quote.Add(self.l_quote, 0, wx.ALL, 2)
	    s_quote.Add(self.tc_quote, 1, wx.ALL|wx.EXPAND, 5)
	    s_quote.Add(self.l_source, 0, wx.ALL, 2)
	    s_quote.Add(self.tc_source, 1, wx.ALL|wx.EXPAND, 5)
	    s_buttons.Add(self.b_create, 1, wx.LEFT|wx.EXPAND, 2)
	    s_buttons.Add(self.b_cancel, 1, wx.LEFT|wx.EXPAND, 2)
	    s_quote.Add(s_buttons, 0, wx.ALL|wx.EXPAND, 2)
	    self.p_main.SetSizer(s_quote)
	    s_main.Add(self.p_main, 1, wx.ALL|wx.EXPAND, 10)
	    self.SetSizer(s_main)
	    s_main.Fit(self)
        #self.SetSizer(s_quote)
        #s_quote.Fit(self)
        # end wxGlade

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

    def OnCreateQuote(self, evt):
    	self.quote = self.tc_quote.GetValue().encode('utf-8')
    	self.source = self.tc_source.GetValue().encode('utf-8')
        
        if self.quote:
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_quote(self.quote, self.source)
            except:
                print "posteado en el blog primario"
            self.OnCancel(self)
        else:
            Message('Quote is required')

    def OnCancel(self, evt):
        """ Sirve para cancel y cerrar la opcion de text """
        self.parent.SetPanel(None)
