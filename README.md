# Zero Shot Image Classifier

## Introduction
Zero Shot Image Classifier is a tiny web app I built with Flask and Huggingface that allows anyone to instantly classify images dynamically based on their own set of labels. 
I built this to learn about computer vision and also to see how robust CLIP is at classifying arbitrary images with arbitrary labels. A good friend of mine demo'd something like this to me a while back before CLIP was cool and it blew my mind, and I wanted to see if I could build something quickly that worked! 
This app is powered by CLIP, can be run locally, and is super straightforward to run. 

## Features
- **Dynamic Label Input**: Users can specify their own set of class labels for image classification. Please make sure they are separated by commas. 
- **Image Upload**: Easy upload interface for users to provide images for classification. By easy I mean bare bones.
- **Immediate Results**: Classification results are displayed instantly on the same page after image submission. You won't be waiting long if you have a reasonable CPU on your machine. For context I am built and ran this on a 2020 M1 Macbook Pro with 16 GB of Memory. 

## Installation

### Prerequisites
- Python 3.x

### Setup
1. **Clone the Repository and install packages. I recommend doing this inside of a virtual environment**
   ```bash
   git clone https://github.com/ezishiri/Zero-Shot-Image-Classifier.git
   cd zero-shot-image-classifier
   python3 -m venv env
   source bin/activate/env
   pip install flask torch transformers Pillow
   
Run the Application
 ```bash
  python3 app.py
```

Access the web application at http://127.0.0.1:5000/.

The screenshots below demonstrate the CLIP can accurately distinguish between extremely similar categories, as it is able to classify the example image as 'glossier lip gloss' among the options lip balm, lipstick, lip gloss, lip liner, and glossier lip gloss among others. 

All credit to OpenAI, and Isaac who opened me up to the cool things you can do with AI!  


<img width="979" alt="Screenshot 2023-11-27 at 9 19 50 PM" src="https://github.com/ezishiri/Zero-Shot-Image-Classifier/assets/40304716/c024fc47-803b-46e0-a4c5-013596f7dda9">
<img width="995" alt="Screenshot 2023-11-27 at 9 20 26 PM" src="https://github.com/ezishiri/Zero-Shot-Image-Classifier/assets/40304716/20e7814a-72ef-4d66-96e0-7bd979975fcd">
<img width="1076" alt="Screenshot 2023-11-27 at 9 20 52 PM" src="https://github.com/ezishiri/Zero-Shot-Image-Classifier/assets/40304716/534e018c-21be-4815-9ae8-2b56c4503f73">
<img width="834" alt="Screenshot 2023-11-27 at 9 21 46 PM" src="https://github.com/ezishiri/Zero-Shot-Image-Classifier/assets/40304716/918af3fe-11a4-47bb-a8ab-0f42b69567d0">
