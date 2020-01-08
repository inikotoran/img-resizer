from PIL import Image

image = Image.open('passport.jpg')

newImage = image.resize((2304,1728))

newImage.save('passport-niko.jpg')