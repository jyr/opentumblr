import ppygui as gui

import tumblr
from tumblr import Api
from dashboard import Dashboard

class Login(gui.CeFrame):
	def __init__(self):
		gui.CeFrame.__init__(self, title="Opentumblr CE")
		self.l_tumblr = gui.Label(self, "Tumblr", align = "center")
		self.l_login = gui.Label(self, "Log in")
		self.l_mail = gui.Label(self, "Email address")
		self.tc_mail = gui.Edit(self)
		self.l_password = gui.Label(self, "Password")
		self.tc_password = gui.Edit(self, password = True)
		self.l_blog = gui.Label(self, "Blog")
		self.tc_blog = gui.Edit(self)
		self.b_login = gui.Button(self, "Login")
		
		self.b_login.bind(clicked = self.OnAuthTumblr)
		
		self.__set_properties()
		self.__do_layout()
	
	def __set_properties(self):
		pass
	
	def __do_layout(self):
		sizer_login = gui.VBox(border = (5,5,5,5), spacing = 5)
		sizer_login.add(self.l_tumblr)
		sizer_login.add(self.l_login)
		sizer_login.add(self.l_mail)
		sizer_login.add(self.tc_mail)
		sizer_login.add(self.l_password)
		sizer_login.add(self.tc_password)
		sizer_login.add(self.l_blog)
		sizer_login.add(self.tc_blog)
		sizer_login.add(self.b_login)
		
		self.sizer = sizer_login
	
	def OnAuthTumblr(self, evt):
		self.Blog = self.tc_blog.get_text()
		self.User = self.tc_mail.get_text()
		self.Password = self.tc_password.get_text()
		
		self.api = Api(self.Blog, self.User, self.Password)
		try:
			self.auth = self.api.auth_check()
			self.dashboard = Dashboard(self.api)
		except tumblr.TumblrAuthError:
			gui.Message.ok(title = 'Error', caption = 'Invalid email or password. Please try again')
		
if __name__ == '__main__':
	app = gui.Application(Login())
	app.run()