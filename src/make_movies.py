import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter
import matplotlib.image as mgimg
import os
import ffmpeg

folder = '04_May_2020_02_36_01'
path = "../results/"+ folder + "/figures"
save_path = "../results/"+ folder + "/video/"
#os.mkdir(os.path.join(os.getcwd(), save_path))

listing = os.listdir(os.path.join(os.getcwd(), path))

writer = FFMpegWriter(fps=15)
fig = plt.figure()
im = plt.imshow(np.zeros((20,20)))


with writer.saving(fig,'anim.mp4', 100):
    for file in listing:
        img = mgimg.imread(path + "/" + file)
        im.set_data(img)
        writer.grab_frame()


