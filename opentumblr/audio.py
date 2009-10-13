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
import wx.lib.filebrowsebutton as filebrowse

class Audio(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)
        self.parent = parent
        self.api = self.parent.api
        self.tags = None
        self.date = None
        self.private = 0

        self.p_main = wx.Panel(self, -1)
        self.s_audio_staticbox = wx.StaticBox(self.p_main, -1, "")
        self.s_browse_staticbox = wx.StaticBox(self.p_main, -1, "")
        self.b_options = wx.Button(self.p_main, -1, "Advanced  options")
        self.l_addaudio = wx.StaticText(self.p_main, -1, "Upload an Audio Post")
        self.l_audiofile = wx.StaticText(self.p_main, -1, "Audio File")
        self.b_browse = filebrowse.FileBrowseButton(self.p_main, -1)
        
        """
        Not supported in the tumblr api at this time
        self.l_audiofileurl = wx.StaticText(self.p_main, -1, "Photo Url")
        self.tc_audiofileurl = wx.TextCtrl(self.p_main, -1, "")
        """
        
        self.l_caption = wx.StaticText(self.p_main, -1, "Caption (optional)")
        self.tc_caption = wx.TextCtrl(self.p_main, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_main, -1, "Create post")
        self.b_cancel = wx.Button(self.p_main, -1, "Cancel")
        
        self.Bind(wx.EVT_BUTTON, self.AdvancedOptions, id = self.b_options.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCreateAudio, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.l_addaudio.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_audiofile.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        
        """
        Not supported in the tumblr api at this time
        self.l_audiofileurl.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        """
        
        self.l_caption.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_caption.SetMinSize((250, 222))
        self.p_main.SetBackgroundColour(wx.Colour(255, 255, 255))

    def __do_layout(self):
	    s_main = wx.BoxSizer(wx.VERTICAL)
	    s_audio = wx.StaticBoxSizer(self.s_audio_staticbox, wx.VERTICAL)
	    s_buttons = wx.BoxSizer(wx.HORIZONTAL)
	    s_audio.Add(self.b_options, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 2)
	    s_audiofileurl = wx.BoxSizer(wx.HORIZONTAL)
	    s_browse = wx.StaticBoxSizer(self.s_browse_staticbox, wx.HORIZONTAL)
	    s_audio.Add(self.l_addaudio, 0, wx.ALL, 2)
	    s_audio.Add(self.l_audiofile, 0, wx.ALL, 2)
	    s_browse.Add(self.b_browse, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
	    s_audio.Add(s_browse, 0, wx.EXPAND, 0)
	
	    """
	    Not supported in the tumblr api at this time
	    s_audiofileurl.Add(self.l_audiofileurl, 0, wx.ALL, 2)
	    s_audiofileurl.Add(self.tc_audiofileurl, 1, wx.ALL|wx.EXPAND, 2)
	    s_audio.Add(s_audiofileurl, 0, wx.EXPAND, 0)
	    """
	    s_audio.Add(self.l_caption, 0, wx.ALL, 2)
	    s_audio.Add(self.tc_caption, 0, wx.ALL|wx.EXPAND, 2)
	    s_buttons.Add(self.b_create, 1, wx.LEFT|wx.EXPAND, 2)
	    s_buttons.Add(self.b_cancel, 1, wx.LEFT|wx.EXPAND, 2)
	    s_audio.Add(s_buttons, 0, wx.ALL|wx.EXPAND, 2)
	    self.p_main.SetSizer(s_audio)
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
    
    def OnCreateAudio(self, evt):
    	self.data = self.b_browse.GetValue()
    	if not self.data:
    		self.data =None
    	
    	"""
    	Not supported in the tumblr api at this time
    	self.source = self.tc_audiofileurl.GetValue()
    	if not self.source:
    		self.source = None
    	"""
    	self.source = None    	
    	self.caption = self.tc_caption.GetValue().encode('utf-8')

        if self.data or self.source:
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_audio(self.data, self.source, self.caption)
            except:
                print "audio posteado en el blog primario"
            self.OnCancel(self)
        else:
            Message('Audio File is required')

    def OnCancel(self, evt):
        """ Sirve para cancel y cerrar la opcion de text """
        self.parent.SetPanel(None)