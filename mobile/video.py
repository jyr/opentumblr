import ppygui as gui

from tumblr import Api

class Video(gui.CeFrame):
	def __init__(self, api):
		self.api = api
		gui.CeFrame.__init__(self, title="Opentumblr CE")
		
		self.l_video = gui.Label(self, "Add a Video", align = "center")
		self.l_embed = gui.Label(self, "Embed a Video")
		self.tc_embed = gui.Edit(self)
		self.l_caption = gui.Label(self, "Caption (optional)")
		self.tc_caption = gui.Edit(self,multiline = True)
		
		self.b_create = gui.Button(self, "Create Post")
		self.b_cancel = gui.Button(self, "Cancel")
		
		self.b_create.bind(clicked = self.OnCreateVideo)
		self.b_cancel.bind(clicked = self.OnCancel)
		
		self.__set_properties()
		self.__do_layout()
	
	def __set_properties(self):
		pass
	
	def __do_layout(self):
		s_video = gui.VBox(border = (5,5,5,5), spacing = 2)
		s_video.add(self.l_video)
		s_video.add(self.l_embed)
		s_video.add(self.tc_embed)
		s_video.add(self.l_caption)
		s_video.add(self.tc_caption)
		s_video.add(self.b_create)
		s_video.add(self.b_cancel)
		
		self.sizer = s_video
	
	def OnCreateVideo(self, evt):
		self.embed = self.tc_embed.get_text()
		self.caption = self.tc_caption.get_text()
		
		if self.embed:
			self.api = Api(self.api.name, self.api.email, self.api.password)
			try:
				self.post = self.api.write_video(self.embed, self.caption)
			except:
				print "Posteado en el primario"
			self.close()
		else:
			gui.Message.ok(title = 'Warning', caption = 'Embed a video is required')
	
	def OnCancel(self, evt):
		self.close()

#if __name__ == '__main__':
#	app = gui.Application(Video())
#	app.run()