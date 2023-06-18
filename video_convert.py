import os
import cv2
import numpy as np
from PIL import Image

directory = "D:\VScode\Python\ML\Photomosaic\sub image"
os.chdir(directory)

num_of_image = 15


def generate_video():
    image_folder = '.'
    video_name = 'Photomosaic.avi'
    os.chdir(directory)

    linlist = [1, 2, 3, 5, 7, 10, 15, 20, 25, 30, 40, 55, 70, 100, 200]

    images = [img for img in os.listdir(image_folder)]
    images = ["out_im{}.png".format(int(index)) for index in linlist]

    frame = cv2.imread(os.path.join(image_folder, images[0]))

    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    for i in range(0, 5):
        video.write(cv2.imread("D:\VScode\Python\ML\Photomosaic\image.jpg"))

    cv2.destroyAllWindows()
    video.release()


generate_video()
