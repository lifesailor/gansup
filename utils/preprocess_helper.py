import numpy as np

# crop center
def crop_center(image, width=256, height=256):
    return image[256 - width // 2:256 + width // 2,
                 256 - height // 2:256 + height // 2]

# binarize
def binarize(image):
    bin_pixel1 = image > 1120
    bin_pixel2 = image < 1500
    bin_pixel = bin_pixel1 & bin_pixel2
    return np.where(image, bin_pixel, 0)
