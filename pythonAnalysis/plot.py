# Counter({'BLACK': 3511131, 'WHITE': 2126074, 'ORANGE': 1705732, 'BLUE': 1386757, 'YELLOW': 960390, 'LIGHT_BLUE':
# 659202, 'TEAL': 644300, 'PINK': 588271, 'LIGHT_GREEN': 486561, 'PURPLE': 460484, 'GOLD': 434596, 'BLUE2': 408605,
# 'GREY': 338799, 'BROWN': 294177, 'LIGHT_GREY': 285796, 'LIGHT_PURPLE': 179175})

import matplotlib.pyplot as plt
import pandas as pd


def plot():
    def add_value_label(x_list, y_list):
        for i in range(1, len(x_list) + 1):
            plt.text(i, y_list[i - 1], y_list[i - 1])

    # Data
    df = pd.DataFrame({'Color': ['Black', 'White', 'Orange', 'Blue', 'Yellow', 'Light Blue', 'Teal', 'Pink',
                                 'Light Green', 'Purple', 'Gold', 'Blue 2', 'Grey', 'Brown', 'Light Grey',
                                 'Light Purple'],
                       'Value': [3511131, 2126074, 1705732, 1386757, 960390, 659202, 644300, 588271,
                                 486561, 460484, 434596, 408605, 338799, 294177, 285796, 179175]})

    # Set up colors
    colors = [(0, 0, 0), (255, 255, 255), (255, 69, 0), (54, 144, 234),
              (255, 214, 53), (81, 233, 244), (0, 163, 104), (255, 153, 170),
              (126, 237, 86), (129, 30, 159), (255, 168, 0), (54, 144, 234),
              (137, 141, 144), (156, 105, 38), (212, 215, 217), (180, 74, 192)]

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.
    for i in range(len(colors)):
        r, g, b = colors[i]
        colors[i] = (r / 255., g / 255., b / 255.)

    # Plot

    plt.figure(figsize=(10, 6))

    bars = plt.barh(y=df.Color, width=df.Value, color=colors, edgecolor="grey")

    # Remove ticks
    ax = plt.gca()
    ax.axes.yaxis.set_visible(False)
    ax.axes.xaxis.set_visible(False)

    # Remove border
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Add labels
    ax.bar_label(bars, padding=8, fmt="%d")

    # Add text
    ax.text(1180390, 15, 'Total pixels added by color', fontsize=30)
    ax.text(980000, 13, 'in first expansion of r/place 2022', fontsize=30)

    ax.text(960390, -2, 'Total pixels added: 14,470,050', fontsize=20, fontweight='bold')

    ax.text(4000, -3, 'Data: https://place.thatguyalex.com/')

    # Adjust margins
    plt.subplots_adjust(left=.01, right=0.9, top=0.9, bottom=0.1)

    # Show plot
    # plt.show()

    # Save plot
    plt.savefig('rplace_colors.png')


if __name__ == '__main__':
    plot()
