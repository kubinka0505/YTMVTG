"""YouTube Music Videos Thumbnail Maker"""

import os
from time import time
from PIL import Image
from json import loads
from requests import get
os.chdir(os.path.abspath(os.path.dirname(__file__)))

#--------------------------------#

__author__		= "kubinka0505"
__copyright__	= __author__
__credits__		= __author__
__version__		= "1.0"
__date__		= "16.03.2021"
__status__		= "Mature"
__license__		= "GPL V3"

#--------------------------------#

Config = loads(open("Config.json", encoding = "utf-8").read())

Name = Config["Output"]["Name"]
Format = Config["Output"]["Format"]
File_Path = Config["URL / Path"]

#--------------------------------#

try:
	Picture = Image.open(File_Path).convert("RGB")
except (AttributeError, OSError):
	Picture = Image.open(get(File_Path, stream = True).raw)

if not Name:
	Name = ".".join(File_Path.split("/")[-1].split(os.sep)[-1].split(".")[:-1])
if not Format:
	Format = "PNG" # File_Path.split(".")[-1]

Name += "_" if Name else "" + "_".join(["YTMLTM", str(time()).split(".")[0]])
Format = Format.lower()

Width, Height = Picture.size[0] * Config["Aspect_Ratio"]["Width"] // Config["Aspect_Ratio"]["Height"], Picture.size[1]

Background_Color = Picture.resize((1,1), Config["Resizing_Algorithm"]).getpixel((0,0))
Background = Image.new(size = (Width, Height), mode = Picture.mode, color = Background_Color)
Background.paste(Picture, ((Background.size[0] - Picture.size[0]) // 2, (Background.size[1] - Picture.size[1]) // 2))
Background.save("Images/{0}.{1}".format(Name, Format), quality = 100)