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

class Link(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.parent = parent
        self.api = self.parent.api
        self.tags = None
        self.date = None
        self.private = 0

        self.p_main = wx.Panel(self, -1)
        self.s_link_staticbox = wx.StaticBox(self.p_main, -1, "")
        self.b_options = wx.Button(self.p_main, -1, "Advanced  options")
        self.l_addlink = wx.StaticText(self.p_main, -1, "Add a Link")
        self.l_name = wx.StaticText(self.p_main, -1, "Name (optional)")
        self.tc_name = wx.TextCtrl(self.p_main, -1, "")
        self.l_urllink = wx.StaticText(self.p_main, -1, "URL")
        self.tc_urllink = wx.TextCtrl(self.p_main, -1, "")
        self.l_description = wx.StaticText(self.p_main, -1, "Description (optional)")
        self.tc_description = wx.TextCtrl(self.p_main, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_main, -1, "Create post")
        self.b_cancel = wx.Button(self.p_main, -1, "Cancel")
        
        self.Bind(wx.EVT_BUTTON, self.AdvancedOptions, id = self.b_options.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCreateLink, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.l_addlink.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_name.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_name.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_urllink.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_description.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        #self.tc_description.SetMinSize((245, 203))
        self.tc_description.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.p_main.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
	    s_main = wx.BoxSizer(wx.VERTICAL)
	    s_link = wx.StaticBoxSizer(self.s_link_staticbox, wx.VERTICAL)
	    s_buttons = wx.BoxSizer(wx.HORIZONTAL)
	    s_link.Add(self.b_options, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 2)
	    s_link.Add(self.l_addlink, 0, wx.ALL, 2)
	    s_link.Add(self.l_name, 0, wx.ALL, 2)
	    s_link.Add(self.tc_name, 0, wx.ALL|wx.EXPAND, 2)
	    s_link.Add(self.l_urllink, 0, wx.ALL, 2)
	    s_link.Add(self.tc_urllink, 0, wx.ALL|wx.EXPAND, 2)
	    s_link.Add(self.l_description, 0, wx.ALL, 2)
	    s_link.Add(self.tc_description, 1, wx.ALL|wx.EXPAND, 2)
	    s_buttons.Add(self.b_create, 1, wx.LEFT|wx.EXPAND, 2)
	    s_buttons.Add(self.b_cancel, 1, wx.LEFT|wx.EXPAND, 2)
	    s_link.Add(s_buttons, 0, wx.ALL|wx.EXPAND, 2)
	    self.p_main.SetSizer(s_link)
	    s_main.Add(self.p_main, 1, wx.ALL|wx.EXPAND, 10)
	    self.SetSizer(s_main)
	    s_main.Fit(self)


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

    def OnCreateLink(self, evt):
    	self.name = self.tc_name.GetValue().encode('utf-8')
    	self.urllink = self.tc_urllink.GetValue()
    	self.description = self.tc_description.GetValue().encode('utf-8')
        
        if self.urllink:
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_link(self.name,self.urllink,self.description)
            except:
                print "posteado en el blog primario"
            self.OnCancel(self)
        else:
            Message('URL is required')
    
    def OnCancel(self, evt):
	    """ Sirve para cancel y cerrar la opcion de text """
	    self.parent.SetPanel(None)
