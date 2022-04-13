import numpy as np


def compare_images(img1, img2):

    # Find where indexes are different
    diff_indexes = np.where(img1 != img2)
    x_coord = diff_indexes[0]
    y_coord = diff_indexes[1]

    color_dict = {}

    # For each index where colors are different, check what color it is and add to color_dictionary to find total
    # colors changed from image 1 to image 2
    for i in range(0, len(x_coord), 3):
        x = x_coord[i]
        y = y_coord[i]

        color = img2[x][y]

        if (color == [255, 69, 0]).all():
            color_dict["ORANGE"] = color_dict.get("ORANGE", 0) + 1
        elif (color == [255, 168, 0]).all():
            color_dict["GOLD"] = color_dict.get("GOLD", 0) + 1
        elif (color == [255, 214, 53]).all():
            color_dict["YELLOW"] = color_dict.get("YELLOW", 0) + 1
        elif (color == [0, 163, 104]).all():
            color_dict["TEAL"] = color_dict.get("TEAL", 0) + 1
        elif (color == [126, 237, 86]).all():
            color_dict["LIGHT_GREEN"] = color_dict.get("LIGHT_GREEN", 0) + 1
        elif (color == [36, 80, 164]).all():
            color_dict["BLUE"] = color_dict.get("BLUE", 0) + 1
        elif (color == [54, 144, 234]).all():
            color_dict["BLUE2"] = color_dict.get("BLUE2", 0) + 1
        elif (color == [81, 233, 244]).all():
            color_dict["LIGHT_BLUE"] = color_dict.get("LIGHT_BLUE", 0) + 1
        elif (color == [129, 30, 159]).all():
            color_dict["PURPLE"] = color_dict.get("PURPLE", 0) + 1
        elif (color == [180, 74, 192]).all():
            color_dict["LIGHT_PURPLE"] = color_dict.get("LIGHT_PURPLE", 0) + 1
        elif (color == [255, 153, 170]).all():
            color_dict["PINK"] = color_dict.get("PINK", 0) + 1
        elif (color == [156, 105, 38]).all():
            color_dict["BROWN"] = color_dict.get("BROWN", 0) + 1
        elif (color == [0, 0, 0]).all():
            color_dict["BLACK"] = color_dict.get("BLACK", 0) + 1
        elif (color == [137, 141, 144]).all():
            color_dict["GREY"] = color_dict.get("GREY", 0) + 1
        elif (color == [212, 215, 217]).all():
            color_dict["LIGHT_GREY"] = color_dict.get("LIGHT_GREY", 0) + 1
        elif (color == [255, 255, 255]).all():
            color_dict["WHITE"] = color_dict.get("WHITE", 0) + 1

    return color_dict
