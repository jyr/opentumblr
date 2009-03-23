import os
from distutils.core import setup
from distutils.sysconfig import get_python_lib

path_images = os.getcwd()+'/opentumblr/images/'
image_files = [path_images+'audio.png',path_images+'chat.png',path_images+'link.png',path_images+'photo.png',path_images+'quote.png',path_images+'text.png',path_images+'video.png']
doc_files =['AUTHORS','INSTALL','LICENSE','PKG-INFO','README']

install_dir = get_python_lib() + '/opentumblr/images/'

setup(name="opentumblr",
      version="BETA",
      description="Cliente de escritorio para tumblr",
      author="Jair Gaxiola",
      author_email="jyr.gaxiola@gmail.com",
      url="http://github.com/jyr/opentumblr",
      license="MIT LICENSE",
      scripts=['opentumblr/login.py'],
      packages=['opentumblr'],
      py_modules=['tumblr'],
      data_files=[(install_dir, image_files)]
)
