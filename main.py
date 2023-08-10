from skimage import io
from pyxelate import Pyx, Pal

#load image with 'skimage.io.imread()'

image = io.imread("adult-elephant-with-ivory-cartoon-style_1308-53397.jpg")  
downsample_by = 14  # new image will be 1/14th of the original in size
palette = 7  # find 7 colors

#1) Instantiate Pyx transformer

pyx = Pyx(factor=downsample_by, palette=palette)

#2) fit an image, allow Pyxelate to learn the color palette

pyx.fit(image)

#3) transform image to pixel art using the learned color palette

new_image = pyx.transform(image)
# save new image with 'skimage.io.imsave()'
io.imsave("pixel_adult-elephant-with-ivory-cartoon-style_1308-53397.png", new_image)