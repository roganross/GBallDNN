# GBallDNN

Deep Neural Network dedicated to the recognition of golf balls.

# Description

A DNN that is used to identify golf balls given images of them. It utilises a pretrained model (MobileNetV3) which has been trained further by collected training data. The current model outputs
a yes or no depending on whether a ball is detected or not. To be part of a raspberry-pi based system that attatches to a drone and can be utilised by golf courses/players to locate lost balls.

Includes python scripts to convert HEIC (iphone) images to JPG so they can be used as training data. There is also a preprocess script to label the data if sorted beforehand.

# Acknowledgements

Dan Landers (Idea)

ChatGPT (Coding Assistance)
