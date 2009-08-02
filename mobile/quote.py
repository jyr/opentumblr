import ppygui as gui

class Quote(gui.CeFrame):
	def __init__(self):
		gui.CeFrame.__init__(self, title="Opentumblr CE")
		
		self.l_quote = gui.Label(self, "Add a Quote", align = "center")
		self.l_title = gui.Label(self, "Quote")
		self.tc_title = gui.Edit(self, multiline = True)
		self.l_source = gui.Label(self, "Source (optional)")
		self.tc_source = gui.Edit(self,multiline = True)
		
		self.b_create = gui.Button(self, "Create Post")
		self.b_cancel = gui.Button(self, "Cancel")
		
		self.__set_properties()
		self.__do_layout()
	
	def __set_properties(self):
		pass
	
	def __do_layout(self):
		s_quote = gui.VBox(border = (5,5,5,5), spacing = 5)
		s_quote.add(self.l_quote)
		s_quote.add(self.l_title)
		s_quote.add(self.tc_title)
		s_quote.add(self.l_source)
		s_quote.add(self.tc_source)
		s_quote.add(self.b_create)
		s_quote.add(self.b_cancel)
		
		self.sizer = s_quote

if __name__ == '__main__':
	app = gui.Application(Quote())
	app.run()