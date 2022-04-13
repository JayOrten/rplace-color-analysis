import collections

import numpy as np
from PIL import Image
import glob

import image_comparison


def main():
    # Scan in all images
    image_list = []
    for filename in glob.glob("Images/images_single/*.png"):
        im = np.array(Image.open(filename).convert('RGB'))
        image_list.append(im)
        print(filename)

    # Run comparison functions on each consecutive pair of images, adding to dictionary
    dict_list = collections.Counter({})

    for i in range(1, len(image_list)):
        img1 = image_list[i - 1]
        img2 = image_list[i]

        color_dict = collections.Counter(image_comparison.compare_images(img1, img2))
        print("Colors changed in image " + str(i) + ": " + str(color_dict))
        dict_list = dict_list + color_dict
        print("Total colors: " + str(dict_list))

    print(dict_list)


if __name__ == '__main__':
    main()
