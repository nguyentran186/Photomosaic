import cv2
import os
import numpy as np

directory = "D:\\NGUYEN\image\Bi"
os.chdir(directory)

source_im = open("D:\VScode\Python\ML\Photomosaic\source_im.txt",'w')

for file in os.listdir('.'):
    if file.endswith(".jpg"):
        frame = cv2.imread(file)
        mean_val = np.mean(frame, axis=(0,1))
        print(mean_val)
        #write to file
        source_im.write(file)
        source_im.write("  ")
        source_im.write(str(int(mean_val[0])))
        source_im.write("  ")
        source_im.write(str(int(mean_val[1])))
        source_im.write("  ")
        source_im.write(str(int(mean_val[2])))
        source_im.write("\n")
source_im.close()
print('Done')
