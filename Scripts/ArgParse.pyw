p = ap(
	"YTMVTG",
	description = "YouTube Music Videos Thumbnail Generator",
	add_help = False
)

p.add_argument(
	"-i", "--image",
	help = "URL / Absolute Path to Image",
	type = str,
	metavar = "\b",
	default = SUPPRESS
)

p.add_argument(
	"-ar", "--aspect_ratio",
	help = "Aspect ratio based on image height. (X:Y)",
	type = str,
	metavar = "\b",
	default = SUPPRESS
)

p.add_argument(
	"-h", "--help",
	help = "Shows this message",
	action = "help",
	default = SUPPRESS
)

#---#

args = p.parse_known_args()[0]

if len(os.sys.argv) > 1:
	try:
		Config["Image"]["URL_or_Path"] = args.image
	except AttributeError:
		raise SystemExit("No image URL or absolute path inputted, exiting")

	try:
		__AR = args.aspect_ratio
		__AR = [int(Character) for Character in __AR.split(":") if Character]
		if len(__AR) == 1 or len(__AR) > 2:
			raise SystemExit("Invalid aspect ratio! ({0})".format(":".join(__AR)))
		else:
			Config["Image"]["Aspect_Ratio"]["Width"] = __AR[0]
			Config["Image"]["Aspect_Ratio"]["Height"] = __AR[1]
	except AttributeError:
		__AR = 16, 9
		print("No aspect ratio given - processing with {0}:{1}".format(__AR[0], __AR[1]))
		Config["Image"]["Aspect_Ratio"]["Width"] = __AR[0]
		Config["Image"]["Aspect_Ratio"]["Height"] = __AR[1]