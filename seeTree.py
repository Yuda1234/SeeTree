import pandas as pd
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import csv

path_to_img = "C:\\Users\\yaakovk\\Downloads\\8-bit-256-x-256-Grayscale-Lena-Image.png"
# path = "C:\\Users\\yaakovk\\Downloads\\building-png-skyview-floorplans-luxury-condominium-rentals-with-3.png"



# 1-2 import image, Write a short python script to extract the image  histogram

def import_image():
    img = Image.open(path_to_img)
    img.show()
    img = cv2.imread(path_to_img, 0)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()
    list = sorted(plt.hist(img.ravel(), bins=256)[0], reverse=True)
    print(list)


# 3: Save the tonal values  into a CSV
def save_to_scv():
    img2 = cv2.imread(path_to_img)
    hist_sim = pd.DataFrame(cv2.calcHist(img2, [1], None, [256], [0, 256]))
    bin = pd.DataFrame(plt.hist(img2.ravel(), bins=256)[0])
    hist_sim.to_csv('histogram.csv', index=False)
    bin.to_csv('histogram.csv', index=False)


# 4: Sort the values of the tonal highest to low
def sort_values():
    reader = csv.reader(open("histogram.csv"), delimiter=";")
    sorted_list = sorted(reader, key=lambda x: float(x[0]), reverse=True)
    for each_line in sorted_list:
        print(each_line)



