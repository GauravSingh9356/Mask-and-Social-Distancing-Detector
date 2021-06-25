# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:01:48 2021

@author: gs935
"""


from tkinter import *
from PIL import Image, ImageTk
import os
from mask_detection.mask_detector_img import detectImg
from mask_detection.mask_detector_vid import detectVid
from social_distancing_detector.detect import detectdis

def loadImgDetector():
   detectImg()
   
   
def loadVidDetector():
   detectVid()

def loadDisDetector():
   detectdis()


root = Tk()
root.title("Real Time Mask and Social Distancing Detection")
root.configure(bg="black")
root.geometry("900x900")


img = Image.open("img4.jpg")

img = img.resize((900, 500), Image.ANTIALIAS)
test = ImageTk.PhotoImage(img)


label = Label( image=test)
label.pack()

b1 =Button(root, text="Mask Image Detection",height=3,bg="#16FF01", relief="sunken", bd="3", command=loadImgDetector)
b1.pack(pady=15)


b2 =Button(root, text="Real Time Mask Video Detection",height=3,bg="#16FF01", relief="sunken", bd="3", command=loadVidDetector)
b2.pack(pady=15)

b3 =Button(root, text="Real Time Social Distancing Detection",height=3, bg="#16FF01",relief="sunken", bd="3", command=loadDisDetector)
b3.pack(pady=15)























root.mainloop()


