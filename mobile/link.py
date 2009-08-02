import ppygui as gui

class Link(gui.CeFrame):
	def __init__(self):
		gui.CeFrame.__init__(self, title="Opentumblr CE")
		
		self.l_link = gui.Label(self, "Add a Link", align = "center")
		self.l_name = gui.Label(self, "Name (optional)")
		self.tc_name = gui.Edit(self)
		self.l_url = gui.Label(self, "URL")
		self.tc_url = gui.Edit(self)
		self.l_description = gui.Label(self, "Description (optional)")
		self.tc_description = gui.Edit(self,multiline = True)
		
		self.b_create = gui.Button(self, "Create Post")
		self.b_cancel = gui.Button(self, "Cancel")
		
		self.__set_properties()
		self.__do_layout()
	
	def __set_properties(self):
		pass
	
	def __do_layout(self):
		s_link = gui.VBox(border = (5,5,5,5), spacing = 5)
		s_link.add(self.l_link)
		s_link.add(self.l_name)
		s_link.add(self.tc_name)
		s_link.add(self.l_url)
		s_link.add(self.tc_url)
		s_link.add(self.l_description)
		s_link.add(self.tc_description)
		s_link.add(self.b_create)
		s_link.add(self.b_cancel)
		
		self.sizer = s_link

if __name__ == '__main__':
	app = gui.Application(Link())
	app.run()