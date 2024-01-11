import os
from PIL import Image, ImageOps

path = r"your/minetest/game/mods/path/"

paths = [f"{path}beds", f"{path}binoculars", f"{path}boats", f"{path}bones", f"{path}bucket", f"{path}butterflies", f"{path}carts", f"{path}creative", f"{path}default", f"{path}doors", f"{path}dye", f"{path}farming", f"{path}fire", f"{path}fireflies", f"{path}flowers", f"{path}map", f"{path}player_api", f"{path}screwdriver", f"{path}sfinv", f"{path}stairs", f"{path}tnt", f"{path}vessels", f"{path}wool", f"{path}xpanes"]
files = []
for p in paths :
    for f in os.listdir(p + r"\textures") :# if os.path.isfile(f)
        files.append([f, p + r"\textures"])
for f in files :
    img = Image.open(f[1] + "\\" + f[0])
    r = ImageOps.grayscale(img) 
    r.save(r"your/NoColorStory/path/{0}".format(f[0]))