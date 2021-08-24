"""YouTube Music Videos Thumbnail Generator"""

import os
from time import time
from json import loads
from requests import get
from random import randint
from clipboard import paste
from datetime import timedelta
from urllib.parse import urlparse
from PIL import Image, ImageEnhance
from tkinter import Tk, filedialog as fd
from argparse import ArgumentParser as ap
SUPPRESS = __import__("argparse").SUPPRESS

#-------------------------#

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= __author__
__version__		= "1.3"
__date__		= "24.08.2021"
__status__		= "Mature"
__license__		= "GPL V3"

#-------------------------#

root = Tk()
root.withdraw()
os.chdir(os.path.abspath(os.path.dirname(__file__)))

#-------------------------#

Files = ["Utils", "ArgParse", "Path", "Processing"]
Config = loads(open("Config.json", encoding = "utf-8").read())

for File in Files:
	__STA_TIME = __import__("time").time()
	exec(open("./Scripts/{0}.pyw".format(File), encoding = "utf-8").read())

__END_TIME = str(timedelta(seconds = time() - __STA_TIME))[2:-3]
print('\n{4}Done!{8} ({5}{0}{8})\nImage Name: {6}"{7}{1}{8}{6}"{8} ({2}){3}'.format(
	__END_TIME, Path.split(os.sep)[-1], File_Size(os.path.getsize(Path)), __BEL,
	Styles.Green, Styles.LightBlue, Styles.Cyan, Styles.Underscore, Styles.Reset
	)
)