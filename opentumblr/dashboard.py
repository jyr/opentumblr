#!/usr/bin/env python
# -*- coding: us-ascii -*-

import wx
import os,sys
from tumblelog import TumbleLog


ID_TEXT = wx.NewId()
ID_PHOTO = wx.NewId()
ID_QUOTE = wx.NewId()
ID_LINK = wx.NewId()
ID_CHAT = wx.NewId()
ID_AUDIO = wx.NewId()
ID_VIDEO = wx.NewId()
ID_TUMBLELOG = wx.NewId()


class Dashboard(wx.Frame):
    def __init__(self, parent, id, api, path_images):
        wx.Frame.__init__(self, parent, id)
        self.parent = parent
        self.api = api
        self.path_images = path_images

        self.toolbar_dashboard = ToolBarDashboard(self, -1)
        self.SetToolBar(self.toolbar_dashboard)

        self.panel = TumbleLog(self, -1)
        #self.panel = wx.Panel(self, -1)
        self.b_logout = wx.Button(self, -1, "Logout")
        self.Center()
        self.panel.SetPanel(None)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_TEXT)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_PHOTO)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_QUOTE)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_LINK)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_CHAT)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_AUDIO)
        self.Bind(wx.EVT_TOOL, self.SelectPanel, id = ID_VIDEO)
        self.Bind(wx.EVT_BUTTON, self.OnLogout, id = self.b_logout.GetId())

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("Opentumblr")
        self.panel.SetMinSize((330, 458))
        self.panel.SetBackgroundColour(wx.Colour(47, 47, 47))

    def __do_layout(self):
        s_dashboard = wx.BoxSizer(wx.VERTICAL)
        s_buttons = wx.BoxSizer(wx.VERTICAL)
        s_dashboard.Add(self.panel, 1, wx.EXPAND, 0)
        s_buttons.Add(self.b_logout, 1, wx.ALL|wx.EXPAND, 10)
        s_dashboard.Add(s_buttons, 0, wx.EXPAND, 0)
        self.SetSizer(s_dashboard)
        s_dashboard.Fit(self)
        self.Layout()

    def SelectPanel(self, evt):
        evt_id = evt.GetId()
        if evt_id == ID_TEXT:
            self.panel.SetPanel("TEXT")
        elif evt_id == ID_PHOTO:
            self.panel.SetPanel("PHOTO")
        elif evt_id == ID_QUOTE:
            self.panel.SetPanel("QUOTE")
        elif evt_id == ID_LINK:
            self.panel.SetPanel("LINK")
        elif evt_id == ID_CHAT:
            self.panel.SetPanel("CHAT")
        elif evt_id == ID_AUDIO:
            self.panel.SetPanel("AUDIO")
        elif evt_id == ID_VIDEO:
            self.panel.SetPanel("VIDEO")
        else:
            evt.Skip()

    def OnLogout(self, evt):
    	self.Close()

class MyArtProvider(wx.ArtProvider):
    def CreateBitmap(self, artId, artClient, size):
	    return wx.Bitmap(artId, wx.BITMAP_TYPE_PNG)
		
class ToolBarDashboard(wx.ToolBar):
    def __init__(self, parent, id):
        wx.ToolBar.__init__(self, parent, id, style=wx.TB_TEXT)
        self.path_images = parent.path_images

        self.AddSeparator()
        self.__create_toolbar()
        self.AddSeparator()

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetToolBitmapSize((16, 15))
        self.SetToolPacking(1)
        self.Realize()

    def __do_layout(self):
        pass

    def __create_toolbar(self):
	    #assert False,wx.Platform
	    if wx.Platform == '__WXMAC__':
		    self.AddLabelTool(ID_TEXT, "Txt", wx.Bitmap(self.path_images + "/textmac.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_PHOTO, "Photo", wx.Bitmap(self.path_images + "/photomac.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_QUOTE, "Quote", wx.Bitmap(self.path_images + "/quotemac.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_LINK, "Link", wx.Bitmap(self.path_images + "/linkmac.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_CHAT, "Chat", wx.Bitmap(self.path_images + "/chatmac.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_AUDIO, "Audio", wx.Bitmap(self.path_images + "/audiomac.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_VIDEO, "Video", wx.Bitmap(self.path_images + "/videomac.png", wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
	    else:
		    wx.ArtProvider.Push(MyArtProvider())
		    if wx.Platform == '__WXMSW__':
			    size = (35, 49)
			    self.path_images += '\\'
		    else:
			    size = (30, 44)
			    self.path_images += '/'
				
		    self.AddLabelTool(ID_TEXT, "", wx.ArtProvider.GetBitmap(self.path_images + 'text.png', wx.ART_TOOLBAR, size), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_PHOTO, "", wx.ArtProvider.GetBitmap(self.path_images + 'photo.png', wx.ART_TOOLBAR, size), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_QUOTE, "", wx.ArtProvider.GetBitmap(self.path_images + 'quote.png', wx.ART_TOOLBAR, size), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_LINK, "", wx.ArtProvider.GetBitmap(self.path_images + 'link.png', wx.ART_TOOLBAR, size), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_CHAT, "", wx.ArtProvider.GetBitmap(self.path_images + 'chat.png', wx.ART_TOOLBAR, size), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_AUDIO, "", wx.ArtProvider.GetBitmap(self.path_images + 'audio.png', wx.ART_TOOLBAR, size), wx.NullBitmap, wx.ITEM_NORMAL, "", "")
		    self.AddLabelTool(ID_VIDEO, "", wx.ArtProvider.GetBitmap(self.path_images + 'video.png', wx.ART_TOOLBAR, size), wx.NullBitmap, wx.ITEM_NORMAL, "", "")		    



if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    f_dashboard = Dashboard(None, -1, "")
    app.SetTopWindow(f_dashboard)
    f_dashboard.Show()
    app.MainLoop()
