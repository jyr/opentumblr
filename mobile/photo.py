import ppygui as gui

class Photo(gui.CeFrame):
	def __init__(self):
		gui.CeFrame.__init__(self, title="Opentumblr CE")
		
		self.l_addphoto = gui.Label(self, "Upload a Photo", align = "center")
		self.l_photo = gui.Label(self, "Photo")
		self.b_browse = gui.Button(self, "Open a file", action = self.OnOpen)
		self.l_supports = gui.Label(self, "Supports JPEG, GIF, PNG and BMP. mAX PHOTO SIZE IS 10mb.")
		self.l_photourl = gui.Label(self, "Photo Url")
		self.tc_photourl = gui.Edit(self)
		self.l_caption = gui.Label(self, "Caption")
		self.tc_caption = gui.Edit(self,multiline = True)
		self.l_photolink = gui.Label(self, "Photo links to the URL")
		self.tc_photolink = gui.Edit(self)
		
		self.b_create = gui.Button(self, "Create Post")
		self.b_cancel = gui.Button(self, "Cancel")
		
		self.__set_properties()
		self.__do_layout()
	
	def __set_properties(self):
		pass
	
	def __do_layout(self):
		s_photo = gui.VBox(border = (5,5,5,5), spacing = 2)
		s_photo.add(self.l_addphoto)
		s_photo.add(self.l_photo)
		s_photo.add(self.b_browse)
		s_photo.add(self.l_supports)
		s_photo.add(self.l_photourl)
		s_photo.add(self.tc_photourl)
		s_photo.add(self.l_caption)
		s_photo.add(self.tc_caption)
		s_photo.add(self.l_photolink)
		s_photo.add(self.tc_photolink)
		s_photo.add(self.b_create)
		s_photo.add(self.b_cancel)
		
		self.sizer = s_photo
		
	def OnOpen(self, evt):
		ret = gui.FileDialog.open()
		self.label_ret_value.text = "Return value: %s" %ret 

if __name__ == '__main__':
	app = gui.Application(Photo())
	app.run()
