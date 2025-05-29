from flask import Flask, request, render_template, redirect, url_for
import os
from generate_video import generate_video_with_text

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)




ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




@app.route('/')
def route_1():
    return render_template('index.html')




@app.route('/upload', methods=['POST'])
def upload():
    text = request.form.get('overlay_text', ' ').strip()
    image = request.files.get('image')

    if not text:
        return 'Please enter some text to overlay on the image'
    
    if not image or image.filename == '':
        return 'No image uploaded'
    
    if not allowed_file(image.filename):
        return 'only img files (png, jpg, jpeg, bmg) are allowed'

    try:

        image_path = os.path.join(UPLOAD_FOLDER, image.filename)
        image.save(image_path)
        video_filename = generate_video_with_text(image_path, text)
        
        filename = os.path.basename(video_filename)

        return redirect(url_for('download_page', filename=filename))
    except Exception as e:
        return f'Something went wrong {str(e)}'



@app.route('/download/<filename>')
def download_page(filename):
    return render_template('download.html', filename=filename)










































if __name__ == '__main__':
    app.run(ssl_context=('certs/cert.pem', 'certs/key.pem'), debug=True)