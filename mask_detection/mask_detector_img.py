# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:56:23 2021

@author: gs9356
"""
import cv2 as cv
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from gtts import gTTS

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def sendEmail(email):
    fromaddr = "gauravsingh9356me@gmail.com"
    toaddr = email
       
    # instance of MIMEMultipart
    msg = MIMEMultipart()
      
    # storing the senders email address  
    msg['From'] = fromaddr
      
    # storing the receivers email address 
    msg['To'] = toaddr
      
    # storing the subject 
    msg['Subject'] = "ALERT MESSAGE"
      
    # string to store the body of the mail
    body = "Someone with no mask is found!"
      
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
      
    # open the file to be sent 
    filename = "final.jpg"
    attachment = open("./mask_detection/final.jpg", "rb")
      
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
      
    # To change the payload into encoded form
    p.set_payload((attachment).read())
      
    # encode into base64
    encoders.encode_base64(p)
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
      
    # attach the instance 'p' to instance 'msg'
    msg.attach(p)
      
    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)
      
    # start TLS for security
    s.starttls()
      
    # Authentication
    s.login(fromaddr, "#gauravsingh9356me12345")
      
    # Converts the Multipart msg into a string
    text = msg.as_string()
      
    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
      
    # terminating the session
    s.quit()





def speak(audio):
    language = 'en'
    myobj = gTTS(text=audio, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")

def detectImg():
    img_width, img_height = 200, 200
    
    model = load_model(os.path.join("./mask_detection/predictor.tf"), "saved_model.pb")
    
    
    face_cascade = cv.CascadeClassifier("./mask_detection/haarcascade_frontalface_default.xml")
    
    
    img_count_full = 0
    
    font = cv.FONT_HERSHEY_SIMPLEX
    org = (1, 15)
    class_label = " "
    fontScale = 1
    color = (0, 255, 0)
    thickness = 2
    pred = 0
    
    
    img_count_full += 1
    
    
    img = cv.imread("./mask_detection/me2.jpeg", 1)
    
    scale = 50
    width = int(img.shape[1]*scale/100)
    height = int(img.shape[0]*scale / 100)
    dim = (width, height)
    
    color_img = cv.resize(img, dim, interpolation=cv.INTER_AREA)
    
    gray_img = cv.cvtColor(color_img, cv.COLOR_BGR2GRAY)
    
    
    faces = face_cascade.detectMultiScale(gray_img, 1.2, 2)
    
    img_count = 0
    for (x, y, w, h) in faces:
        org = (x+5, y+30)
        img_count += 1
        color_face = color_img[y:y+h, x:x+w]
        cv.imwrite("./mask_detection/detected_faces/%d%dface.jpg" %
                   (img_count_full, img_count), color_face)
        img = image.load_img("./mask_detection/detected_faces/%d%dface.jpg" %
                             (img_count_full, img_count), target_size=(img_width, img_height))
    
        img = image.img_to_array(img)/255
        img = np.expand_dims(img, axis=0)
        pred_prob = model.predict(img)
    
        pred = np.argmax(pred_prob)
    
        if(pred == 0):
            print("User with mask - prediction = ", pred_prob[0][0])
            class_label = "Mask"
            cv.imwrite("./mask_detection/detected_faces/with_mask/%d%dface.jpg" %
                       (img_count_full, img_count), color_face)
            color = (0, 255, 0)
            pred = pred_prob[0][0]
            speak("Person is masked!")
    
        else:
            print("User without mask - prediction = ", pred_prob[0][1])
            class_label = "Without Mask"
            cv.imwrite("./mask_detection/detected_faces/without_mask/%d%dface.jpg" %
                       (img_count_full, img_count), color_face)
            color = (0, 0, 255)
            pred = pred_prob[0][1]
            speak("Person is not masked!")
    
            sendEmail("gs935688@gmail.com")
    
        cv.rectangle(color_img, (x, y), (x+w+30, y+h), color, 3)
        cv.putText(color_img, class_label+" "+str(pred), org,
                   font, fontScale, color, thickness, cv.LINE_AA)
    
        cv.imshow("LIVE FACE MASK DETECTION", color_img)
        cv.imwrite("./mask_detection/Final.jpg", color_img)
        if(cv.waitKey(0) & 0xFF == ord('q')):
            break
    
    
    
    cv.destroyAllWindows()
