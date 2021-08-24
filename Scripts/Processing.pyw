try:
	Picture = Image.open(File_Path)
except (AttributeError, OSError):
	Picture = Image.open(get(File_Path, stream = True).raw)
Picture = Picture.convert("RGBA")

#---#

print("Processing...")

Width = Picture.size[0] * Config["Image"]["Aspect_Ratio"]["Width"] // Config["Image"]["Aspect_Ratio"]["Height"]
Height = Picture.size[1]

#---#

if Config["Settings"]["Processing_Mode"] == 1:
	Background_Color = Picture.resize((1, 1), Config["Image"]["Resizing_Algorithm"])
	Background_Color = ImageEnhance.Brightness(Background_Color).enhance(Config["Image"]["Background_Brightness_Percentage"] / 100)
	Background_Color = Background_Color.getpixel((0, 0))
	#---#
	Background = Image.new("RGBA", (Width, Height), Background_Color)
	Background.paste(
		Picture, (
			(Background.size[0] - Picture.size[0]) // 2,
			(Background.size[1] - Picture.size[1]) // 2
			),
		Picture
		)
	#---#
	if Grayscale(Background):
		print("{0}Converting image to grayscale colormap...{1}".format(
			Styles.DarkGray, Styles.Reset
			)
		)
		Background = Background.convert("L")
	else:
		Background = Background.convert("P")
	Background.save(Path, quality = 100)
else:
	Background_Comparison = Image.new(Picture.mode, (Width, Height * len(Filters)))
	Y = 0
	for Algorithm in Filters:
		Background_Color = Picture.resize((1, 1), Algorithm)
		Background_Color = ImageEnhance.Brightness(Background_Color).enhance(Config["Image"]["Background_Brightness_Percentage"] / 100)
		Background_Color = Background_Color.getpixel((0, 0))
		#---#
		Background = Image.new(Picture.mode, (Width, Height), Background_Color)
		Background.paste(Picture, (
			(Background.size[0] - Picture.size[0]) // 2,
			(Background.size[1] - Picture.size[1]) // 2
			)
		)
		Background_Comparison.paste(Background, (0, Y))
		#---#
		Y += Height
	Background_Comparison.show()