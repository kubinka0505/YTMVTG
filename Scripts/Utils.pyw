Filters = [Image.NEAREST, Image.BOX, Image.BILINEAR, Image.HAMMING, Image.BICUBIC, Image.LANCZOS]

#---#

_COLP = Config["Settings"]["Colored_Prints"]
__BEL = "" if Config["Settings"]["Sound"] else ""

if not bool(Config["Image"]["Resizing_Algorithm"]):
	Config["Image"]["Resizing_Algorithm"] = randint(0, len(Filters) - 1)

#---#

def URL(URL: str) -> bool:
	"""Checks if string is URL"""
	try:
		Result = urlparse(URL)
		return all([Result.scheme, Result.netloc])
	except ValueError:
		return False

def Grayscale(Image_OBJ: Image) -> bool:
	"""Checks if image can be converted
	into grayscale color palette"""
	Picture = Image_OBJ.convert("RGB")
	Width, Height = Picture.size
	for X in range(Width):
		for Y in range(Height):
			R, G, B = Picture.getpixel((X,Y))
			if R != G != B: return False
	return True

def File_Size(Bytes: float) -> str:
	"""Returns human-readable file size"""
	for Unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
		if Bytes < 1024.: break
		Bytes /= 1024.
	return "{0} {1}".format(round(Bytes, 2), Unit)

class Styles():
	"""Colored Prints."""
	Red			= "\033[31m" if _COLP else ""
	Green		= "\033[32m" if _COLP else ""
	Yellow		= "\033[33m" if _COLP else ""
	LightBlue	= "\033[36m" if _COLP else ""
	DarkGray	= "\033[90m" if _COLP else ""
	LightRed	= "\033[91m" if _COLP else ""
	LightGreen	= "\033[92m" if _COLP else ""
	Cyan		= "\033[96m" if _COLP else ""
	Underscore	= "\033[4m" if _COLP else ""
	Reset		= "\033[0m" if _COLP else ""

#---#

os.system("")