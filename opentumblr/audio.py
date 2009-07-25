#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Sun May  3 23:48:21 2009

import wx
import string
from message import Message

try:
    from opentumblr.tumblr import Api
except ImportError:
    from tumblr import Api
import wx.lib.filebrowsebutton as filebrowse

# begin wxGlade: extracode
# end wxGlade



class Audio(wx.Dialog):
    def __init__(self, parent, id):
        # begin wxGlade: Audio.__init__
        self.parent = parent
        self.api = self.parent.api
    	wx.Dialog.__init__(self, parent, id, style = wx.DEFAULT_DIALOG_STYLE)
        self.panel = wx.Panel(self, -1)
        self.p_options = wx.Panel(self.panel, -1)
        self.p_audio = wx.Panel(self.panel, -1)
        self.s_audiofileurl_staticbox = wx.StaticBox(self.p_audio, -1, "")
        self.s_audio_staticbox = wx.StaticBox(self.p_audio, -1, "")
        self.s_options_staticbox = wx.StaticBox(self.p_options, -1, "")
        self.s_browse_staticbox = wx.StaticBox(self.p_audio, -1, "")
        self.l_addaudio = wx.StaticText(self.p_audio, -1, "Upload an Audio Post")
        self.l_audiofile = wx.StaticText(self.p_audio, -1, "Audio File")
        self.b_browse = filebrowse.FileBrowseButton(self.p_audio, -1, size=(703,-1))

        """
        Not supported in the tumblr api at this time
        self.l_audiofileurl = wx.StaticText(self.p_audio, -1, "Photo Url")
        self.tc_audiofileurl = wx.TextCtrl(self.p_audio, -1, "")
        """
        
        self.l_caption = wx.StaticText(self.p_audio, -1, "Caption (optional)")
        self.tc_caption = wx.TextCtrl(self.p_audio, -1, "", style=wx.TE_MULTILINE)
        self.b_create = wx.Button(self.p_audio, -1, "Create post")
        self.b_cancel = wx.Button(self.p_audio, -1, "Cancel")
        self.b_options = wx.Button(self.p_options, -1, "Advanced  options")
        self.l_publishing = wx.StaticText(self.p_options, -1, "Publishing options")
        
        """
        Not supported in the tumblr api at this time
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "add to queue", "publish on...", "save as draft", "private"], style=wx.CB_DROPDOWN)        
        """
        
        self.cb_publishing = wx.ComboBox(self.p_options, -1, choices=["publish now", "publish on...", "private"], style=wx.CB_DROPDOWN)
        self.l_date = wx.StaticText(self.p_options, -1, "Date this post")
        self.tc_date = wx.TextCtrl(self.p_options, -1, "")
        self.l_tag = wx.StaticText(self.p_options, -1, "Tag this post")
        self.tc_tag = wx.TextCtrl(self.p_options, -1, "", style=wx.TE_MULTILINE)

        """"
        Not supported in the tumblr api at this time
        self.l_url = wx.StaticText(self.p_options, -1, "Set a custom post URL")
        self.tc_url = wx.TextCtrl(self.p_options, -1, "/post/123456/")
        """

        self.Bind(wx.EVT_BUTTON, self.OnCreateAudio, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())
        self.Bind(wx.EVT_COMBOBOX, self.GetParent().OnPublishingOptions, id = self.cb_publishing.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Audio.__set_properties
        self.SetTitle("Upload an Audio Post")
        self.SetBackgroundColour(wx.Colour(55, 85, 113))
        self.l_addaudio.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_addaudio.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_audiofile.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_audiofile.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        
        """
        Not supported in the tumblr api at this time
        self.l_audiofileurl.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_audiofileurl.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_audiofileurl.SetMinSize((500, 25))
        self.tc_audiofileurl.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        """
        
        self.l_caption.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.l_caption.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_caption.SetMinSize((640, 200))
        self.tc_caption.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.p_audio.SetBackgroundColour(wx.Colour(255, 255, 255))
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
        # begin wxGlade: Audio.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        gs_audio = wx.FlexGridSizer(1, 2, 0, 0)
        s_options = wx.StaticBoxSizer(self.s_options_staticbox, wx.VERTICAL)
        s_audio = wx.StaticBoxSizer(self.s_audio_staticbox, wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.HORIZONTAL)

        """
        Not supported in the tumblr api at this time
        s_audiofileurl = wx.StaticBoxSizer(self.s_audiofileurl_staticbox, wx.HORIZONTAL)
        """

        s_browse = wx.StaticBoxSizer(self.s_browse_staticbox, wx.HORIZONTAL)
        s_audio.Add(self.l_addaudio, 0, wx.ALL|wx.EXPAND, 2)
        s_audio.Add(self.l_audiofile, 0, wx.ALL|wx.EXPAND, 2)
        s_browse.Add(self.b_browse, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_audio.Add(s_browse, 0, wx.EXPAND, 0)
        
        """
        Not supported in the tumblr api at this time
        s_audiofileurl.Add(self.l_audiofileurl, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_audiofileurl.Add(self.tc_audiofileurl, 0, wx.ALL|wx.EXPAND, 2)
        s_audio.Add(s_audiofileurl, 0, wx.EXPAND, 0)
        """
        
        s_audio.Add(self.l_caption, 0, wx.ALL|wx.EXPAND, 2)
        s_audio.Add(self.tc_caption, 0, wx.ALL|wx.EXPAND, 10)
        s_buttons.Add(self.b_create, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_buttons.Add(self.b_cancel, 0, wx.LEFT|wx.ALIGN_CENTER_VERTICAL, 520)
        s_audio.Add(s_buttons, 0, wx.ALL|wx.EXPAND, 2)
        self.p_audio.SetSizer(s_audio)
        gs_audio.Add(self.p_audio, 1, wx.ALL|wx.EXPAND, 20)
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
        gs_audio.Add(self.p_options, 1, wx.ALL|wx.EXPAND, 20)
        self.panel.SetSizer(gs_audio)
        sizer.Add(self.panel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
        # end wxGlade

# end of class Audio
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
        self.tags = self.tc_tag.GetValue().encode('utf-8')
        self.tags = string.replace(self.tags,' ', ',')
        self.date = self.tc_date.GetValue().encode('utf-8')

        if self.cb_publishing.GetValue() == 'private':
        	self.private = 1
        else:
        	self.private = 0

        if self.data or self.source:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_audio(self.data, self.source, self.caption)
            except:
                print "audio posteado en el blog primario"
            self.Close()
        else:
            Message('Audio File is required')
    def OnCancel(self, evt):
        self.Close()

if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    d_audio = Audio(None, -1, "")
    app.SetTopWindow(d_audio)
    d_audio.Show()
    app.MainLoop()
