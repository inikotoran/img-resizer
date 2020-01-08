from PIL import Image
import sys

arguments = sys.argv
original_file = arguments[1]
new_file = arguments[2]
ratio = float(arguments[3])

original_image = Image.open(original_file)

height, width = original_image.size
new_height = int(height * ratio)
new_width = int(width * ratio)

new_image = original_image.resize((new_height, new_width))
new_image.save(new_file)
print(new_file + " with resolution " + str(new_height) + "x" + str(new_width) + " created.")
