from flask import Flask, request, render_template, redirect, url_for
import os

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
        return f"Image Uploaded!! Text: {text}"
    return "No Image uploaded."












































if __name__ == '__main__':
    app.run(debug=True)