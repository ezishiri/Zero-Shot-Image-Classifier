# Zero Shot Image Classifier

## Introduction
Zero Shot Image Classifier is a tiny web app I built with Flask that allows anyone to instantly classify images dynamically based on their own set of labels. 
This app uses CLIP, can be run locally, and is super straightforward to run. 

## Features
- **Dynamic Label Input**: Users can specify their own set of class labels for image classification. Make sure they are separated by commas
- **Image Upload**: Easy upload interface for users to provide images for classification.
- **Immediate Results**: Classification results are displayed instantly on the same page after image submission.

## Installation

### Prerequisites
- Python 3.x
- Flask
- Torch
- Transformers library
- Pillow

### Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/ezishiri/Zero-Shot-Image-Classifier.git
   cd zero-shot-image-classifier
   pip install flask torch transformers Pillow
   
Run the Application
 ```bash
  python app.py
```

Access the web application at http://127.0.0.1:5000/.
