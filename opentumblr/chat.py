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

class Chat(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.parent = parent
        self.api = self.parent.api
        self.tags = None
        self.date = None
        self.private = 0

        self.p_main = wx.Panel(self, -1)
        self.s_chat_staticbox = wx.StaticBox(self.p_main, -1, "")
        self.b_options = wx.Button(self.p_main, -1, "Advanced  options")
        self.l_addchat = wx.StaticText(self.p_main, -1, "Add a Chat Post")
        self.l_title = wx.StaticText(self.p_main, -1, "Title (optional)")
        self.tc_title = wx.TextCtrl(self.p_main, -1, "")
        self.l_dialogue = wx.StaticText(self.p_main, -1, "Dialogue")
        self.l_example = wx.StaticText(self.p_main, -1, "Example")
        self.l_tourist = wx.StaticText(self.p_main, -1, "Tourist: Could you give us directions to Olive Garden?")
        self.l_nyorker = wx.StaticText(self.p_main, -1, "New Yorker:No,but I could give you directions to an actual restaurant.")
        self.tc_dialogue = wx.TextCtrl(self.p_main, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_main, -1, "Create post")
        self.b_cancel = wx.Button(self.p_main, -1, "Cancel")
        
        self.Bind(wx.EVT_BUTTON, self.AdvancedOptions, id = self.b_options.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCreateChat, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_addchat.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_title.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_dialogue.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_example.SetBackgroundColour(wx.Colour(216, 216, 191))
        self.l_example.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_tourist.SetBackgroundColour(wx.Colour(216, 216, 191))
        self.l_tourist.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.l_nyorker.SetBackgroundColour(wx.Colour(216, 216, 191))
        self.l_nyorker.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        #self.tc_dialogue.SetMinSize((260, 202))
        self.p_main.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
	    s_main = wx.BoxSizer(wx.VERTICAL)
	    s_chat = wx.StaticBoxSizer(self.s_chat_staticbox, wx.VERTICAL)
	    s_buttons = wx.BoxSizer(wx.HORIZONTAL)
	    s_chat.Add(self.b_options, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 2)
	    s_chat.Add(self.l_addchat, 0, wx.ALL, 2)
	    s_chat.Add(self.l_title, 0, wx.ALL, 2)
	    s_chat.Add(self.tc_title, 0, wx.ALL|wx.EXPAND, 10)
	    s_chat.Add(self.l_dialogue, 0, wx.ALL, 2)
	    s_chat.Add(self.l_example, 0, wx.LEFT|wx.TOP, 2)
	    s_chat.Add(self.l_tourist, 0, wx.LEFT, 2)
	    s_chat.Add(self.l_nyorker, 0, wx.LEFT, 2)
	    s_chat.Add(self.tc_dialogue, 1, wx.ALL|wx.EXPAND, 2)
	    s_buttons.Add(self.b_create, 1, wx.LEFT|wx.EXPAND, 2)
	    s_buttons.Add(self.b_cancel, 1, wx.LEFT|wx.EXPAND, 2)
	    s_chat.Add(s_buttons, 0, wx.ALL|wx.EXPAND, 2)
	    self.p_main.SetSizer(s_chat)
	    s_main.Add(self.p_main, 1, wx.ALL|wx.EXPAND, 10)
	    self.SetSizer(s_main)
	    s_main.Fit(self)
        #self.SetSizer(s_chat)
        #s_chat.Fit(self)

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

    def OnCreateChat(self, evt):
    	self.title = self.tc_title.GetValue().encode('utf-8')
    	self.conversation = self.tc_dialogue.GetValue().encode('utf-8')
        
        if self.conversation:
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_conversation(self.title, self.conversation)
            except:
                print "posteado en el blog primario"
            self.OnCancel(self)
        else:
            Message('Dialogue is required')

    def OnCancel(self, evt):
	    """ Sirve para cancel y cerrar la opcion de text """
	    self.parent.SetPanel(None)
