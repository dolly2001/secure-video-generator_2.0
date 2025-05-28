from flask import Flask, request, render_template, redirect, url_for
import os
from generate_video import generate_video_with_text

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def route_1():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    text = request.form.get('overlay_text')
    image = request.files['image']

    if image:
        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)
        video_filename = generate_video_with_text(image_path, text)
        return f"Image Uploaded!! Text: {text}"
    return "No Image uploaded."












































if __name__ == '__main__':
    app.run(debug=True)