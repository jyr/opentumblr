import ppygui as gui

class Text(gui.CeFrame):
	def __init__(self):
		gui.CeFrame.__init__(self, title="Opentumblr CE")
		
		self.l_text = gui.Label(self, "Add a Text Post", align = "center")
		self.l_title = gui.Label(self, "Title (optional)")
		self.tc_title = gui.Edit(self)
		self.l_post = gui.Label(self, "Post")
		self.tc_post = gui.Edit(self,multiline = True)
		
		self.b_create = gui.Button(self, "Create Post")
		self.b_cancel = gui.Button(self, "Cancel")
		
		self.__set_properties()
		self.__do_layout()
	
	def __set_properties(self):
		pass
	
	def __do_layout(self):
		s_text = gui.VBox(border = (5,5,5,5), spacing = 5)
		s_text.add(self.l_text)
		s_text.add(self.l_title)
		s_text.add(self.tc_title)
		s_text.add(self.l_post)
		s_text.add(self.tc_post)
		s_text.add(self.b_create)
		s_text.add(self.b_cancel)
		
		self.sizer = s_text

if __name__ == '__main__':
	app = gui.Application(Text())
	app.run()