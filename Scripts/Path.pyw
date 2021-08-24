if Config["Image"]["URL_or_Path"] == "clipboard":
	File_Path = paste()

if not Config["Image"]["URL_or_Path"]:
	Config["Image"]["URL_or_Path"] = os.path.abspath(
		fd.askopenfilename(
			title = "Select image file",
			initialdir = "..",
			filetypes = [("Static Image Files", ".bmp .ico .jpeg .jpg .png .tiff .webp")],
			defaultextension = ".png"
			)
		)
	if Config["Image"]["URL_or_Path"] == os.getcwd():
		raise SystemExit("Folder selection aborted")

File_Path = Config["Image"]["URL_or_Path"]

#---#

if URL(File_Path):
	with get(File_Path, stream = True) as Site:
		if not Site.ok:
			raise SystemExit("\n{2}Warning{4}: {3}URL returns status code {0}{4} ({3}{1}{4}){3}\nImage will not be processed.{4}{5}".format(
				Site.status_code, Site.reason.title(), Styles.Yellow, Styles.Red, Styles.Reset, __BEL
				)
			)

#---#

Format = Config["Image"]["Output_Format"]

if not Format:
	Format = "PNG" # File_Path.split(".")[-1]

#---#

Path = os.path.abspath("Images/{0}.{1}".format(
	"_".join(
		["YTMVTG", str(time()).split(".")[0]]
		),
	Format.lower()
	)
)