import collections

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import glob

import image_comparison


def main():
    image_list = []
    for filename in glob.glob("Images/images_single/*.png"):
        im = np.array(Image.open(filename).convert('RGB'))
        image_list.append(im)
        print(filename)

    dict_list = collections.Counter({})

    for i in range(1, len(image_list)):
        img1 = image_list[i - 1]
        img2 = image_list[i]

        color_dict = collections.Counter(image_comparison.compare_images(img1, img2))
        print("Colors changed in image " + str(i) + ": " + str(color_dict))
        dict_list = dict_list + color_dict
        print("Total colors: " + str(dict_list))

    print(dict_list)


# Counter({'BLACK': 3511131, 'WHITE': 2126074, 'ORANGE': 1705732, 'BLUE': 1386757, 'YELLOW': 960390, 'LIGHT_BLUE':
# 659202, 'TEAL': 644300, 'PINK': 588271, 'LIGHT_GREEN': 486561, 'PURPLE': 460484, 'GOLD': 434596, 'BLUE2': 408605,
# 'GREY': 338799, 'BROWN': 294177, 'LIGHT_GREY': 285796, 'LIGHT_PURPLE': 179175})

"""
        img1 = np.array(Image.open('Images/images_single/0-1648822500.png').convert('RGB'))
        img2 = np.array(Image.open('Images/images_single/0-1648822512.png').convert('RGB'))
        plt.figure(figsize=(10, 10))
        plt.imshow(img1)
        plt.imshow(img2)
        plt.show()
"""

if __name__ == '__main__':
    main()
