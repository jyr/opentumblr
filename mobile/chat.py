import ppygui as gui

from tumblr import Api

class Chat(gui.CeFrame):
	def __init__(self, api):
		self.api = api
		gui.CeFrame.__init__(self, title="Opentumblr CE")
		
		self.l_chat = gui.Label(self, "Add a Chat Post", align = "center")
		self.l_title = gui.Label(self, "Title (optional)")
		self.tc_title = gui.Edit(self)
		self.l_dialogue = gui.Label(self, "Dialogue")
		self.l_example = gui.Label(self, "Example")
		self.l_tourist = gui.Label(self, "Tourist: Could you give us directions to Olive Garden")
		self.l_nyorker = gui.Label(self, "New Yorker: No, but I could give you directions to an actual Italian restaurant.")
		self.tc_dialogue = gui.Edit(self,multiline = True)
		
		self.b_create = gui.Button(self, "Create Post")
		self.b_cancel = gui.Button(self, "Cancel")
		
		self.b_create.bind(clicked = self.OnCreateChat)
		self.b_cancel.bind(clicked = self.OnCancel)
		
		self.__set_properties()
		self.__do_layout()
	
	def __set_properties(self):
		pass
	
	def __do_layout(self):
		s_chat = gui.VBox(border = (5,5,5,5), spacing = 5)
		s_chat.add(self.l_chat)
		s_chat.add(self.l_title)
		s_chat.add(self.tc_title)
		s_chat.add(self.l_dialogue)
		s_chat.add(self.l_example)
		s_chat.add(self.l_tourist)
		s_chat.add(self.l_nyorker)
		s_chat.add(self.tc_dialogue)
		s_chat.add(self.b_create)
		s_chat.add(self.b_cancel)
		
		self.sizer = s_chat
	
	def OnCreateChat(self, evt):
		self.title = self.tc_title.get_text()
		self.conversation = self.tc_dialogue.get_text()
		
		if self.conversation:
			self.api = Api(self.api.name, self.api.email, self.api.password)
			try:
				self.post = self.api.write_conversation(self.title, self.conversation)
			except:
				print "Posteado en el primario"
			self.close()
		else:
			gui.Message.ok(title = 'Warning', caption = 'Dialogue is required')
	
	def OnCancel(self, evt):
		self.close()

#if __name__ == '__main__':
#	app = gui.Application(Chat())
#	app.run()