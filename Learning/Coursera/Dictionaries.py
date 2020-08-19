wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for cloth, colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color, cloth))