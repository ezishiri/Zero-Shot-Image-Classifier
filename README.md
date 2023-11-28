# Zero Shot Image Classifier

## Introduction
Zero Shot Image Classifier is a tiny web app I built with Flask and Huggingface that allows anyone to instantly classify images dynamically based on their own set of labels. 
This app uses CLIP, can be run locally, and is super straightforward to run. 

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
