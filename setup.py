import sys

NAME="opentumblr-client"
VERSION = "0.0.2"
DESCRIPTION = "Cliente de escritorio para tumblr"
AUTHOR = "Jair Gaxiola"
AUTHOR_EMAIL = "jyr.gaxiola@gmail.com"
URL = "http://opentumblr.tumblr.com"
LICENSE = "MIT LICENSE"

if sys.platform == "darwin":
	"""
	This is a setup.py script generated by py2applet

	Usage:
	    python setup.py py2app --iconfile opentumblr/images/opentumblr.icns
	"""

	from setuptools import setup

	APP = ['opentumblr/opentumblr-client.py']
	DATA_FILES = []
	OPTIONS = {'argv_emulation': True}

	setup(
		name=NAME,
		version=VERSION,
		description=DESCRIPTION,
	   	author=AUTHOR,
     	author_email=AUTHOR_EMAIL,
      	url=URL,
      	license=LICENSE,
    	app=APP,
		packages=['poster', 'simplejson'],
	    data_files=DATA_FILES,
	    options={'py2app': OPTIONS},
	    setup_requires=['py2app'],
	)
	
else:
	if sys.platform == "win32":
		from distutils.core import setup
		import py2exe
		
		setup(
			console=['opentumblr/opentumblr-client.py']
		)
	else:
		import os
		from distutils.core import setup
		#from distutils.sysconfig import get_python_lib

		ipath_docs = '/usr/share/doc/opentumblr/'
		ipath_images = '/usr/share/pixmaps/opentumblr/'
		ipath_dashboard = ipath_images+'dashboard/'
		ipath_desktop = '/usr/share/applications/'

		path_images = os.getcwd() + '/opentumblr/images/'
		image_files = [path_images+'audio.png',path_images+'chat.png',path_images+'link.png',path_images+'photo.png',path_images+'quote.png',path_images+'text.png',path_images+'video.png']
		doc_files =['AUTHORS','INSTALL','LICENSE','README','THANKS']
		icon_files = ['opentumblr/images/opentumblr.png','opentumblr/images/opentumblr.xpm']

		if not os.path.isdir(ipath_docs):
			os.mkdir(ipath_docs)

		if not os.path.isdir(ipath_images):
			os.mkdir(ipath_images)
			os.mkdir(ipath_dashboard)

		setup(
			name=NAME,
			version=VERSION,
	      	description=DESCRIPTION,
	      	author=AUTHOR,
	      	author_email=AUTHOR_EMAIL,
	      	url=URL,
	      	license=LICENSE,
	      	scripts=['opentumblr/opentumblr-client.py'],
	      	packages=['opentumblr'],
	      	data_files=[('/usr/share/pixmaps/', icon_files),(ipath_dashboard, image_files),(ipath_docs, doc_files),(ipath_desktop,['opentumblr.desktop'])]
		)