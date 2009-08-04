import ppygui as gui

class Audio(gui.CeFrame):
	def __init__(self):
		gui.CeFrame.__init__(self, title="Opentumblr CE")
		
		self.l_audio = gui.Label(self, "Upload an Audio Post", align = "center")
		self.l_file = gui.Label(self, "Audio File")
		self.b_browse = gui.Button(self, "Open a file", action = self.OnOpen)
		self.l_audiourl = gui.Label(self, "Audio Url")
		self.tc_audiourl = gui.Edit(self)
		self.l_description = gui.Label(self, "Description")
		self.tc_description = gui.Edit(self,multiline = True)
		
		self.b_create = gui.Button(self, "Create Post")
		self.b_cancel = gui.Button(self, "Cancel")
		
		self.__set_properties()
		self.__do_layout()
	
	def __set_properties(self):
		pass
	
	def __do_layout(self):
		s_audio = gui.VBox(border = (5,5,5,5), spacing = 2)
		s_audio.add(self.l_audio)
		s_audio.add(self.l_file)
		s_audio.add(self.b_browse)
		s_audio.add(self.l_audiourl)
		s_audio.add(self.tc_audiourl)
		s_audio.add(self.l_description)
		s_audio.add(self.tc_description)
		s_audio.add(self.b_create)
		s_audio.add(self.b_cancel)
		
		self.sizer = s_audio
		
	def OnOpen(self, evt):
		ret = gui.FileDialog.open()
		self.label_ret_value.text = "Return value: %s" %ret 

#if __name__ == '__main__':
#	app = gui.Application(Audio())
#	app.run()