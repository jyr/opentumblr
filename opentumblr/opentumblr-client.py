#!/usr/bin/env python
import urllib2
import wx

try:
    import tumblr
    from tumblr import Api
    from dashboard import Dashboard
    from invalid import Invalid
except ImportError:
    import opentumblr.tumblr
    from opentumblr.tumblr import Api
    from opentumblr.dashboard import Dashboard
    from opentumblr.invalid import Invalid
# begin wxGlade: extracode
# end wxGlade

errors = {'403':'Login o password incorrectos','404':'Tumblrlog incorrecto','urlopen':'no ingreso su tumblrlog'}

class Login(wx.Frame):
    def __init__(self, parent, id):
        # begin wxGlade: Login.__init__
        #kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.FULL_REPAINT_ON_RESIZE|wx.CLIP_CHILDREN
        wx.Frame.__init__(self, parent, id)
        self.parent = parent
        self.panel_login = wx.Panel(self, -1)
        self.l_tumblr = wx.StaticText(self, -1, "tumblr", style=wx.ALIGN_CENTRE)
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
        # end wxGlade

    def __set_properties(self):
        self.SetTitle("Opentumblr")
        self.SetSize((290, 570))
        self.l_tumblr.SetFont(wx.Font(40, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Login.__do_layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer_login = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.l_tumblr, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 15)
        sizer_login.Add(self.l_mail, 0, 0, 0)
        sizer_login.Add(self.cb_mail, 0, wx.EXPAND, 0)
        sizer_login.Add(self.l_password, 0, 0, 0)
        sizer_login.Add(self.tc_password, 0, wx.EXPAND, 0)
        sizer_login.Add(self.l_blog, 0, 0, 0)
        sizer_login.Add(self.tc_blog, 0, wx.EXPAND, 0)
        sizer_login.Add((20, 20), 0, wx.ALL|wx.EXPAND, 5)
        sizer_login.Add(self.b_login, 0, wx.ALL|wx.EXPAND, 5)
        self.panel_login.SetSizer(sizer_login)
        sizer.Add(self.panel_login, 1, wx.ALL|wx.EXPAND, 10)
        sizer.Add((250, 180), 0, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer)
        self.Layout()
        # end wxGlade

# end of class Login
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
		    self.dashboard = Dashboard(None, -1, self.api)
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
