#!/usr/bin/env python
# -*- coding: us-ascii -*-
# generated by wxGlade 0.6.3 on Fri Aug 14 15:46:15 2009

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



class Photo(wx.Panel):
    def __init__(self, parent, id):
        # begin wxGlade: Photo.__init__
        #kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, parent, id)
        self.parent = parent
        self.api = self.parent.api
        self.s_photo_staticbox = wx.StaticBox(self, -1, "")
        self.s_browse_staticbox = wx.StaticBox(self, -1, "")
        self.l_addphoto = wx.StaticText(self, -1, "Upload a Photo")
        self.l_photo = wx.StaticText(self, -1, "Photo")
        self.b_browse = filebrowse.FileBrowseButton(self, -1)
        self.l_supports = wx.StaticText(self, -1, "Supports JPEG, GIF, PNG and BMP.  Max photo size is 10 MB.     ")
        self.l_photourl = wx.StaticText(self, -1, "Photo Url")
        self.tc_photourl = wx.TextCtrl(self, -1, "")
        self.l_caption = wx.StaticText(self, -1, "Caption")
        self.tc_caption = wx.TextCtrl(self, -1, "", style=wx.TE_MULTILINE)
        self.l_photolink = wx.StaticText(self, -1, "Photo links to the URL")
        self.tc_photolink = wx.TextCtrl(self, -1, "")
        self.b_create = wx.Button(self, -1, "Create post")
        self.b_cancel = wx.Button(self, -1, "Cancel")
        
        self.Bind(wx.EVT_BUTTON, self.OnCreatePhoto, id = self.b_create.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnCancel, id = self.b_cancel.GetId())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Photo.__set_properties
        self.l_addphoto.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_photo.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_supports.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.l_photourl.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_photourl.SetMinSize((-1, -1))
        self.tc_photourl.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_caption.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.tc_caption.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "Lucida Grande"))
        self.tc_caption.SetMinSize((100, 120))
        self.tc_photolink.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.tc_photolink.SetFont(wx.Font(25, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Photo.__do_layout
        s_photo = wx.StaticBoxSizer(self.s_photo_staticbox, wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.HORIZONTAL)
        s_photolink = wx.BoxSizer(wx.VERTICAL)
        s_photourl = wx.BoxSizer(wx.HORIZONTAL)
        s_browse = wx.StaticBoxSizer(self.s_browse_staticbox, wx.HORIZONTAL)
        s_photo.Add(self.l_addphoto, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_photo.Add(self.l_photo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_browse.Add(self.b_browse, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_photo.Add(s_browse, 0, wx.EXPAND, 0)
        s_photo.Add(self.l_supports, 0, wx.BOTTOM, 20)
        s_photourl.Add(self.l_photourl, 0, wx.ALL, 2)
        s_photourl.Add(self.tc_photourl, 1, wx.ALL|wx.EXPAND, 2)
        s_photo.Add(s_photourl, 0, wx.EXPAND, 0)
        s_photo.Add(self.l_caption, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 2)
        s_photo.Add(self.tc_caption, 0, wx.ALL|wx.EXPAND, 2)
        s_photolink.Add(self.l_photolink, 0, wx.ALL, 2)
        s_photolink.Add(self.tc_photolink, 0, wx.ALL|wx.EXPAND, 2)
        s_photo.Add(s_photolink, 0, wx.EXPAND, 0)
        s_buttons.Add(self.b_create, 1, wx.LEFT|wx.EXPAND, 2)
        s_buttons.Add(self.b_cancel, 1, wx.LEFT|wx.EXPAND, 2)
        s_photo.Add(s_buttons, 0, wx.ALL|wx.EXPAND, 2)
        self.SetSizer(s_photo)
        s_photo.Fit(self)
        # end wxGlade

# end of class Photo
    def OnCreatePhoto(self, evt):
    	self.source = self.tc_photourl.GetValue()
    	if not self.source:
    		self.source = None

    	self.data = self.b_browse.GetValue()
    	if not self.data:
    		self.data = None
    	
    	print dir(self.api)

    	self.caption = self.tc_caption.GetValue().encode('utf-8')
    	self.click  = self.tc_photolink.GetValue()
        self.tags = self.tc_tag.GetValue().encode('utf-8')
        self.tags = string.replace(self.tags,' ', ',')
        self.date = self.tc_date.GetValue().encode('utf-8')

        if self.cb_publishing.GetValue() == 'private':
        	self.private = 1
        else:
        	self.private = 0
        	
        
        if self.source or self.data:
            #self.format = None
            self.api = Api(self.api.name, self.api.email, self.api.password, self.private, self.date, self.tags)
            try:
                self.post = self.api.write_photo(self.source, self.data, self.caption, self.click)
            except:
                print "Posteado en el primario"
            self.Close()
        else:
            Message('Photo is required')
            
    def OnCancel(self, evt):
        self.Close()
    

