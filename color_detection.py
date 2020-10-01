# Color detection

### Libraries

from PIL import Image
import os, os.path
import webcolors

# Uses rgb value to find nearest color 
# Source of this function:
# https://stackoverflow.com/questions/9694165/convert-rgb-color-to-english-color-name-like-green-with-python
def get_nearest_color(rgb):
  colors = {}
  for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
    r_c, g_c, b_c = webcolors.hex_to_rgb(key)
    rd = (r_c - rgb[0]) ** 2
    gd = (g_c - rgb[1]) ** 2
    bd = (b_c - rgb[2]) ** 2
    colors[(rd + gd + bd)] = name
  return colors[min(colors.keys())]

# Creates a dictionary with filename and color of image
def get_colors(path)
  colors = {}
  for f in os.listdir(path):
    im = Image.open(os.path.join(path,f))
    _, rgb = max(im.getcolors(im.size[0]*im.size[1]))
    if (len(rgb)==4):
      # It is rgba
      rgb = rgb[:-1]
    color = get_nearest_color(rgb)
    colors.update({f:color})
  return colors

# Run example
path = "images_color/"
dict_colors = get_colors(path)
print("Result: ")
print(dict_colors)
