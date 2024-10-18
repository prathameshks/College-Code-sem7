from flask import Flask, render_template, request, redirect, url_for, send_file, flash
from PIL import Image, ExifTags
import hashlib
import os
import datetime

app = Flask(__name__)
app.secret_key = "forensic_tool_secret"
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Dictionary to track the chain of custody
chain_of_custody = {}

# Function to calculate hash of the image
def calculate_hash(file_path):
    hash_md5 = hashlib.md5()     # MD5 hash object
    hash_sha1 = hashlib.sha1()    # SHA-1 hash object

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
            hash_sha1.update(chunk)
    
    return hash_md5.hexdigest(), hash_sha1.hexdigest()

# Function to extract metadata from image using Pillow
def extract_metadata(file_path):
    metadata = {}
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        
        if exif_data:
            for tag, value in exif_data.items():
                tag_name = ExifTags.TAGS.get(tag, tag)
                metadata[tag_name] = value
        else:
            metadata['Error'] = "No EXIF metadata found"
    except Exception as e:
        metadata['Error'] = f"Error reading metadata: {str(e)}"
    return metadata

# Function for file format analysis
def file_format_analysis(file_path):
    file_size = os.path.getsize(file_path)
    image = Image.open(file_path)
    file_format = image.format
    return file_format, file_size

# Function for image content analysis (checking if it's grayscale or colored)
def image_content_analysis(file_path):
    image = Image.open(file_path)
    if image.mode == "L":
        return "Grayscale"
    else:
        return "Colored"

# Function to track chain of custody
def update_chain_of_custody(filename, md5_hash, sha1_hash, file_format, file_size):
    custody_info = {
        'filename': filename,
        'upload_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'md5_hash': md5_hash,
        'sha1_hash': sha1_hash,
        'file_format': file_format,
        'file_size': file_size
    }
    chain_of_custody[filename] = custody_info

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'imagefile' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['imagefile']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        try:
            # File format analysis
            file_format, file_size = file_format_analysis(file_path)
        except Exception as e:
            flash(f"Error: {str(e)}")
            return redirect("/error")
        
        # Extract metadata, hash values, and image content analysis
        md5_hash, sha1_hash = calculate_hash(file_path)
        metadata = extract_metadata(file_path)
        content_type = image_content_analysis(file_path)
        
        # Update chain of custody
        update_chain_of_custody(file.filename, md5_hash, sha1_hash, file_format, file_size)
        
        return render_template('analysis.html', 
                               filename=file.filename, 
                               md5_hash=md5_hash, 
                               sha1_hash=sha1_hash, 
                               metadata=metadata, 
                               file_format=file_format, 
                               file_size=file_size, 
                               content_type=content_type, 
                               chain_of_custody=chain_of_custody[file.filename])

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))

if __name__ == '__main__':
    app.run(debug=True)
