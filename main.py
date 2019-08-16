import numpy as np
import cv2
from PIL import ImageGrab
import time

while(True):
    img = ImageGrab.grab(bbox=(100,10,400,780)) #bbox specifies specific region (bbox= x,y,width,height)
    img_np = np.array(img)
    print(img_np)
    time.sleep(4)
