#!/usr/bin/env python
# -*- coding: us-ascii -*-

import urllib2
import os, sys
import wx

try:
    import tumblr
    from tumblr import Api
    from dashboard import Dashboard
    from invalid import Invalid
except ImportError:
    from opentumblr import tumblr
    from opentumblr.tumblr import Api
    from opentumblr.dashboard import Dashboard
    from opentumblr.invalid import Invalid

errors = {'403':'Login o password incorrectos','404':'Tumblrlog incorrecto','urlopen':'no ingreso su tumblrlog'}

class Login(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id)
        self.parent = parent
        self.p_main = wx.Panel(self, -1)
        self.panel_login = wx.Panel(self.p_main, -1)
        self.path_images = '/usr/share/pixmaps/opentumblr/dashboard/'

        if not os.path.isdir(self.path_images):
	        if sys.platform == "win32":
		        self.path_images = os.path.abspath(os.path.dirname(sys.argv[0])) + '\\..\\images\\'
	        else:
	            self.path_images = os.path.abspath('images') + '/'
	
        self.bitmap_1 = wx.StaticBitmap(self.p_main, -1, wx.Bitmap(self.path_images + "opentumblr.png", wx.BITMAP_TYPE_ANY))
        self.l_mail = wx.StaticText(self.panel_login, -1, "E-mail address")
        self.cb_mail = wx.ComboBox(self.panel_login, -1, choices=[], style=wx.CB_DROPDOWN)
        self.l_password = wx.StaticText(self.panel_login, -1, "Password")
        self.tc_password = wx.TextCtrl(self.panel_login, -1, "", style=wx.TE_PASSWORD)
        self.l_blog = wx.StaticText(self.panel_login, -1, "Blog")
        self.tc_blog = wx.TextCtrl(self.panel_login, -1, "")
        self.b_login = wx.Button(self.panel_login, -1, "Login")

        self.Bind(wx.EVT_BUTTON, self.OnAuthTumblr, id = self.b_login.GetId())

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("Opentumblr")
        self.l_mail.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_password.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.l_blog.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.panel_login.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.p_main.SetBackgroundColour(wx.Colour(47, 47, 47))

    def __do_layout(self):
        s_main = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_login = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.bitmap_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 20)
        sizer_login.Add(self.l_mail, 0, wx.ALL, 5)
        sizer_login.Add(self.cb_mail, 0, wx.ALL|wx.EXPAND, 5)
        sizer_login.Add(self.l_password, 0, wx.ALL, 5)
        sizer_login.Add(self.tc_password, 0, wx.ALL|wx.EXPAND, 5)
        sizer_login.Add(self.l_blog, 0, wx.ALL, 5)
        sizer_login.Add(self.tc_blog, 0, wx.ALL|wx.EXPAND, 5)
        sizer_login.Add((20, 20), 0, wx.ALL|wx.EXPAND, 5)
        sizer_login.Add(self.b_login, 0, wx.ALL|wx.EXPAND, 5)
        self.panel_login.SetSizer(sizer_login)
        sizer.Add(self.panel_login, 1, wx.ALL|wx.EXPAND, 10)
        sizer.Add((320, 155), 0, wx.ALL|wx.EXPAND, 5)
        self.p_main.SetSizer(sizer)
        s_main.Add(self.p_main, 1, wx.EXPAND, 10)
        self.SetSizer(s_main)
        s_main.Fit(self)
        self.Layout()
        self.Centre()

    def OnAuthTumblr(self, event):
	    self.Blog = self.tc_blog.GetValue()
        #if not self.Blog:
	        #self.Blog = ''
	        #assert False,self.Blog
	        #print "Conectado al blog primario: "
	    self.User = self.cb_mail.GetValue()
	    self.Password = self.tc_password.GetValue()
	    self.api = Api(self.Blog, self.User, self.Password)
	    #assert False,dir(self.api)
	    try:
		    self.auth = self.api.auth_check()
		    self.dashboard = Dashboard(None, -1, self.api, self.path_images)
		    self.dashboard.Show()
		    self.Close()
		    #print "Te haz logueado"
	    except tumblr.TumblrAuthError:
	    	self.invalid = Invalid(self)
	    	self.invalid.Show()
	    	print errors['403']
	    except urllib2.HTTPError:
	    	print errors['404']
	    except urllib2.URLError:
	    	print errors['urlopen']


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    f_login = Login(None, -1)
    app.SetTopWindow(f_login)
    f_login.Show()
    app.MainLoop()
