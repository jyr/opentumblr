import ppygui as gui

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

if __name__ == '__main__':
	app = gui.Application(Login())
	app.run()