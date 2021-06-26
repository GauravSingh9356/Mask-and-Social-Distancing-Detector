# Mask-and-Social-Distancing-Detector


<h2> Motivation<span style='font-size:100px;'>&#127775;</span></h2>	
<p>
Wearing Mask and Social distancing are the methods used to control the spread of contagious diseases. It implies that people physically distance themselves from one another, reducing close contact, and thereby reducing the spread of a contagious disease (such as the COVID-19 Disease).
Can AI be used to prevent the covid spread?. We have implemented Real time Mask Detection on image as well as on real time video. Also we have implemented Social Distancing Detection on images as well as real time videos. We have intregated both with common GUI made with tkinter.
</p>



<h1 align="left">
    Face Mask Detection
</h1>


Face Mask Detection with CNN model using tensorflow, OpenCV

## About

<ul>
  <li>Network used : Convolutional Network</li>
  <li>Framework used : Tensorflow</li>
  <li>API used : Keras</li>
  <li>Computer Vision library used : openCV</li>
</ul>

### Detecting face mask with accuracy with real time video

<img src="https://github.com/GauravSingh9356/Computer-Vision/blob/master/Face%20Mask%20Detection/ezgif.com-gif-maker%20(5).gif">



<h1 align="left">
    Social Distancing Detector
</h1>

A social distancing detector built with OpenCV using YOLO(COCO model) object detector


<p align="center">
  <img src="social_distancing_detector/res/social_distance_detector_spread.gif">
</p>

<p align="center">
   Social distancing is crucial to the prevention of the spread of disease.
</p>

## Features :gem:
* Object detection using the YOLO COCO model to detect only people in a video stream.
* Computes the pairwise distances between all detected people.
* Based on the computed distances, we determine whether social distancing rule is being violated or not.




## Usage :computer:
* Caution :bomb:\
For most accurate results, you should calibrate your camera through intrinsic/extrinsic parameters so that you can map pixels to measurable units.
An easier alternative(but less accurate) method would be to apply triangle similarity calibaration. Both of these methods can be used to map pixels to measurable units.\
If you do not want/cannot apply camera calibration, you can still utilize the social distancing detector but you'll have to rely strictly on the pixel distances, which won't necessarily be accurate.
For the sake of simplicity, this OpenCV Social Distancing detector implementation will rely on pixel distances. 
You can extend the implementation as you see fit though :wink:.

* YOLO COCO weights\
The weight file exceeds the github limits but can be download from <a href="https://pjreddie.com/media/files/yolov3.weights">here</a>.\
Add the weight file to the yolo-coco folder.

* GPU\
Provided you already have OpenCV installed with NVIDIA GPU support, all you need to do is set ```USE_GPU=True``` in your ```config.py``` file.

## Demo :movie_camera:
![raw-vid](social_distancing_detector/res/demo0.gif "Unprocessed video") ![processed-vid](social_distancing_detector/res/demo1.gif "Processed video")



- Email - gs935688@gmail.com :e-mail:
- Let's connect on <a href="https://www.linkedin.com/in/gauravsingh9356/">LinkedIn.</a> :pushpin:
