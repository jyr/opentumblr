import ppygui as gui

from text import Text
from photo import Photo
from quote import Quote
from link import Link
from chat import Chat
from audio import Audio
from video import Video

class Dashboard(gui.CeFrame):
	def __init__(self, api):
		self.api = api
		gui.CeFrame.__init__(self, title = "Opentumblr CE")
		
		self.l_dashboard = gui.Label(self, "Dashboard", align = "center")
		self.bmap_text = gui.Button(self, "Text")
		self.bmap_photo = gui.Button(self, "Photo")
		self.bmap_quote = gui.Button(self, "Quote")
		self.bmap_link = gui.Button(self, "Link")
		self.bmap_chat = gui.Button(self, "Chat")
		self.bmap_audio = gui.Button(self, "Audio")
		self.bmap_video = gui.Button(self, "Video")
		
		self.b_logout = gui.Button(self, "Logout")
		
		self.bmap_text.bind(clicked = self.OnText)
		self.bmap_photo.bind(clicked = self.OnPhoto)
		self.bmap_quote.bind(clicked = self.OnQuote)
		self.bmap_link.bind(clicked = self.OnLink)
		self.bmap_chat.bind(clicked = self.OnChat)
		self.bmap_audio.bind(clicked = self.OnAudio)
		self.bmap_video.bind(clicked = self.OnVideo)
		
		self.b_logout.bind(clicked = self.OnClose)
		
		self.__set_properties()
		self.__do_layout()
	
	def __set_properties(self):
		pass
	
	def __do_layout(self):
		s_dashboard = gui.VBox(border = (5,5,5,5), spacing = 5)
		s_dashboard.add(self.l_dashboard)
		s_dashboard.add(self.bmap_text)
		s_dashboard.add(self.bmap_photo)
		s_dashboard.add(self.bmap_quote)
		s_dashboard.add(self.bmap_link)
		s_dashboard.add(self.bmap_chat)
		s_dashboard.add(self.bmap_audio)
		s_dashboard.add(self.bmap_video)
		s_dashboard.add(self.b_logout)
		
		self.sizer = s_dashboard
	
	def OnText(self, evt):
		Text(self.api)
	
	def OnPhoto(self, evt):
		pass
	
	def OnQuote(self, evt):
		Quote(self.api)
	
	def OnLink(self, evt):
		Link(self.api)
	
	def OnChat(self, evt):
		Chat(self.api)
	
	def OnAudio(self, evt):
		pass
	
	def OnVideo(self, evt):
		Video(self.api)
	
	def OnClose(self, evt):
		self.close()

#if __name__ == '__main__':
#	app = gui.Application(Dashboard())	
#	app.run()