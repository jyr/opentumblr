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

setup(name="opentumblr",
      version="0.0.1",
      description="Cliente de escritorio para tumblr",
      author="Jair Gaxiola",
      author_email="jyr.gaxiola@gmail.com",
      url="http://github.com/jyr/opentumblr",
      license="MIT LICENSE",
      scripts=['opentumblr/login.py'],
      packages=['opentumblr'],
      py_modules=['tumblr'],
      data_files=[('/usr/share/pixmaps/', icon_files),(ipath_dashboard, image_files),(ipath_docs, doc_files),(ipath_desktop,['opentumblr.desktop'])]
)
