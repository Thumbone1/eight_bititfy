from skimage import io
from pyxelate import Pyx


image = io.imread("your_image.jpg")
downsample_by = 14
palette = 7
pyx = Pyx(factor=downsample_by, palette=palette)
pyx.fit(image)
new_image = pyx.transform(image)
io.imsave("pixelfied_your_image.png", new_image)
