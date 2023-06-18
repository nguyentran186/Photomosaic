import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pandas as pd

directory = "D:\VScode\Python\ML\Photomosaic"
out_directory = "D:\VScode\Python\ML\Photomosaic\sub image"
sub_directory = "D:\\NGUYEN\image\Bi"
os.chdir(directory)

image = cv2.imread("image.jpg")
height, width, rgb_num = image.shape
# cv2.imshow("Image", image)
# cv2.waitKey(0)

# ######IMPORT SOURCE IM
df = pd.read_csv("source_im.txt", delim_whitespace=True, engine="python")
df = df.to_numpy()
os.chdir(sub_directory)


def operate(num_col):
    num_cols = num_col
    cell_width = width / num_cols
    cell_height = cell_width
    num_rows = int(height / cell_height)

    os.chdir(sub_directory)
    img = Image.new(mode="RGBA", size=(width, height), color='white')
    draw = ImageDraw.Draw(img)
    for row in range(num_rows):
        for col in range(num_col):
            print(row, col)
            min_index = 0
            min_val = 255*2
            for i in range(0, len(df)):
                diff = abs(image[int(row*cell_height)][int(col*cell_width)][0] - df[i][1]) + abs(image[int(row*cell_height)]
                                                                                                 [int(col*cell_width)][1] - df[i][2]) + abs(image[int(row*cell_height)][int(col*cell_width)][2] - df[i][3])
                if min_val > diff:
                    min_index = i
                    min_val = diff
            sub_image = Image.open(df[min_index][0])
            sub_image = sub_image.resize((int(cell_height), int(cell_width)))
            img.paste(sub_image, (int(col*cell_width), int(row*cell_height)))
    os.chdir(out_directory)
    img.save('out_im{}.png'.format(num_col))


list = [70, 200]
for i in list:
    operate(i)
    print('Done', i)
