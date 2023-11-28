from flask import Flask, request, render_template
from PIL import Image
from io import BytesIO
import os
from werkzeug.utils import secure_filename
import torch
from transformers import CLIPProcessor, CLIPModel

# Initialize Flask app
app = Flask(__name__)

# handle photo uploads for displaying
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load your model
model = CLIPModel.from_pretrained("openai/clip-vit-large-patch14")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-large-patch14")

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    result = None
    filename = None
    labels_input = ''
    if request.method == 'POST':
        if 'file' not in request.files:
            result = 'No file part'
        else:
            file = request.files['file']
            if file.filename == '':
                result = 'No selected file'
            else:
                # Extract labels from the form
                labels_input = request.form['labels']
                classes = [label.strip() for label in labels_input.split(',')]

                # Convert the Image to the format expected by CLIP model
                image = Image.open(BytesIO(file.read()))

                # classify the image
                inputs = processor(text=classes, images=image, return_tensors="pt", padding=True)
                outputs = model(**inputs)
                probs = outputs.logits_per_image.softmax(dim=1)
                class_index = torch.argmax(probs.detach())

                # Return the result
                result = classes[class_index]

    return render_template('template.html', result=result, filename=filename, labels_input=labels_input)

if __name__ == '__main__':
    app.run(debug=True)
