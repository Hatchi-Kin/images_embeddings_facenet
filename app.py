import json
import os
from process_pipeline import ImageProcessor
import base64
from PIL import Image
import io

import numpy as np
from keras_facenet import FaceNet
from scipy.spatial.distance import cosine

from flask import Flask, render_template, request

###################################################################

def extract_embedding_from_array(image_array, model):
    embedding = model.embeddings(np.array([image_array]))[0]
    return embedding.tolist()

def load_embeddings(filename):
    with open(filename, 'r') as f:
        embeddings_dict = json.load(f)
    return embeddings_dict

def find_closest_matches(embedding, embeddings_dict, num_matches=5):
    distances = {}
    for filename, stored_embedding in embeddings_dict.items():
        distance = cosine(embedding, stored_embedding)
        distances[filename] = distance
    sorted_distances = sorted(distances.items(), key=lambda x: x[1])
    return sorted_distances[:num_matches]

###################################################################

app = Flask(__name__)

processor = ImageProcessor()
embedder = FaceNet()
PATH_TO_EMBEDDINGS = "static/Celebrity_Faces_Dataset_processed/embeddings_dataset.json"
embeddings_dict = load_embeddings(PATH_TO_EMBEDDINGS)

###################################################################
# Define a route for the homepage

@app.route('/')
def index():
    return render_template('upload.html')

###################################################################
# Define a route for finding top5 matches in an uploaded 

@app.route('/matches', methods=['POST'])
def return_matches():
    
    uploaded_image = request.files['image']
    uploaded_image_processed = processor.process_image(image_input= uploaded_image )
    new_embedding = extract_embedding_from_array(uploaded_image_processed, embedder)
    closest_matches = find_closest_matches(new_embedding, embeddings_dict, num_matches=3)
    
    closest_matches_modified = []
    for filename, distance in closest_matches:
        new_filename = os.path.join('static', filename)
        rounded_distance = round(distance, 4)
        closest_matches_modified.append((new_filename, rounded_distance))

    # Convert numpy array to PIL Image
    pil_image = Image.fromarray((uploaded_image_processed).astype(np.uint8))
    # Save PIL image to BytesIO object
    byte_arr = io.BytesIO()
    pil_image.save(byte_arr, format='PNG')
    # Encode BytesIO object in base64 and decode it to string
    encoded_image = base64.b64encode(byte_arr.getvalue()).decode('ascii')
    
    return render_template('upload.html', matches=closest_matches_modified, image=encoded_image)

###################################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
